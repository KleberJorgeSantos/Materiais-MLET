"""Synthetic Telco Customer Churn dataset generator.

Reproduces the schema and statistical flavor of the IBM Telco Customer Churn
dataset (the dataset referenced by the Fase 01 Tech Challenge) without requiring
network access. Uses fixed seeds so every student lands on the same data.

Usage::

    python dataset/generate_dataset.py            # writes to dataset/processed/
    python dataset/generate_dataset.py --rows 5000

Outputs the canonical Gold table at ``dataset/processed/telco_churn.parquet`` and a
matching ``telco_churn.csv`` for tools that prefer CSV.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from pydantic import BaseModel


class GeneratorConfig(BaseModel):
    seed: int = 42
    rows: int = 8_000
    churn_rate: float = 0.265  # near IBM dataset baseline
    output_dir: Path = Path(__file__).resolve().parent / "processed"

    model_config = {"arbitrary_types_allowed": True}


@dataclass(slots=True)
class DatasetSummary:
    rows: int
    columns: int
    churn_rate: float
    output_parquet: Path
    output_csv: Path


# ---------------------------------------------------------------------------
# Generators per feature family. Each helper returns a Series of length ``n``.
# ---------------------------------------------------------------------------

def _categorical(rng: np.random.Generator, values: list[str], probs: list[float], n: int) -> np.ndarray:
    return rng.choice(values, size=n, p=probs)


def _numeric_skewed(rng: np.random.Generator, low: float, high: float, n: int, skew: float = 1.5) -> np.ndarray:
    samples = rng.beta(skew, skew, size=n)
    return low + samples * (high - low)


def _make_dataframe(cfg: GeneratorConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.seed)
    n = cfg.rows

    customer_id = np.array([f"C{idx:07d}" for idx in range(n)])

    gender = _categorical(rng, ["Female", "Male"], [0.504, 0.496], n)
    senior_citizen = _categorical(rng, [0, 1], [0.838, 0.162], n)
    partner = _categorical(rng, ["Yes", "No"], [0.483, 0.517], n)
    dependents = _categorical(rng, ["Yes", "No"], [0.301, 0.699], n)

    tenure = rng.integers(low=0, high=73, size=n)
    phone_service = _categorical(rng, ["Yes", "No"], [0.903, 0.097], n)
    multiple_lines = np.where(
        phone_service == "No",
        "No phone service",
        _categorical(rng, ["Yes", "No"], [0.421, 0.579], n),
    )
    internet_service = _categorical(rng, ["DSL", "Fiber optic", "No"], [0.343, 0.439, 0.218], n)

    def _internet_dependent(yes_prob: float) -> np.ndarray:
        return np.where(
            internet_service == "No",
            "No internet service",
            _categorical(rng, ["Yes", "No"], [yes_prob, 1 - yes_prob], n),
        )

    online_security = _internet_dependent(0.286)
    online_backup = _internet_dependent(0.345)
    device_protection = _internet_dependent(0.343)
    tech_support = _internet_dependent(0.290)
    streaming_tv = _internet_dependent(0.384)
    streaming_movies = _internet_dependent(0.388)

    contract = _categorical(rng, ["Month-to-month", "One year", "Two year"], [0.551, 0.209, 0.240], n)
    paperless_billing = _categorical(rng, ["Yes", "No"], [0.592, 0.408], n)
    payment_method = _categorical(
        rng,
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        [0.336, 0.228, 0.219, 0.217],
        n,
    )

    base_monthly = _numeric_skewed(rng, 18.0, 119.0, n, skew=1.3)
    discount = np.where(contract == "Two year", -8.5, np.where(contract == "One year", -3.5, 0.0))
    bump = np.where(internet_service == "Fiber optic", 12.0, np.where(internet_service == "No", -10.0, 0.0))
    monthly_charges = np.round(base_monthly + discount + bump, 2)
    monthly_charges = np.clip(monthly_charges, 15.0, 130.0)

    total_charges = np.round(monthly_charges * np.maximum(tenure, 0) + rng.normal(0, 15, size=n), 2)
    total_charges = np.where(tenure == 0, 0.0, total_charges)
    total_charges = np.clip(total_charges, 0.0, None)

    # Latent churn propensity (logit) — used to draw labels with given base rate.
    logit = (
        -2.1
        + 1.6 * (contract == "Month-to-month")
        - 0.8 * (contract == "Two year")
        + 0.6 * (internet_service == "Fiber optic")
        - 0.7 * (online_security == "Yes")
        - 0.5 * (tech_support == "Yes")
        + 0.018 * (monthly_charges - 60.0)
        - 0.04 * (tenure - 30.0)
        + 0.4 * (senior_citizen == 1)
        + rng.normal(0, 0.4, size=n)
    )
    propensity = 1.0 / (1.0 + np.exp(-logit))
    # Calibrate to the target churn rate by shifting the threshold quantile.
    threshold = np.quantile(propensity, 1.0 - cfg.churn_rate)
    churn = np.where(propensity >= threshold, "Yes", "No")

    df = pd.DataFrame(
        {
            "customer_id": customer_id,
            "gender": gender,
            "senior_citizen": senior_citizen,
            "partner": partner,
            "dependents": dependents,
            "tenure": tenure,
            "phone_service": phone_service,
            "multiple_lines": multiple_lines,
            "internet_service": internet_service,
            "online_security": online_security,
            "online_backup": online_backup,
            "device_protection": device_protection,
            "tech_support": tech_support,
            "streaming_tv": streaming_tv,
            "streaming_movies": streaming_movies,
            "contract": contract,
            "paperless_billing": paperless_billing,
            "payment_method": payment_method,
            "monthly_charges": monthly_charges,
            "total_charges": total_charges,
            "churn": churn,
        }
    )
    return df


def generate(cfg: GeneratorConfig | None = None) -> DatasetSummary:
    cfg = cfg or GeneratorConfig()
    df = _make_dataframe(cfg)
    cfg.output_dir.mkdir(parents=True, exist_ok=True)

    parquet_path = cfg.output_dir / "telco_churn.parquet"
    csv_path = cfg.output_dir / "telco_churn.csv"
    try:
        df.to_parquet(parquet_path, index=False)
    except (ImportError, ValueError):
        # pyarrow/fastparquet not installed — fall back to CSV only.
        parquet_path.write_text("")
    df.to_csv(csv_path, index=False)

    return DatasetSummary(
        rows=len(df),
        columns=df.shape[1],
        churn_rate=float((df["churn"] == "Yes").mean()),
        output_parquet=parquet_path,
        output_csv=csv_path,
    )


def _parse_args() -> dict[str, Any]:
    parser = argparse.ArgumentParser(description="Generate synthetic Telco churn dataset.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--rows", type=int, default=8_000)
    parser.add_argument("--churn-rate", type=float, default=0.265)
    return vars(parser.parse_args())


def main() -> None:
    args = _parse_args()
    cfg = GeneratorConfig(seed=args["seed"], rows=args["rows"], churn_rate=args["churn_rate"])
    summary = generate(cfg)
    print("rows         :", summary.rows)
    print("columns      :", summary.columns)
    print(f"churn_rate   : {summary.churn_rate:.3f}")
    print("parquet      :", summary.output_parquet)
    print("csv          :", summary.output_csv)


if __name__ == "__main__":
    main()

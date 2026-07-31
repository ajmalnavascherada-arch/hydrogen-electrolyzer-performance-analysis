"""
Data Cleaning
"""

import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:

    print("\nCleaning dataset...")

    # Remove unnamed column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Remove duplicated percentage column
    if "H2E_f_NLR_CurrentCmd (%).1" in df.columns:
        df = df.drop(columns=["H2E_f_NLR_CurrentCmd (%).1"])

    # Forward/backward fill
    df = df.ffill().bfill()

    # Remove impossible efficiencies
    df.loc[
        df["Efficiency (kWh/kg)"] > 100,
        "Efficiency (kWh/kg)"
    ] = pd.NA

    df["Efficiency (kWh/kg)"] = (
        df["Efficiency (kWh/kg)"]
        .interpolate()
        .ffill()
        .bfill()
    )

    # Remove duplicate rows
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Removed {before-after} duplicate rows")

    print("Dataset cleaned.")

    return df


def dataset_summary(df):

    print("\nDATASET SUMMARY")
    print("-" * 50)

    print(df.shape)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())
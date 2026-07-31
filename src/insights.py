"""
Engineering Insights Module

Automatically generates engineering insights from the dataset.
"""

import numpy as np
import pandas as pd


TARGET = "H2E_f_Elec_CalcProdRate"


def generate_insights(df: pd.DataFrame):

    print("\n" + "=" * 70)
    print("ENGINEERING INSIGHTS")
    print("=" * 70)

    numerical = df.select_dtypes("number")

    # -------------------------------------------------
    # 1 Highest Hydrogen Production
    # -------------------------------------------------

    idx = df[TARGET].idxmax()

    print("\n1. Maximum Hydrogen Production")

    print(f"Production Rate : {df.loc[idx, TARGET]:.3f}")

    print(
        f"Current : "
        f"{df.loc[idx,'H2E_f_PSU_A_Current']:.2f} A"
    )

    print(
        f"Power : "
        f"{df.loc[idx,'H2E_n_PSU_A_Power (kW)']:.2f} kW"
    )

    print(
        f"Voltage : "
        f"{df.loc[idx,'Power Supply Average Voltage (Vdc)']:.2f} V"
    )

    # -------------------------------------------------
    # Strongest Correlations
    # -------------------------------------------------

    print("\n2. Variables Most Correlated With Hydrogen Production")

    corr = numerical.corr()[TARGET]

    corr = corr.drop(TARGET)

    corr = corr.abs().sort_values(ascending=False)

    print(corr.head(10))

    # -------------------------------------------------
    # Most Variable Sensor
    # -------------------------------------------------

    print("\n3. Sensor With Highest Variability")

    std = numerical.std()

    sensor = std.idxmax()

    print(sensor)

    print(f"Std Dev : {std.max():.2f}")

    # -------------------------------------------------
    # Average Operating Conditions
    # -------------------------------------------------

    print("\n4. Average Operating Conditions")

    print(
        f"Power : "
        f"{df['H2E_n_PSU_A_Power (kW)'].mean():.2f} kW"
    )

    print(
        f"Voltage : "
        f"{df['Power Supply Average Voltage (Vdc)'].mean():.2f} V"
    )

    print(
        f"Current : "
        f"{df['H2E_f_PSU_A_Current'].mean():.2f} A"
    )

    print(
        f"Efficiency : "
        f"{df['Efficiency (kWh/kg)'].mean():.2f} kWh/kg"
    )

    # -------------------------------------------------
    # Z-score Outliers
    # -------------------------------------------------

    print("\n5. Outlier Detection")

    z = np.abs(
        (
            numerical -
            numerical.mean()
        ) /
        numerical.std()
    )

    outliers = (z > 3).sum()

    print(outliers.sort_values(ascending=False).head(10))

    # -------------------------------------------------
    # Best Experiment
    # -------------------------------------------------

    print("\n6. Experiment Ranking")

    ranking = (
        df.groupby("Experiment")[TARGET]
        .mean()
        .sort_values(ascending=False)
    )

    print(ranking)

    print("=" * 70)
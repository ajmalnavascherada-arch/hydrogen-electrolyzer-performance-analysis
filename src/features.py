"""
Engineering Feature Calculations
"""

import numpy as np
import pandas as pd


def add_engineering_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived engineering features.
    """

    print("\nCreating engineering features...")

    # Power-to-Wind ratio
    df["Power_to_Wind_Ratio"] = (
        df["H2E_n_PSU_A_Power (kW)"] /
        df["GE 1.5 MW Wind Turbine Power (kW)"]
    )

    # Hydrogen production efficiency
    df["Hydrogen_per_kW"] = (
        df["H2E_f_Elec_CalcProdRate"] /
        df["H2E_n_PSU_A_Power (kW)"]
    )

    # Voltage * Current
    df["Electrical_Power_Calculated"] = (
        df["Power Supply Average Voltage (Vdc)"] *
        df["H2E_f_PSU_A_Current"]
    ) / 1000

    # Difference between measured and calculated power
    df["Power_Error"] = (
        df["Electrical_Power_Calculated"] -
        df["H2E_n_PSU_A_Power (kW)"]
    )

    print("Engineering features created.")

    return df
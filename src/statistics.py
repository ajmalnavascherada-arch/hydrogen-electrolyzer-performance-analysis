"""
Statistical Analysis
"""

import pandas as pd


def descriptive_statistics(df: pd.DataFrame):

    print("\nDESCRIPTIVE STATISTICS")
    print("-" * 60)

    print(df.describe().T)
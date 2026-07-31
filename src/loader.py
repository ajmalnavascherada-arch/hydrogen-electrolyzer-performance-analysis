"""
Dataset Loader
"""

from pathlib import Path

import pandas as pd


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load CSV dataset.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    DataFrame
    """

    print("\nLoading dataset...")

    df = pd.read_csv(file_path)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df
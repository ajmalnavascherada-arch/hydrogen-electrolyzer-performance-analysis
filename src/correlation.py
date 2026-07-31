"""
Correlation Analysis
"""

import matplotlib.pyplot as plt
import pandas as pd


def correlation_heatmap(df):

    corr = df.select_dtypes("number").corr()

    plt.figure(figsize=(18,14))

    plt.imshow(corr, cmap="coolwarm")

    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=90,
        fontsize=8
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns,
        fontsize=8
    )

    plt.tight_layout()

    plt.savefig(
        "figures/correlation_heatmap.png",
        dpi=300
    )

    plt.close()

    print("Correlation heatmap saved.")
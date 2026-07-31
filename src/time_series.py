"""
Time Series Visualizations
"""

import matplotlib.pyplot as plt


def plot_series(df, column):

    plt.figure(figsize=(14,5))

    plt.plot(df[column], linewidth=0.8)

    plt.title(column)

    plt.xlabel("Sample")

    plt.ylabel(column)

    plt.grid(alpha=0.3)

    filename = column.replace("/", "_")
    filename = filename.replace(" ", "_")

    plt.tight_layout()

    plt.savefig(
        f"figures/{filename}.png",
        dpi=300
    )

    plt.close()
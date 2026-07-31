"""
Visualization Utilities
"""

from pathlib import Path

import matplotlib.pyplot as plt


FIGURE_DIR = Path("figures")
FIGURE_DIR.mkdir(exist_ok=True)

def anomaly_plot(df):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(12,6))

    normal = df[df["Anomaly"] == 1]

    anomaly = df[df["Anomaly"] == -1]

    plt.scatter(
        normal["H2E_f_PSU_A_Current"],
        normal["H2E_f_Elec_CalcProdRate"],
        s=5,
        alpha=0.3,
        label="Normal"
    )

    plt.scatter(
        anomaly["H2E_f_PSU_A_Current"],
        anomaly["H2E_f_Elec_CalcProdRate"],
        s=15,
        label="Anomaly"
    )

    plt.xlabel("Current (A)")
    plt.ylabel("Hydrogen Production (kg/hr)")
    plt.title("Anomaly Detection")

    plt.legend()

    save_plot("anomaly_detection")
def save_plot(name: str):

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR / f"{name}.png",
        dpi=300
    )

    plt.close()


def line_plot(df, x, y, title, xlabel, ylabel, filename):

    plt.figure(figsize=(12, 5))

    plt.plot(df[x], df[y])

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.grid(True)

    save_plot(filename)
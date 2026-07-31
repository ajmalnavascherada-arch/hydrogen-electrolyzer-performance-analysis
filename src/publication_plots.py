"""
Publication Quality Engineering Plots
"""

from pathlib import Path
import matplotlib.pyplot as plt

FIGURES = Path("figures")
FIGURES.mkdir(exist_ok=True)

plt.rcParams.update({
    "figure.figsize": (12, 6),
    "figure.dpi": 150,
    "font.size": 12,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def save(name):
    plt.tight_layout()
    plt.savefig(FIGURES / f"{name}.png", dpi=300)
    plt.close()


def power_vs_hydrogen(df):

    plt.figure()

    plt.scatter(
        df["H2E_n_PSU_A_Power (kW)"],
        df["H2E_f_Elec_CalcProdRate"],
        s=8,
        alpha=0.4,
    )

    plt.xlabel("Electrolyzer Power (kW)")
    plt.ylabel("Hydrogen Production (kg/hr)")
    plt.title("Hydrogen Production vs Electrolyzer Power")

    save("power_vs_hydrogen")


def voltage_vs_current(df):

    plt.figure()

    plt.scatter(
        df["H2E_f_PSU_A_Current"],
        df["Power Supply Average Voltage (Vdc)"],
        s=8,
        alpha=0.4,
    )

    plt.xlabel("Current (A)")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage vs Current")

    save("voltage_vs_current")


def efficiency_histogram(df):

    plt.figure()

    plt.hist(
        df["Efficiency (kWh/kg)"],
        bins=40
    )

    plt.xlabel("Efficiency (kWh/kg)")
    plt.ylabel("Frequency")
    plt.title("Efficiency Distribution")

    save("efficiency_histogram")
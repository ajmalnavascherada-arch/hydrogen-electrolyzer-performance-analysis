"""
Hydrogen Electrolyzer Performance Analysis

Author: Ajmal Navas Cherada

Main execution file.
"""

from pathlib import Path

from src.loader import load_dataset
from src.cleaning import clean_dataset, dataset_summary
from src.statistics import descriptive_statistics
from src.features import add_engineering_features
from src.correlation import correlation_heatmap
from src.insights import generate_insights
from src.dashboard import print_dashboard
from src.anomaly import detect_anomalies
from src.visualization import (
    line_plot,
    anomaly_plot
)
from src.publication_plots import (
    power_vs_hydrogen,
    voltage_vs_current,
    efficiency_histogram,
)
from src.time_series import plot_series

DATA_PATH = Path("data") / "combined_historical_wind_experiments.csv"


def main():

    print("=" * 60)
    print("HYDROGEN ELECTROLYZER PERFORMANCE ANALYSIS")
    print("=" * 60)

    # Load dataset
    df = load_dataset(DATA_PATH)

    # Clean dataset
    df = clean_dataset(df)

    # Dataset overview
    dataset_summary(df)

    # Statistical analysis
    descriptive_statistics(df)

    # Feature engineering
    df = add_engineering_features(df)
    df = detect_anomalies(df)
    # -----------------------------
    # Visualization starts here
    # -----------------------------

    correlation_heatmap(df)
    power_vs_hydrogen(df)

    voltage_vs_current(df)

    efficiency_histogram(df)

    anomaly_plot(df)
    generate_insights(df)
    print_dashboard(df)
    anomaly_plot(df)
    plot_series(df, "GE 1.5 MW Wind Turbine Power (kW)")

    plot_series(df, "H2E_n_PSU_A_Power (kW)")

    plot_series(df, "Efficiency (kWh/kg)")

    plot_series(df, "H2E_f_Elec_CalcProdRate")

    plot_series(df, "Power Supply Average Voltage (Vdc)")

    plot_series(df, "H2E_f_PSU_A_Current")

    print("\nNew Features")

    print(df[[
        "Power_to_Wind_Ratio",
        "Hydrogen_per_kW",
        "Electrical_Power_Calculated",
        "Power_Error"
    ]].head())

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
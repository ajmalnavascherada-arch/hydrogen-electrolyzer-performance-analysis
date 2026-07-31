"""
Console Dashboard
"""

from src.kpi import calculate_kpis


def print_dashboard(df):

    kpis = calculate_kpis(df)

    print("\n")
    print("=" * 70)
    print("HYDROGEN ELECTROLYZER PERFORMANCE DASHBOARD")
    print("=" * 70)

    for key, value in kpis.items():

        if isinstance(value, float):
            print(f"{key:<40}{value:>12.2f}")
        else:
            print(f"{key:<40}{value}")

    print("=" * 70)
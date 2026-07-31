"""
Key Performance Indicators (KPIs)
"""

import pandas as pd


def calculate_kpis(df: pd.DataFrame):

    kpis = {}

    kpis["Total Samples"] = len(df)

    kpis["Experiments"] = df["Experiment"].nunique()

    kpis["Average Wind Power (kW)"] = \
        df["GE 1.5 MW Wind Turbine Power (kW)"].mean()

    kpis["Maximum Wind Power (kW)"] = \
        df["GE 1.5 MW Wind Turbine Power (kW)"].max()

    kpis["Average Electrolyzer Power (kW)"] = \
        df["H2E_n_PSU_A_Power (kW)"].mean()

    kpis["Maximum Electrolyzer Power (kW)"] = \
        df["H2E_n_PSU_A_Power (kW)"].max()

    kpis["Average Hydrogen Production (kg/hr)"] = \
        df["H2E_f_Elec_CalcProdRate"].mean()

    kpis["Maximum Hydrogen Production (kg/hr)"] = \
        df["H2E_f_Elec_CalcProdRate"].max()

    kpis["Average Efficiency (kWh/kg)"] = \
        df["Efficiency (kWh/kg)"].mean()

    kpis["Minimum Efficiency (kWh/kg)"] = \
        df["Efficiency (kWh/kg)"].min()

    kpis["Maximum Voltage (V)"] = \
        df["Power Supply Average Voltage (Vdc)"].max()

    kpis["Maximum Current (A)"] = \
        df["H2E_f_PSU_A_Current"].max()

    return kpis
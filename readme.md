# Hydrogen Electrolyzer Performance Analysis using Python

> A research-oriented Python project for analyzing industrial hydrogen electrolyzer performance using data analytics, statistical analysis, machine learning, and engineering visualization.

---

## Overview

This project presents a complete data analysis pipeline for an industrial-scale hydrogen electrolyzer powered by renewable wind energy. Using real operational data, the project performs data preprocessing, engineering feature extraction, statistical analysis, anomaly detection, and visualization to evaluate system performance and identify key operational insights.

The repository demonstrates practical applications of Python in renewable energy engineering, hydrogen technologies, electrochemical systems, and scientific computing.

---

## Objectives

- Analyze industrial hydrogen electrolyzer operational data
- Perform automated data cleaning and preprocessing
- Generate engineering performance metrics
- Visualize system behavior using publication-quality figures
- Detect abnormal operating conditions using machine learning
- Produce engineering insights through statistical analysis

---

## Dataset

The dataset contains operational measurements from a wind-powered hydrogen electrolyzer system.

### Dataset Summary

| Property | Value |
|----------|------:|
| Samples | 28,798 |
| Features | 30 |
| Experiments | 2 |
| Missing Values | Automatically handled |
| Duplicate Rows | Removed |

### Measured Parameters

- Wind Turbine Power
- Electrolyzer Power
- Current Command
- Power Supply Voltage
- Power Supply Current
- Hydrogen Production Rate
- Efficiency
- Pressure Sensors
- Temperature Sensors
- Water Level
- Water Resistivity
- Dew Point
- Hydrogen Safety Measurements

---

# Project Structure

```text
hydrogen-electrolyzer-performance-analysis/

│
├── data/
│   └── combined_historical_wind_experiments.csv
│
├── figures/
│
├── notebooks/
│
├── report/
│
├── src/
│   ├── loader.py
│   ├── cleaning.py
│   ├── features.py
│   ├── statistics.py
│   ├── visualization.py
│   ├── correlation.py
│   ├── anomaly.py
│   ├── insights.py
│   ├── dashboard.py
│   ├── publication_plots.py
│   └── report.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Workflow

```text
Raw Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Statistical Analysis
      │
      ▼
Correlation Analysis
      │
      ▼
Machine Learning
(Anomaly Detection)
      │
      ▼
Engineering Insights
      │
      ▼
Publication Quality Figures
      │
      ▼
Engineering Report
```

---

# Features

## Data Processing

- Automatic dataset loading
- Missing value handling
- Duplicate removal
- Outlier filtering
- Dataset validation

---

## Engineering Feature Engineering

Derived engineering metrics include:

- Power-to-Wind Ratio
- Hydrogen Production per kW
- Calculated Electrical Power
- Power Error Analysis

---

## Statistical Analysis

- Descriptive statistics
- Correlation analysis
- Dataset summary
- Operating condition statistics

---

## Machine Learning

Isolation Forest is used to automatically identify abnormal operating conditions.

Detected outputs include:

- Operational anomalies
- Sensor abnormalities
- Outlier visualization

---

## Engineering Insights

The analysis automatically reports:

- Maximum hydrogen production
- Average operating conditions
- Most correlated variables
- Highest variability sensor
- Experiment ranking
- Operational outliers

---

## Publication Quality Visualizations

The project automatically generates figures including:

- Hydrogen Production vs Power
- Voltage vs Current
- Efficiency Distribution
- Correlation Heatmap
- Anomaly Detection
- Time-Series Sensor Plots

All figures are exported in high-resolution PNG format suitable for reports and publications.

---

# Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- OpenPyXL
- Jupyter Notebook

---

# Installation

Clone the repository

```bash
git clone https://github.com/ajmalnavascherada-arch/hydrogen-electrolyzer-performance-analysis.git
```

Navigate to the project

```bash
cd hydrogen-electrolyzer-performance-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# Example Output

The project automatically generates

```
figures/

correlation_heatmap.png

power_vs_hydrogen.png

voltage_vs_current.png

efficiency_histogram.png

anomaly_detection.png
```

and

```
report/

summary.txt
```

---

# Example Engineering KPIs

The dashboard reports key performance indicators such as

- Average Wind Power
- Maximum Electrolyzer Power
- Hydrogen Production Rate
- Electrolyzer Efficiency
- Maximum Current
- Maximum Voltage
- Experiment Comparison

---

# Engineering Applications

This project demonstrates practical skills relevant to:

- Hydrogen Energy Systems
- Electrochemical Engineering
- Renewable Energy
- Energy System Integration
- Process Engineering
- Scientific Computing
- Industrial Data Analytics
- Predictive Maintenance
- Digital Engineering

---

# Future Improvements

Planned enhancements include

- Interactive Plotly Dashboard
- Predictive Maintenance Models
- Regression Analysis
- Time-Series Forecasting
- Remaining Useful Life Estimation
- Sensor Fault Detection
- Real-Time Monitoring Dashboard
- Streamlit Web Application
- Docker Deployment
- CI/CD using GitHub Actions

---

# Skills Demonstrated

- Python Programming
- Data Analysis
- Data Visualization
- Machine Learning
- Statistical Analysis
- Engineering Problem Solving
- Feature Engineering
- Scientific Computing
- Renewable Energy Analytics
- Hydrogen Technologies

---

# Author

**Ajmal Navas Cherada**

M.Sc. Chemical and Energy Engineering

Otto von Guericke University Magdeburg

📧 ajmalnavascherada@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/ajmal-navas-cherada-224151171

💻 GitHub: https://github.com/ajmalnavascherada-arch

---

# License

This project is released under the MIT License.

---

## Acknowledgements

This project was developed as a personal engineering portfolio to demonstrate practical skills in hydrogen technologies, industrial data analytics, renewable energy systems, and scientific Python programming. The analysis is based on publicly available operational data and is intended for educational and research purposes.

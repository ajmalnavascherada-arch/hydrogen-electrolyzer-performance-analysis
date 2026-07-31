"""
Anomaly Detection
"""

from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    numerical = df.select_dtypes("number")

    model = IsolationForest(
        contamination=0.01,
        random_state=42
    )

    prediction = model.fit_predict(numerical)

    df["Anomaly"] = prediction

    anomalies = (prediction == -1).sum()

    print(f"\nDetected anomalies : {anomalies}")

    return df
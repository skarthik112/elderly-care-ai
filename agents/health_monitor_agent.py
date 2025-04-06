import pandas as pd

class HealthMonitorAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)

        # ✅ Add this line to ensure timestamp column is datetime
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])

    def check_vitals(self):
        alerts = []
        for _, row in self.data.iterrows():
            if str(row['Alert Triggered (Yes/No)']).strip().lower() == 'yes':
                msg = (
                    f"[{row['Timestamp']}] - High Vitals Detected:\n"
                    f"  → Heart Rate: {row['Heart Rate']} bpm\n"
                    f"  → BP: {row['Blood Pressure']}\n"
                    f"  → Glucose: {row['Glucose Levels']} mg/dL\n"
                    f"  → SpO2: {row['Oxygen Saturation (SpO₂%)']}%\n"
                )
                alerts.append(msg)
        return alerts

import pandas as pd

class HealthMonitorAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)

        if 'Timestamp' in self.data.columns:
            self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'], errors='coerce')
        else:
            self.data['Timestamp'] = pd.NaT  # Create empty timestamp column if missing

    def check_vitals(self):
        alerts = []

        for _, row in self.data.iterrows():
            alert_triggered = str(row.get('Alert Triggered (Yes/No)', '')).strip().lower() == 'yes'

            if alert_triggered:
                parts = [f"[{row.get('Timestamp', 'Unknown Time')}] - High Vitals Detected:"]
                
                if 'Heart Rate' in row:
                    parts.append(f"  → Heart Rate: {row['Heart Rate']} bpm")
                if 'Blood Pressure' in row:
                    parts.append(f"  → BP: {row['Blood Pressure']}")
                if 'Glucose Levels' in row:
                    parts.append(f"  → Glucose: {row['Glucose Levels']} mg/dL")
                if 'Oxygen Saturation (SpO₂%)' in row:
                    parts.append(f"  → SpO2: {row['Oxygen Saturation (SpO₂%)']}%")
                
                alert_msg = "\n".join(parts)
                alerts.append(alert_msg)

        return alerts

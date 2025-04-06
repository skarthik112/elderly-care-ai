import pandas as pd

class SafetyAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)

    def check_safety(self):
        safety_alerts = []
        for _, row in self.data.iterrows():
            fall_detected = row.get('Fall Detected', 'N/A')
            smoke_detected = row.get('Smoke Detected', 'N/A')
            unusual_activity = row.get('Unusual Activity', 'N/A')

            alert_msg = f"Safety Alert: Fall: {fall_detected}, Smoke: {smoke_detected}, Unusual Activity: {unusual_activity}"
            safety_alerts.append(alert_msg)

        return safety_alerts

import pandas as pd

class SafetyAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)


    def check_safety(self):
        alerts = []
        for _, row in self.data.iterrows():
            if str(row['Fall Detected (Yes/No)']).strip().lower() == 'yes':
                msg = (
                    f"[{row['Timestamp']}] - Fall Detected!\n"
                    f"  → Location: {row['Location']}\n"
                    f"  → Inactivity: {row['Post-Fall Inactivity Duration (Seconds)']} seconds"
                )
                alerts.append(msg)
        return alerts

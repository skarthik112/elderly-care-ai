import pandas as pd
from datetime import datetime

class MedicationAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)

    def check_reminders(self):
        now_time = datetime.now().strftime('%H:%M')
        reminders = []

        for _, row in self.data.iterrows():
            scheduled = row['Scheduled Time'][:5]  # HH:MM
            if scheduled == now_time and str(row['Reminder Sent (Yes/No)']).strip().lower() != 'yes':
                msg = f"Reminder: {row['Reminder Type']} scheduled at {scheduled}"
                reminders.append(msg)
        return reminders

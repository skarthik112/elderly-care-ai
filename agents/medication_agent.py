import pandas as pd

class MedicationAgent:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.read_csv(data)

        # Ensure 'Scheduled Time' is in correct format
        if 'Scheduled Time' in self.data.columns:
            self.data['Scheduled Time'] = pd.to_datetime(self.data['Scheduled Time'], errors='coerce')

    def check_medications(self):
        reminders = []
        for _, row in self.data.iterrows():
            medication_name = row.get('Medication Name', 'N/A')
            scheduled_time = row.get('Scheduled Time', 'N/A')
            status = row.get('Status', 'N/A')

            reminder_msg = f"[{scheduled_time}] - Medication Reminder: {medication_name}, Status: {status}"
            reminders.append(reminder_msg)

        return reminders

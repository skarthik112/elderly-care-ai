class CaregiverAgent:
    def notify(self, alert_type, messages):
        print(f"\n📬 NOTIFICATION to Caregiver - {alert_type}")
        for msg in messages:
            print(msg)

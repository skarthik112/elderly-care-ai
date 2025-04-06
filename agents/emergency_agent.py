class EmergencyAgent:
    def handle_emergency(self, alert_type, messages):
        print(f"\n🚨 EMERGENCY - {alert_type} 🚨")
        for msg in messages:
            print(msg)

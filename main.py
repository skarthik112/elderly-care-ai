from agents.health_monitor_agent import HealthMonitorAgent
from agents.safety_agent import SafetyAgent
from agents.medication_agent import MedicationAgent
from agents.emergency_agent import EmergencyAgent
from agents.caregiver_agent import CaregiverAgent

# Initialize agents
health_agent = HealthMonitorAgent("data/health_monitoring.csv")
safety_agent = SafetyAgent("data/safety_monitoring.csv")
med_agent = MedicationAgent("data/daily_reminder.csv")
emergency_agent = EmergencyAgent()
caregiver_agent = CaregiverAgent()

def run_simulation():
    print("\n--- 🧠 Elderly Care AI Assistant: Simulation Started ---")

    # Step 1: Health Monitoring
    health_alerts = health_agent.check_vitals()
    if health_alerts:
        emergency_agent.handle_emergency("Health Issue", health_alerts)
        caregiver_agent.notify("Health Alert", health_alerts)

    # Step 2: Safety Monitoring
    safety_alerts = safety_agent.check_safety()
    if safety_alerts:
        emergency_agent.handle_emergency("Safety Issue", safety_alerts)
        caregiver_agent.notify("Safety Alert", safety_alerts)

    # Step 3: Medication Reminders
    med_reminders = med_agent.check_reminders()
    for reminder in med_reminders:
        caregiver_agent.notify("Medication Reminder", [reminder])

    print("\n✅ Simulation Completed.")

if __name__ == "__main__":
    run_simulation()

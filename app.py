import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
from datetime import datetime
from agents.health_monitor_agent import HealthMonitorAgent
from agents.safety_agent import SafetyAgent
from agents.medication_agent import MedicationAgent
from agents.emergency_agent import EmergencyAgent
from agents.caregiver_agent import CaregiverAgent

# Streamlit config
st.set_page_config(page_title="Elderly Care AI Assistant", layout="wide")

# App title
st.title("👵👴 Elderly Care AI Assistant")

st.markdown("This assistant monitors **health**, **safety**, and **medication**, and notifies caregivers in real-time.")

# -------------------------------------
# 📂 Sidebar – Upload Files
# -------------------------------------
st.sidebar.title("📂 Upload Your Own CSV Files (Optional)")
health_file = st.sidebar.file_uploader("🩺 Upload Health Monitoring CSV", type="csv")
safety_file = st.sidebar.file_uploader("🛡️ Upload Safety Monitoring CSV", type="csv")
reminder_file = st.sidebar.file_uploader("💊 Upload Medication Reminder CSV", type="csv")

# -------------------------------------
# 📄 Load CSVs – Uploaded or Default
# -------------------------------------
def load_csv(file, default_path):
    if file is not None:
        return pd.read_csv(file)
    return pd.read_csv(default_path)

health_df = load_csv(health_file, "data/health_monitoring.csv")
safety_df = load_csv(safety_file, "data/safety_monitoring.csv")
reminder_df = load_csv(reminder_file, "data/daily_reminder.csv")

# -------------------------------------
# 🤖 Initialize Agents
# -------------------------------------
health_agent = HealthMonitorAgent(health_df)
safety_agent = SafetyAgent(safety_df)
med_agent = MedicationAgent(reminder_df)
emergency_agent = EmergencyAgent()
caregiver_agent = CaregiverAgent()

# -------------------------------------
# Utility function to check if required columns exist
# -------------------------------------
def check_column_exists(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    return missing_columns

# -------------------------------------
# ▶️ Run Simulation Button
# -------------------------------------
if st.button("▶️ Run Simulation"):
    st.markdown("### 🔍 Simulation Results:")

    col1, col2, col3 = st.columns(3)

    # 🩺 Health Monitoring
    with col1:
        st.markdown("### 💓 Health Monitoring")
        health_alerts = health_agent.check_vitals()
        if health_alerts:
            st.error("🚨 Health Alerts Detected:")
            for msg in health_alerts:
                st.markdown(f"- {msg}")
            caregiver_agent.notify("Health Emergency", health_alerts)
        else:
            st.success("✅ No health issues detected.")

    # 🛡️ Safety Monitoring
    with col2:
        st.markdown("### 🛡️ Safety Monitoring")
        safety_alerts = safety_agent.check_safety()
        if safety_alerts:
            st.warning("⚠️ Safety Alerts Detected:")
            for msg in safety_alerts:
                st.markdown(f"- {msg}")
            caregiver_agent.notify("Safety Emergency", safety_alerts)
        else:
            st.success("✅ No safety issues detected.")

    # 💊 Medication Reminders
    with col3:
        st.markdown("### 💊 Medication Reminders")
        med_reminders = med_agent.check_medications()
        if med_reminders:
            st.info("💊 Medication Reminders:")
            for reminder in med_reminders:
                st.markdown(f"- {reminder}")
            caregiver_agent.notify("Medication Reminder", med_reminders)
        else:
            st.success("✅ No medication reminders right now.")

    st.success("✅ Simulation complete.")

else:
    st.info("Click the button above to start the AI assistant simulation.")

st.markdown("---")
st.markdown("## 📈 Health Vitals Trends")

if st.checkbox("📊 Show Vitals Charts", value=True):
    # Check for missing columns before plotting
    missing_columns = check_column_exists(health_agent.data, ['Heart Rate', 'Glucose Levels', 'Oxygen Saturation (SpO₂%)', 'Timestamp'])

    if not missing_columns:
        st.markdown("### Heart Rate Over Time")
        st.altair_chart(
            alt.Chart(health_agent.data).mark_line().encode(
                x='Timestamp:T',
                y='Heart Rate:Q',
                tooltip=['Timestamp', 'Heart Rate']
            ).properties(width=700, height=300),
            use_container_width=True
        )

        st.markdown("### Glucose Levels Over Time")
        st.altair_chart(
            alt.Chart(health_agent.data).mark_line(color='orange').encode(
                x='Timestamp:T',
                y='Glucose Levels:Q',
                tooltip=['Timestamp', 'Glucose Levels']
            ).properties(width=700, height=300),
            use_container_width=True
        )

        st.markdown("### SpO₂ Levels Over Time")
        st.altair_chart(
            alt.Chart(health_agent.data).mark_line(color='green').encode(
                x='Timestamp:T',
                y='Oxygen Saturation (SpO₂%):Q',
                tooltip=['Timestamp', 'Oxygen Saturation (SpO₂%)']
            ).properties(width=700, height=300),
            use_container_width=True
        )
    else:
        for column in missing_columns:
            st.warning(f"⚠️ Missing required column: {column} for the health vitals charts.")
        
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 10px; font-size: 0.9em; color: gray;'>
        🤖 Built with ❤️ for the Hackathon &nbsp;|&nbsp; Elderly Care AI Assistant Dashboard &nbsp;|&nbsp; © 2025
    </div>
    """,
    unsafe_allow_html=True
)

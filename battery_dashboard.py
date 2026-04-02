
import streamlit as st
import pandas as pd
import numpy as np

# Title and Instructions
st.title("🔋 Battery Cycle Anomaly Detector")
st.markdown("""
Upload a CSV summary (e.g., cycle_summary.csv) and select a cycle to view its anomaly risk.
""")
uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'cycle_id' not in df.columns:
        st.error("The file must contain a 'cycle_id' column.")
    else:
        selected_cycle = st.selectbox("Select a cycle:", df['cycle_id'].unique())
        selected_row = df[df['cycle_id'] == selected_cycle].iloc[0]

        # Calculate anomaly score (basic Z-score sum for key fields)
        stats = {
            'temp_max_mean': df['temp_max'].mean(),
            'temp_max_std': df['temp_max'].std(),
            'current_mean_mean': df['current_mean'].mean(),
            'current_mean_std': df['current_mean'].std(),
            'voltage_mean_mean': df['voltage_mean'].mean(),
            'voltage_mean_std': df['voltage_mean'].std()
        }

        def detect_anomaly(temp, current, voltage, stats):
            z_temp = (temp - stats['temp_max_mean']) / stats['temp_max_std']
            z_current = (current - stats['current_mean_mean']) / stats['current_mean_std']
            z_voltage = (voltage - stats['voltage_mean_mean']) / stats['voltage_mean_std']
            score = abs(z_temp) + abs(z_current) + abs(z_voltage)
            return score, score > 4.0

        score, is_anomaly = detect_anomaly(
            selected_row['temp_max'],
            selected_row['current_mean'],
            selected_row['voltage_mean'],
            stats
        )

        st.metric("Anomaly Score", f"{score:.2f}")
        st.success("No anomaly detected") if not is_anomaly else st.error("⚠️ Anomaly Detected!")

        # Show basic trip metrics
        st.subheader("Cycle Metrics")
        st.dataframe(selected_row.to_frame())

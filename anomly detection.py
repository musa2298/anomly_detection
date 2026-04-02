import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SPICE Solar Dashboard",
    layout="wide"
)

# Load data
df = pd.read_csv("data/solar_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Calculations
df['total_power'] = df[['inverter1','inverter2','inverter3']].sum(axis=1)
df['avg_power'] = df[['inverter1','inverter2','inverter3']].mean(axis=1)

mean = df['avg_power'].mean()
std = df['avg_power'].std()

df['z_score'] = (df['avg_power']-mean)/std
df['anomaly'] = df['z_score'].apply(lambda x: "Anomaly" if abs(x)>2 else "Normal")

# Sidebar
with st.sidebar:
    selected = option_menu(
        "Solar Monitoring",
        ["Dashboard","Anomaly Detection","Inverter Analysis"],
        icons=["speedometer","exclamation-triangle","cpu"]
    )

st.title("☀️ SPICE Solar Plant Monitoring")

# KPI cards
col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Production (kWh)", round(df['total_power'].sum(),2))
col2.metric("Average Output", round(df['avg_power'].mean(),2))
col3.metric("Anomaly Days", df[df['anomaly']=="Anomaly"].shape[0])
col4.metric("Total Records", df.shape[0])

st.divider()

# Dashboard Page
if selected=="Dashboard":

    st.subheader("Power Production Trend")

    fig = px.line(df,
                  x="date",
                  y="total_power")

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Inverter Performance")

    fig2 = px.line(
        df,
        x="date",
        y=['inverter1','inverter2','inverter3']
    )

    st.plotly_chart(fig2,use_container_width=True)

# Anomaly Page
elif selected=="Anomaly Detection":

    st.subheader("Z-Score Anomaly Detection")

    fig3 = px.scatter(
        df,
        x="date",
        y="z_score",
        color="anomaly"
    )

    st.plotly_chart(fig3,use_container_width=True)

    st.subheader("Outlier Days")

    st.dataframe(df[df['anomaly']=="Anomaly"])

# Inverter Page
elif selected=="Inverter Analysis":

    st.subheader("Inverter Output Distribution")

    fig4 = px.box(
        df,
        y=['inverter1','inverter2','inverter3']
    )

    st.plotly_chart(fig4,use_container_width=True)

    df['rolling_std'] = df['avg_power'].rolling(7).std()

    st.subheader("Rolling Variability")

    fig5 = px.line(
        df,
        x="date",
        y="rolling_std"
    )

    st.plotly_chart(fig5,use_container_width=True)
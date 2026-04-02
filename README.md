
# 🔋 EV Battery Anomaly Detection

This project analyzes real-world electric vehicle (EV) battery data to detect potential anomalies using statistical methods and clustering techniques. It includes both exploratory analysis in a Jupyter notebook and an interactive dashboard built with Streamlit for live anomaly scoring.

---

## 📂 Project Structure

- `battery.ipynb`: Full analysis notebook with data cleaning, anomaly detection, and clustering.
- `cycle_summary.csv`: Trip-level summary data containing temperature, voltage, and current metrics.
- `battery_dashboard.py`: Streamlit app to upload a CSV and visualize anomaly scores per trip.

---

## 📈 Key Features

- **Z-score-based Anomaly Detection**: Detects unusual cycles based on max battery temperature, current draw, and voltage drop.
- **KMeans Clustering**: Groups driving cycles into interpretable usage types (e.g., Normal, High Stress, Urban Mild).
- **Trip Deep Dives**: Investigates trips like TripA32, which exhibit unusual thermal behavior.
- **Interactive Streamlit Dashboard**: Upload your own summary file and get instant anomaly diagnostics with visual feedback.

---

## 🚀 How to Run the Streamlit App

```bash
# Step 1: Install dependencies
pip install streamlit pandas numpy

# Step 2: Run the dashboard locally
streamlit run battery_dashboard.py
```

Then open the link (usually http://localhost:8501) in your browser.

---

## 🧠 Project Highlights

- Anomaly score = sum of Z-scores across temperature, current, and voltage.
- Real-time scoring function built for potential telemetry deployment.
- PCA + KMeans used to reduce dimensionality and group similar trips.
- Flagged trips can be exported or tracked by engineers for maintenance.

---

## 🧪 Example Use Case

> “TripA32” was identified as a thermal anomaly. A deep dive showed elevated current draw and low voltage early in the drive, possibly due to heating load — a pattern common in the “High Stress” cluster.

---

## 💬 Contact

Built by Fatima Malikli  
[GitHub Profile](https://github.com/Fatima138)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Village Insights", layout="centered")

st.title("🌱 Smart Village Insights")
st.write("A simple data-driven dashboard for Electricity, Water, and Crop Monitoring")

# ---------------------------
# Section 1: Electricity Cuts
# ---------------------------
st.header("⚡ Electricity Cut Analysis")

electricity_data = {
    "Day": list(range(1, 31)),
    "Electricity_Cut_Hours": [2,3,4,1,0,2,5,3,2,1,
                              4,6,2,3,5,1,0,2,3,4,
                              6,5,3,2,1,4,3,2,5,4]
}
df = pd.DataFrame(electricity_data)

fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.plot(df["Day"], df["Electricity_Cut_Hours"], marker='o', linestyle='-')
ax1.set_title("Daily Electricity Cut Hours (30 Days)")
ax1.set_xlabel("Day")
ax1.set_ylabel("Hours Without Power")
ax1.grid(True)
st.pyplot(fig1)

st.caption("This chart shows fluctuation of electricity cuts; some days reach up to 6 hours.")

# ---------------------------
# Section 2: Water Usage
# ---------------------------
st.header("💧 Water Usage vs Wastage")

water_data = {
    "Day": list(range(1, 11)),
    "Water_Used": [150, 180, 200, 170, 160, 190, 210, 180, 175, 165],
    "Water_Wasted": [20, 30, 25, 15, 10, 35, 40, 20, 15, 25]
}
water_df = pd.DataFrame(water_data)

fig2, ax2 = plt.subplots(figsize=(8,4))
water_df.plot(x="Day", y=["Water_Used", "Water_Wasted"], kind="bar", ax=ax2)
ax2.set_title("Water Usage vs Wastage (10 Days)")
ax2.set_xlabel("Day")
ax2.set_ylabel("Liters")
st.pyplot(fig2)

st.caption("On certain days, wastage peaked at ~40 liters due to tank overflow conditions.")

# ---------------------------
# Section 3: Crop Yield
# ---------------------------
st.header("🌾 Rainfall vs Crop Yield")

crop_data = {
    "Rainfall (mm)": [50, 100, 150, 200, 250, 300],
    "Crop_Yield (quintals/acre)": [10, 20, 35, 45, 40, 30]
}
crop_df = pd.DataFrame(crop_data)

fig3, ax3 = plt.subplots(figsize=(8,4))
ax3.plot(crop_df["Rainfall (mm)"], crop_df["Crop_Yield (quintals/acre)"], marker='o')
ax3.set_title("Rainfall vs Crop Yield")
ax3.set_xlabel("Rainfall (mm)")
ax3.set_ylabel("Yield (quintals/acre)")
ax3.grid(True)
st.pyplot(fig3)

st.caption("Yield improves as rainfall increases up to ~200 mm, then starts dropping with excess water.")


import streamlit as st
import pandas as pd

st.set_page_config(page_title="PitchAlert 2025", layout="wide")
st.title("🎯 PitchAlert - 2025 MLB Relievers Dashboard")
st.markdown("Live data view from FanGraphs export (updated manually)")

# Upload area
uploaded_file = st.file_uploader("Upload updated FanGraphs Excel file here", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ File uploaded and loaded successfully.")
else:
    # Default file (the current one from user)
    df = pd.read_excel("mlb relif pitchers.xlsx")

# Clean table display
df_display = df.drop(columns=["#", "vFA (pi)"], errors="ignore")  # drop index/velocity if cluttered
st.dataframe(df_display, use_container_width=True)

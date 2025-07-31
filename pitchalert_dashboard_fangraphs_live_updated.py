
import streamlit as st
import pandas as pd

# Load the Excel file (replace this with uploader if running live)
df = pd.read_excel("mlb relif pitchers.xlsx")

# Remove index column if it exists
if "#" in df.columns:
    df.drop(columns=["#"], inplace=True)

# Set up the app page
st.set_page_config(page_title="PitchAlert - 2025 MLB Relievers", layout="wide")
st.title("🎯 PitchAlert - 2025 MLB Relievers Dashboard")
st.markdown("Live data view from FanGraphs export (updated manually)")

# File uploader for updated data
uploaded_file = st.file_uploader("Upload updated FanGraphs Excel file here", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    if "#" in df.columns:
        df.drop(columns=["#"], inplace=True)

# Filter by team
teams = ["All"] + sorted(df["Team"].unique())
selected_team = st.selectbox("Filter by Team", options=teams)

if selected_team != "All":
    df = df[df["Team"] == selected_team]

# Toggle to track players
st.subheader("📣 Track Relievers for Alerts")
tracked = []

for i, row in df.iterrows():
    cols = st.columns([3, 3, 2, 1])
    cols[0].markdown(f"**{row['Name']}** - {row['Team']}")
    cols[1].markdown(f"ERA: {row['ERA']}, FIP: {row['FIP']}, WAR: {row['WAR']}")
    if cols[2].toggle(f"Track {row['Name']}", key=row['Name']):
        tracked.append(row['Name'])

if tracked:
    st.success("✅ You're tracking: " + ", ".join(tracked))
else:
    st.info("Toggle above to track relievers and receive alerts when warming up.")

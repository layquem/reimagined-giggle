
import streamlit as st
import pandas as pd

# Sample data
data = {
    "Player": [
        "Josh Hader", "Camilo Doval", "Emmanuel Clase", "Aroldis Chapman", "David Bednar",
        "Ryan Helsley", "Pete Fairbanks", "Alexis Diaz", "Tanner Scott", "Yennier Cano"
    ],
    "Team": [
        "HOU", "SF", "CLE", "PIT", "PIT",
        "STL", "TB", "CIN", "MIA", "BAL"
    ],
    "ERA": [2.31, 2.70, 1.98, 3.45, 2.22, 2.12, 3.01, 3.56, 2.67, 2.88],
    "WHIP": [1.02, 1.12, 0.95, 1.26, 1.10, 0.93, 1.20, 1.31, 1.08, 1.14],
    "K%": [38.2, 32.5, 35.4, 31.7, 30.2, 34.1, 28.5, 27.9, 29.8, 26.7],
    "BB%": [9.3, 10.1, 5.2, 12.8, 7.0, 6.4, 9.7, 11.2, 8.5, 7.9],
    "Last Used": ["Jul 28", "Jul 27", "Jul 28", "Jul 25", "Jul 26", "Jul 27", "Jul 28", "Jul 26", "Jul 28", "Jul 27"],
    "Pitches Thrown": [18, 12, 16, 24, 15, 10, 22, 19, 14, 17],
    "Projected Usage": ["High", "Medium", "High", "Rest", "Medium", "High", "Low", "Medium", "High", "Medium"]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="PitchAlert", layout="wide")
st.title("🎯 PitchAlert - Today's Top Relievers")
st.markdown("Live insights and projections for MLB bullpen arms")

selected_team = st.selectbox("Filter by Team", options=["All"] + sorted(df["Team"].unique().tolist()))

if selected_team != "All":
    df = df[df["Team"] == selected_team]

# Add alert tracking toggle
st.subheader("📣 Track Relievers for Alerts")
tracked = []

for idx, row in df.iterrows():
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.write(f"**{row['Player']}** - {row['Team']}")
    with col2:
        st.write(f"ERA: {row['ERA']}, WHIP: {row['WHIP']}")
    with col3:
        if st.toggle(f"Track {row['Player']}", key=row['Player']):
            tracked.append(row['Player'])

if tracked:
    st.success("✅ You're tracking: " + ", ".join(tracked))
else:
    st.info("Toggle above to track relievers and receive alerts when warming up.")

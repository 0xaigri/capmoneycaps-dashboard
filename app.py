import pandas as pd
import streamlit as st

st.set_page_config(page_title="CAPS Dashboard", layout="centered")
st.title("📈 Évolution quotidienne du total de CAPS")

df = pd.read_csv("caps_history.csv", names=["date", "total_caps"], parse_dates=["date"])

st.metric("Dernier total enregistré", f"{df['total_caps'].iloc[-1]:,}")

# Trie par date
df = df.sort_values("date")
df = df.set_index("date")

# 🔑 Forcer l’axe Y à commencer à 600 millions
st.line_chart(df["total_caps"], y_min=600_000_000)

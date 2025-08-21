import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="CAPS Dashboard", layout="centered")
st.title("📈 Daily evolution of total CAPS")

df = pd.read_csv("caps_history.csv", names=["date", "total_caps"], parse_dates=["date"]).sort_values("date")

st.metric("Last recorded total", f"{df['total_caps'].iloc[-1]:,}")

# Graphique Altair : axe Y démarre à 600M
y_min = 600_000_000
chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("total_caps:Q",
                title="Total CAPS",
                scale=alt.Scale(domain=[y_min, float(df["total_caps"].max())])),
        tooltip=[alt.Tooltip("date:T", title="Date"),
                 alt.Tooltip("total_caps:Q", title="Total CAPS", format="~s")]
    )
    .properties(width="container", height=400)
)

st.altair_chart(chart, use_container_width=True)

st.markdown("*Created by 0xaigri*", unsafe_allow_html=True)

import streamlit as st
from components import load_css

load_css()

st.title("🏆 Rewards")

st.metric(
    "Points",
    "1250"
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.success(
        "🥇 First Donation"
    )

with c2:
    st.success(
        "🌱 Eco Champion"
    )

with c3:
    st.success(
        "🍽 Food Saver"
    )

with c4:
    st.success(
        "🏅 10 Donations"
    )

st.progress(0.8)

st.write(
    "8 / 10 Donations"
)
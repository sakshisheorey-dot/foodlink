def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

import streamlit as st

st.title("🥇 Donor Leaderboard")

leaderboard = [
    ("ABC Restaurant", 1500),
    ("Fresh Mart", 1200),
    ("Hotel Paradise", 950),
    ("Food Junction", 700)
]

rank = 1

for donor, score in leaderboard:

    st.success(
        f"#{rank} {donor} — {score} points"
    )

    rank += 1
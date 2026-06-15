import streamlit as st
from components import load_css

load_css()

st.title("🏆 Community Leaderboard")

st.subheader("Top 3 Champions")

c1, c2, c3 = st.columns(3)

with c2:
    st.success("""
    🥇

    ABC Restaurant

    1500 Points
    """)

with c1:
    st.info("""
    🥈

    Fresh Mart

    1200 Points
    """)

with c3:
    st.warning("""
    🥉

    Hotel Paradise

    950 Points
    """)

st.divider()

st.subheader("Rankings")

rankings = [
    ("4", "Food Junction", 700),
    ("5", "Green Grocers", 550),
    ("6", "City Bakery", 480),
    ("7", "Royal Caterers", 430),
]

for rank, name, points in rankings:

    st.markdown(f"""
    <div class="ngo-card">
        <h4>#{rank} {name}</h4>
        <p>{points} Points</p>
    </div>
    """, unsafe_allow_html=True)
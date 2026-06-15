import streamlit as st
import pandas as pd
from database import get_leaderboard

if "user" not in st.session_state:
    st.stop()

st.title("🥇 FoodLink Leaderboard")

st.markdown(
    "### Top Contributors This Month"
)

st.divider()

# PODIUM

c1, c2, c3 = st.columns(3)

with c2:

    with st.container(border=True):

        st.markdown("# 🥇")
        st.subheader("Sarah")
        st.metric(
            "Points",
            "2450"
        )

with c1:

    with st.container(border=True):

        st.markdown("# 🥈")
        st.subheader("Rahul")
        st.metric(
            "Points",
            "2200"
        )

with c3:

    with st.container(border=True):

        st.markdown("# 🥉")
        st.subheader("Priya")
        st.metric(
            "Points",
            "2050"
        )

st.divider()

st.subheader(
    "Full Rankings"
)

from database import get_leaderboard

st.subheader("Full Rankings")

leaders = get_leaderboard()

rank_data = []

rank = 1

for name, points in leaders:

    rank_data.append({
        "Rank": rank,
        "Name": name,
        "Points": points
    })

    rank += 1

leaderboard_df = pd.DataFrame(rank_data)

st.dataframe(
    leaderboard_df,
    use_container_width=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "Top NGOs"
    )

    st.success(
        "Helping Hands"
    )

    st.success(
        "Care Foundation"
    )

    st.success(
        "Food For All"
    )

with col2:

    st.subheader(
        "Top Food Categories"
    )

    st.info(
        "Cooked Food"
    )

    st.info(
        "Vegetables"
    )

    st.info(
        "Bakery"
    )
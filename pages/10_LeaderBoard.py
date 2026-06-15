import streamlit as st
import pandas as pd

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

leaderboard = pd.DataFrame({

    "Rank":[1,2,3,4,5,6,7,8],
    "Name":[
        "Sarah",
        "Rahul",
        "Priya",
        "Ankit",
        "Sneha",
        "Aman",
        "Rohan",
        "Kiran"
    ],
    "Points":[
        2450,
        2200,
        2050,
        1800,
        1700,
        1600,
        1500,
        1400
    ]
})

st.dataframe(
    leaderboard,
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
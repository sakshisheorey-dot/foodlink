import streamlit as st

st.title("🏆 Rewards & Badges")

st.metric(
    "Current Points",
    "1,250"
)

st.progress(0.75)

st.caption(
    "750 / 1000 points for next badge"
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:

    with st.container(border=True):

        st.markdown("# 🥇")
        st.subheader(
            "First Donation"
        )

with col2:

    with st.container(border=True):

        st.markdown("# 🌱")
        st.subheader(
            "Food Saver"
        )

with col3:

    with st.container(border=True):

        st.markdown("# ♻️")
        st.subheader(
            "Eco Champion"
        )

with col4:

    with st.container(border=True):

        st.markdown("# 🏅")
        st.subheader(
            "10 Donations"
        )

st.divider()

st.subheader("How Rewards Work")

st.info("""
1. Donate food

2. NGO accepts request

3. Delivery completed

4. Earn points

5. Unlock badges

6. Climb leaderboard
""")
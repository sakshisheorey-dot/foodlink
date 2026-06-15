import streamlit as st

def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

from database import (
    get_user_rewards,
    get_badges
)

st.title("🏆 Rewards & Badges")

USER_ID = 1

reward_df = get_user_rewards(USER_ID)

points = 0

if not reward_df.empty:
    points = reward_df["points"].sum()

st.metric(
    "FoodLink Points",
    points
)

st.divider()

st.subheader("Badges Earned")

badges = get_badges(USER_ID)

if badges.empty:

    st.info(
        "No badges earned yet."
    )

else:

    cols = st.columns(4)

    for i, badge in enumerate(
        badges["badge_name"]
    ):

        with cols[i % 4]:

            st.success(
                f"🏅 {badge}"
            )

st.divider()

st.subheader(
    "Donation Progress"
)

goal = 10

donations_completed = 6

progress = (
    donations_completed / goal
)

st.progress(progress)

st.write(
    f"{donations_completed}/{goal} Donations"
)

st.divider()

st.subheader(
    "How FoodLink Works"
)

st.markdown("""
### LIST

Identify surplus food.

⬇️

### POST

Create food listing.

⬇️

### MATCH

NGOs discover food.

⬇️

### CLAIM

NGOs request donation.

⬇️

### COLLECT

Pickup and delivery.
""")
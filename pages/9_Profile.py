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
from database import (
    get_notifications
)

st.title("👤 Profile")

user_name = st.session_state.get(
    "name",
    "Demo User"
)

user_role = st.session_state.get(
    "role",
    "Donor"
)

st.subheader(user_name)

st.write(
    f"Role: {user_role}"
)

st.divider()

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Donations",
        12
    )

with c2:
    st.metric(
        "Food Saved",
        "520 kg"
    )

with c3:
    st.metric(
        "NGOs Helped",
        8
    )

st.divider()

menu = st.radio(
    "Navigation",
    [
        "My Donations",
        "Notifications",
        "Settings",
        "Help & Support",
        "About FoodLink"
    ]
)

if menu == "Notifications":

    st.subheader(
        "Notifications"
    )

    notifications = get_notifications(1)

    if notifications.empty:

        st.info(
            "No notifications."
        )

    else:

        for _, row in notifications.iterrows():

            st.info(
                row["message"]
            )

if menu == "About FoodLink":

    st.markdown("""
    ## FoodLink

    Connecting surplus food
    with those who need it most.

    Reduce waste.
    Increase impact.
    Strengthen communities.
    """)
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

import pandas as pd
from database import (
    get_all_donations,
    update_donation_status
)

st.set_page_config(layout="wide")

st.title("🚚 Track Donation")

df = get_all_donations()

if df.empty:

    st.info(
        "No donations available."
    )

    st.stop()

selected_id = st.selectbox(
    "Select Donation",
    df["id"]
)

donation = df[
    df["id"] == selected_id
].iloc[0]

status = donation["status"]

st.subheader(
    f"Donation #{selected_id}"
)

st.write(
    f"Category: {donation['category']}"
)

st.write(
    f"Quantity: {donation['quantity']} kg"
)

st.write(
    f"Location: {donation['location']}"
)

st.divider()

st.subheader("Progress")

steps = [
    "Posted",
    "Request Accepted",
    "Picked Up",
    "Delivered"
]

current_step = 0

if status in steps:
    current_step = steps.index(status)

progress = (
    current_step + 1
) / len(steps)

st.progress(progress)

for i, step in enumerate(steps):

    if i <= current_step:
        st.success(f"✅ {step}")
    else:
        st.info(f"⏳ {step}")

st.divider()

st.subheader("Update Status")

new_status = st.selectbox(
    "Status",
    steps
)

if st.button("Update"):

    update_donation_status(
        selected_id,
        new_status
    )

    st.success(
        "Status Updated"
    )

    st.rerun()

st.divider()

st.subheader("NGO Contact")

st.info("""
NGO: Helping Hands Foundation

Contact: +91 9876543210

Email:
helpinghands@email.com
""")
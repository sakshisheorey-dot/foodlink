import streamlit as st

if "user" not in st.session_state:
    st.stop()

st.title("🚚 Track Donation")

donation_id = st.text_input(
    "Donation ID"
)

st.divider()

stage = "Picked Up"

progress = {
    "Posted":25,
    "Accepted":50,
    "Picked Up":75,
    "Delivered":100
}

st.progress(
    progress[stage]
)

c1,c2,c3,c4 = st.columns(4)

c1.success("Posted")
c2.success("Accepted")
c3.success("Picked Up")
c4.info("Delivered")

st.divider()

st.subheader(
    "Donation Details"
)

left,right = st.columns(2)

with left:

    st.write(
        "**NGO:** Helping Hands"
    )

    st.write(
        "**Volunteer:** Rahul"
    )

    st.write(
        "**Pickup Time:** 2:30 PM"
    )

with right:

    st.write(
        "**Contact:** +91 XXXXX XXXXX"
    )

    st.write(
        "**Status:** Picked Up"
    )

    st.write(
        "**ETA:** 30 mins"
    )

st.divider()

timeline = [
    "Food Posted",
    "NGO Accepted Request",
    "Volunteer Assigned",
    "Food Picked Up",
    "On The Way",
    "Delivered"
]

for item in timeline:
    st.success(item)
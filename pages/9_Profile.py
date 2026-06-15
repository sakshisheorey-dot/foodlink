import streamlit as st
from components import load_css

load_css()

st.title("👤 Profile")

st.image(
    "https://via.placeholder.com/150",
    width=120
)

st.subheader(
    "Sakshi Sheorey"
)

st.write(
    "Donor"
)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Donations",
        15
    )

with c2:
    st.metric(
        "Food Saved",
        "520 kg"
    )

with c3:
    st.metric(
        "NGOs Helped",
        12
    )

st.divider()

st.button(
    "Notifications",
    use_container_width=True
)

st.button(
    "Settings",
    use_container_width=True
)

st.button(
    "Help & Support",
    use_container_width=True
)

st.button(
    "About FoodLink",
    use_container_width=True
)
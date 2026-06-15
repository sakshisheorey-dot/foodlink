import streamlit as st

if "user" not in st.session_state:
    st.stop()

st.title("👤 Profile")

col1, col2 = st.columns([1,2])

with col1:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
    )

    st.subheader("John Doe")

    st.caption("Food Donor")

with col2:

    st.subheader("Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Donations",
        "48"
    )

    c2.metric(
        "Food Saved",
        "1250 kg"
    )

    c3.metric(
        "NGOs Helped",
        "38"
    )

st.divider()

st.subheader("Recent Activity")

st.success(
    "40kg food delivered successfully"
)

st.success(
    "Earned Food Saver badge"
)

st.success(
    "New NGO connection established"
)

st.divider()

st.subheader("Account Settings")

st.button(
    "🔔 Notifications"
)

st.button(
    "⚙️ Settings"
)

st.button(
    "❓ Help & Support"
)

st.button(
    "ℹ️ About FoodLink"
)
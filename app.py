import streamlit as st
from auth import signup, login

st.set_page_config(
    page_title="FoodLink",
    page_icon="🍽️",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("""
# 🍽️ FoodLink

### Connecting surplus food with those who need it most
""")

col1,col2,col3 = st.columns([1,2,1])

with col2:

    tab1,tab2 = st.tabs(["Login","Sign Up"])

    with tab1:

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login(email,password)

            if user:

                st.session_state.logged_in = True
                st.session_state.user_id = user[0]
                st.session_state.name = user[1]
                st.session_state.role = user[4]

                st.success("Login Successful")

            else:
                st.error("Invalid Credentials")

    with tab2:

        name = st.text_input("Name")

        new_email = st.text_input("New Email")

        new_password = st.text_input(
            "New Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            ["Donor","NGO"]
        )

        if st.button("Create Account"):

            if signup(
                name,
                new_email,
                new_password,
                role
            ):
                st.success("Account Created")

            else:
                st.error("Email already exists")

st.divider()

st.metric("Food Saved","2,500 kg")
st.metric("Lives Impacted","8,200")
st.metric("NGOs Connected","120")
import streamlit as st
from PIL import Image

from database import init_db
from auth import register_user, login_user, logout


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="FoodLink",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# DATABASE INIT
# ---------------------------------------------------

init_db()

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------------------------------------------
# LOGO
# ---------------------------------------------------

def display_logo():

    try:
        st.image(
            "assets/logo.png",
            width=120
        )
    except:
        st.markdown("# 🍏 FoodLink")


# ---------------------------------------------------
# LANDING PAGE
# ---------------------------------------------------

def landing_page():

    col1, col2 = st.columns([1, 1])

    with col1:

        display_logo()

        st.title(
            "Connecting Surplus Food With Those Who Need It Most"
        )

        st.markdown("""
        ### Reduce Food Waste. Feed Communities.

        FoodLink helps restaurants, hotels,
        caterers and households donate
        surplus food to verified NGOs.

        ### Key Features

        ✅ Post Surplus Food

        ✅ Find Nearby NGOs

        ✅ Real-Time Tracking

        ✅ Impact Analytics

        ✅ Rewards & Recognition

        ✅ Volunteer Logistics

        """)

    with col2:

        st.image(
            "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c",
            use_container_width=True
        )

# ---------------------------------------------------
# LOGIN PAGE
# ---------------------------------------------------

def login_screen():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:
            st.success("Login Successful")
            st.rerun()

        else:
            st.error(
                "Invalid Credentials"
            )

# ---------------------------------------------------
# REGISTER PAGE
# ---------------------------------------------------

def register_screen():

    st.subheader("Create Account")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email Address"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Select Role",
        [
            "Donor",
            "NGO",
            "Admin"
        ]
    )

    if st.button(
            "Create Account"):

        success = register_user(
            name,
            email,
            password,
            role
        )

        if success:

            st.success(
                "Registration Successful"
            )

        else:

            st.error(
                "Email Already Exists"
            )

# ---------------------------------------------------
# AUTH SCREEN
# ---------------------------------------------------

def auth_page():

    st.markdown(
        "<h1 style='text-align:center;'>FoodLink</h1>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    with tab1:
        login_screen()

    with tab2:
        register_screen()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

def sidebar():

    with st.sidebar:

        display_logo()

        st.markdown("---")

        st.write(
            f"Welcome, "
            f"{st.session_state.user['name']}"
        )

        st.caption(
            st.session_state.user["role"]
        )

        st.markdown("---")

        st.page_link(
            "pages/1_Home.py",
            label="🏠 Dashboard"
        )

        st.page_link(
            "pages/2_Post_Food.py",
            label="🍱 Post Food"
        )

        st.page_link(
            "pages/3_Available_Surplus.py",
            label="🗺️ Available Surplus"
        )

        st.page_link(
            "pages/4_NGO_Requests.py",
            label="📥 NGO Requests"
        )

        st.page_link(
            "pages/5_Track_Donations.py",
            label="🚚 Tracking"
        )

        st.page_link(
            "pages/6_Impact_Dashboard.py",
            label="📈 Impact Dashboard"
        )

        st.page_link(
            "pages/7_Explore_NGOs.py",
            label="🏢 Explore NGOs"
        )

        st.page_link(
            "pages/8_Rewards.py",
            label="🏆 Rewards"
        )

        st.page_link(
            "pages/9_Profile.py",
            label="👤 Profile"
        )

        st.page_link(
            "pages/10_LeaderBoard.py",
            label="🥇 Leaderboard"
        )

        st.markdown("---")

        if st.button(
                "Logout"):

            logout()
            st.rerun()

# ---------------------------------------------------
# DASHBOARD HOME
# ---------------------------------------------------

def dashboard_home():

    st.title(
        "🌱 FoodLink Platform"
    )

    st.markdown(
        """
        Welcome to FoodLink,
        a smart food redistribution platform
        reducing food waste and feeding
        communities.
        """
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Food Saved",
        "360 kg",
        "+45 kg"
    )

    c2.metric(
        "NGOs Helped",
        "22",
        "+4"
    )

    c3.metric(
        "Lives Impacted",
        "720",
        "+56"
    )

    c4.metric(
        "Active Donations",
        "18",
        "+3"
    )

    st.markdown("---")

    left, right = st.columns(
        [2, 1]
    )

    with left:

        st.subheader(
            "Recent Activity"
        )

        st.info(
            "20kg food donated to Helping Hands NGO"
        )

        st.info(
            "15kg vegetables accepted by Care Foundation"
        )

        st.info(
            "40kg meals delivered successfully"
        )

    with right:

        st.subheader(
            "Quick Actions"
        )

        st.page_link(
            "pages/2_Post_Food.py",
            label="➕ Post Food"
        )

        st.page_link(
            "pages/3_Available_Surplus.py",
            label="🗺️ Browse Food"
        )

        st.page_link(
            "pages/6_Impact_Dashboard.py",
            label="📈 View Impact"
        )

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if st.session_state.user is None:

    landing_page()

    st.markdown("---")

    auth_page()

else:

    sidebar()

    dashboard_home()
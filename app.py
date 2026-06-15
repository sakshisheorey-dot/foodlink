import streamlit as st
from components import load_css

st.set_page_config(
    page_title="FoodLink",
    page_icon="🍏",
    layout="wide"
)

load_css()

left, right = st.columns([1,1])

with left:

    st.markdown("""
    # 🍏 FoodLink

    ## Connecting surplus food with those who need it most

    A digital platform that connects surplus food sources with NGOs for real-time redistribution and waste reduction.
    """)

    col1,col2 = st.columns(2)

    with col1:
        st.button(
            "Get Started",
            use_container_width=True
        )

    with col2:
        st.button(
            "I'm an NGO",
            use_container_width=True
        )

with right:

    # Replace with your image
    st.image(
        "assets/foodlink_hero.png",
        use_container_width=True
    )
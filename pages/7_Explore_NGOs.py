import streamlit as st
from components import load_css

load_css()

st.title("🏢 Explore NGOs")

search = st.text_input(
    "Search NGO"
)

for i in range(6):

    st.markdown("""
    <div class="ngo-card">
        <h4>Helping Hands</h4>
        <p>⭐ 4.8</p>
        <p>Child Nutrition</p>
        <p>Hyderabad</p>
    </div>
    """,
    unsafe_allow_html=True)

    st.button(
        "View Profile",
        key=i
    )
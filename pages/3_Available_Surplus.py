import streamlit as st
from components import load_css

load_css()

st.title("🗺 Available Surplus")

search = st.text_input(
    "Search Food"
)

filters = st.columns(4)

with filters[0]:
    st.selectbox(
        "Food Type",
        [
            "All",
            "Cooked Food",
            "Vegetables",
            "Bakery"
        ]
    )

with filters[1]:
    st.selectbox(
        "Distance",
        [
            "All",
            "<5 km",
            "<10 km"
        ]
    )

with filters[2]:
    st.selectbox(
        "Expiry",
        [
            "All",
            "Expiring Soon"
        ]
    )

with filters[3]:
    st.button(
        "Apply Filters"
    )

st.divider()

for i in range(5):

    st.markdown(f"""
    <div class="food-card">
        <h4>Fresh Bread</h4>
        <p>Quantity: 20kg</p>
        <p>Distance: 2 km</p>
        <p>Expires in 4 hours</p>
    </div>
    """,
    unsafe_allow_html=True)

    st.button(
        f"Claim Food {i}",
        use_container_width=True
    )
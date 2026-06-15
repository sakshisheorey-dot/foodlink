import streamlit as st
from components import load_css, section_title

load_css()

st.title("🍽 Post Surplus Food")

left,right = st.columns([2,1])

with left:

    section_title("Food Details")

    category = st.selectbox(
        "Category",
        [
            "Cooked Food",
            "Vegetables",
            "Fruits",
            "Bakery"
        ]
    )

    quantity = st.number_input(
        "Quantity (kg)",
        min_value=1
    )

    expiry = st.date_input(
        "Expiry Date"
    )

    location = st.text_input(
        "Pickup Location"
    )

    description = st.text_area(
        "Description"
    )

with right:

    section_title("Food Photo")

    image = st.file_uploader(
        "Upload Image"
    )

    if image:
        st.image(
            image,
            use_container_width=True
        )

st.divider()

section_title("Safety Checklist")

st.checkbox("Properly Packed")
st.checkbox("Fresh Condition")
st.checkbox("Within Expiry")
st.checkbox("Stored Hygienically")

if st.button(
    "Post Donation",
    use_container_width=True
):
    st.success(
        "Donation Posted Successfully"
    )
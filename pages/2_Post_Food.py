import streamlit as st
from database import add_donation
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("🍽 Post Surplus Food")

st.subheader("Food Information")

category = st.selectbox(
    "Food Category",
    [
        "Cooked Food",
        "Vegetables",
        "Fruits",
        "Bakery",
        "Packaged Food",
        "Beverages"
    ]
)

quantity = st.number_input(
    "Quantity (kg)",
    min_value=1,
    value=10
)

description = st.text_area(
    "Description"
)

expiry = st.datetime_input(
    "Expiry Date & Time"
)

location = st.text_input(
    "Pickup Location"
)

st.subheader("Food Safety Checklist")

safe = st.checkbox("Properly Packed")
fresh = st.checkbox("Fresh Condition")
expiry_ok = st.checkbox("Within Expiry")
clean = st.checkbox("Stored Hygienically")

uploaded_file = st.file_uploader(
    "Upload Food Photo",
    type=["png","jpg","jpeg"]
)

image_path = ""

if uploaded_file:

    os.makedirs("assets/food_images",
                exist_ok=True)

    image_path = f"assets/food_images/{uploaded_file.name}"

    with open(image_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file,width=350)

estimated_meals = quantity * 2

st.info(
    f"Estimated Meals Generated: {estimated_meals}"
)

if st.button("Post Food"):

    if not all([
        safe,
        fresh,
        expiry_ok,
        clean
    ]):

        st.error(
            "Complete all safety checks."
        )

    else:

        add_donation(
            donor_id=1,
            category=category,
            quantity=quantity,
            description=description,
            expiry=str(expiry),
            location=location,
            image_path=image_path
        )

        st.success(
            "Food Listing Created!"
        )
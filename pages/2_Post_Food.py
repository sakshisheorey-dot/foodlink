import streamlit as st
from database import create_food_post

st.title("🍱 Post Surplus Food")

with st.form("food_form"):

    c1, c2 = st.columns(2)

    with c1:

        food_type = st.selectbox(
            "Food Category",
            [
                "Cooked Food",
                "Raw Ingredients",
                "Bakery",
                "Fruits",
                "Vegetables"
            ]
        )

        quantity = st.number_input(
            "Quantity (kg)",
            min_value=1
        )

        expiry = st.datetime_input(
            "Expiry Time"
        )

    with c2:

        location = st.text_area(
            "Pickup Location"
        )

        image = st.file_uploader(
            "Food Image"
        )

    description = st.text_area(
        "Description"
    )

    submit = st.form_submit_button(
        "Post Donation"
    )

if submit:

    create_food_post(
        donor_id=1,
        food_type=food_type,
        quantity=quantity,
        description=description,
        expiry_time=str(expiry),
        location=location,
        image_path=""
    )

    st.success(
        "Food posted successfully!"
    )
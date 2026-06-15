import streamlit as st
import pandas as pd
from database import get_available_food

st.title("🗺️ Available Surplus Food")

c1, c2, c3 = st.columns(3)

with c1:
    st.selectbox(
        "Food Type",
        ["All","Cooked","Raw"]
    )

with c2:
    st.selectbox(
        "Distance",
        ["All","<5 km","<10 km"]
    )

with c3:
    st.selectbox(
        "Expiry",
        ["All","Within 2 hrs"]
    )

st.divider()

map_data = pd.DataFrame({
    "lat":[17.3850,17.3950,17.4200],
    "lon":[78.4867,78.4700,78.5000]
})

st.map(map_data)

st.divider()

food_data = get_available_food()

for food in food_data:

    with st.container(border=True):

        st.subheader(food[2])

        c1, c2 = st.columns(2)

        with c1:
            st.write(
                f"Quantity: {food[3]} kg"
            )

            st.write(
                f"Location: {food[6]}"
            )

        with c2:
            st.write(
                f"Expiry: {food[5]}"
            )

            st.write(
                f"Status: {food[8]}"
            )

        if st.button(
            f"Claim Food #{food[0]}"
        ):
            st.success(
                "Request sent successfully"
            )
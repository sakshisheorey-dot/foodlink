def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

import streamlit as st
import pandas as pd
from database import get_all_donations
from database import create_request

from streamlit_folium import st_folium
import folium

st.title("🗺 Available Surplus Food")

df = get_all_donations()

if df.empty:

    st.warning("No surplus food available.")

    st.stop()

tab1, tab2 = st.tabs(
    ["Map View","List View"]
)

# ------------------------------------------------
# MAP VIEW
# ------------------------------------------------

with tab1:

    m = folium.Map(
        location=[17.3850,78.4867],
        zoom_start=11
    )

    for _, row in df.iterrows():

        folium.Marker(
            [17.3850,78.4867],
            popup=f"""
            {row['category']}
            <br>
            {row['quantity']} kg
            """
        ).add_to(m)

    st_folium(
        m,
        width=1000,
        height=500
    )

# ------------------------------------------------
# LIST VIEW
# ------------------------------------------------

with tab2:

    filter_option = st.selectbox(
        "Filter",
        [
            "All",
            "Cooked Food",
            "Vegetables",
            "Fruits",
            "Bakery",
            "Packaged Food"
        ]
    )

    filtered_df = df

    if filter_option != "All":

        filtered_df = df[
            df["category"] == filter_option
        ]

    for _, row in filtered_df.iterrows():

        with st.container():

            col1,col2 = st.columns([3,1])

            with col1:

                st.subheader(
                    row["category"]
                )

                st.write(
                    row["description"]
                )

                st.write(
                    f"Quantity: {row['quantity']} kg"
                )

                st.write(
                    f"Location: {row['location']}"
                )

            with col2:

                if st.button(
                    f"Claim #{row['id']}"
                ):

                    create_request(
                        donation_id=row["id"],
                        ngo_id=1
                    )

                    st.success(
                        "Request Sent"
                    )

            st.divider()
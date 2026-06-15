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

from database import (
    get_ngos
)

st.set_page_config(
    layout="wide"
)

st.title("🏢 Explore NGOs")

ngos = get_ngos()

if ngos.empty:

    st.info("""
    No NGOs found.

    Add sample NGOs
    directly in database.
    """)

    st.stop()

search = st.text_input(
    "Search NGO"
)

cause_filter = st.selectbox(
    "Cause",
    [
        "All",
        "Child Nutrition",
        "Homeless Support",
        "Community Support",
        "Women Welfare"
    ]
)

filtered = ngos.copy()

if search:

    filtered = filtered[
        filtered["name"]
        .str.contains(
            search,
            case=False
        )
    ]

if cause_filter != "All":

    filtered = filtered[
        filtered["cause"]
        == cause_filter
    ]

st.write(
    f"{len(filtered)} NGOs Found"
)

for _, ngo in filtered.iterrows():

    with st.container():

        c1,c2 = st.columns(
            [4,1]
        )

        with c1:

            st.subheader(
                ngo["name"]
            )

            st.write(
                f"Cause: {ngo['cause']}"
            )

            st.write(
                f"Location: {ngo['location']}"
            )

            st.write(
                f"⭐ Rating: {ngo['rating']}"
            )

        with c2:

            st.button(
                "View Profile",
                key=ngo["id"]
            )

        st.divider()
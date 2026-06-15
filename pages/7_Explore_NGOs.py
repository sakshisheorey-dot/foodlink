import streamlit as st

if "user" not in st.session_state:
    st.stop()

st.title("🏢 Explore NGOs")

search = st.text_input(
    "Search NGO"
)

category = st.selectbox(
    "Cause",
    [
        "All",
        "Child Nutrition",
        "Homeless Support",
        "Community Welfare"
    ]
)

st.divider()

ngos = [

    {
        "name":"Helping Hands",
        "rating":"4.8",
        "cause":"Homeless Support",
        "distance":"2.5 km"
    },

    {
        "name":"Care Foundation",
        "rating":"4.7",
        "cause":"Child Nutrition",
        "distance":"4.2 km"
    },

    {
        "name":"Food For All",
        "rating":"4.9",
        "cause":"Community Welfare",
        "distance":"5.8 km"
    }

]

cols = st.columns(3)

for i, ngo in enumerate(ngos):

    with cols[i % 3]:

        with st.container(border=True):

            st.image(
                "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                width=100
            )

            st.subheader(
                ngo["name"]
            )

            st.write(
                f"⭐ {ngo['rating']}"
            )

            st.write(
                ngo["cause"]
            )

            st.write(
                ngo["distance"]
            )

            st.button(
                f"Connect - {ngo['name']}"
            )
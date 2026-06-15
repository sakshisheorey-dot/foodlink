import streamlit as st
from components import load_css

load_css()

st.title("📨 NGO Requests")

for i in range(5):

    st.markdown(f"""
    <div class="food-card">
        <h4>Helping Hands NGO</h4>
        <p>Requested: 20kg Cooked Food</p>
        <p>Distance: 2 km</p>
    </div>
    """,
    unsafe_allow_html=True)

    c1,c2 = st.columns(2)

    with c1:
        st.button(
            f"Accept {i}",
            use_container_width=True
        )

    with c2:
        st.button(
            f"Reject {i}",
            use_container_width=True
        )

    st.divider()
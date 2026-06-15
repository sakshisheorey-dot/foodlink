import streamlit as st

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def impact_card(value, label):
    st.markdown(f"""
    <div class="impact-card">
        <div class="metric-number">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def food_card(name, quantity, location, expiry):
    st.markdown(f"""
    <div class="food-card">
        <h4>{name}</h4>
        <p>Quantity: {quantity}</p>
        <p>Location: {location}</p>
        <p>Expires: {expiry}</p>
    </div>
    """, unsafe_allow_html=True)

def ngo_card(name, cause, rating):
    st.markdown(f"""
    <div class="ngo-card">
        <h4>{name}</h4>
        <p>{cause}</p>
        <p>⭐ {rating}</p>
    </div>
    """, unsafe_allow_html=True)
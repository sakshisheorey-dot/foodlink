import streamlit as st


def metric_card(title, value, delta=""):
    st.markdown(f"""
    <div class='metric-card'>
        <h4>{title}</h4>
        <h2>{value}</h2>
        <p>{delta}</p>
    </div>
    """, unsafe_allow_html=True)


def section_header(title):
    st.markdown(
        f"<h2>{title}</h2>",
        unsafe_allow_html=True
    )


def donation_card(
        title,
        quantity,
        location,
        status):

    st.markdown(f"""
    <div class='food-card'>
        <h4>{title}</h4>
        <p>Quantity: {quantity} kg</p>
        <p>Location: {location}</p>
        <p>Status: {status}</p>
    </div>
    """, unsafe_allow_html=True)


def badge_card(
        badge,
        description):

    st.markdown(f"""
    <div class='badge-card'>
        <h3>{badge}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


def leaderboard_card(
        rank,
        name,
        score):

    st.markdown(f"""
    <div class='leader-card'>
        <h3>#{rank}</h3>
        <h4>{name}</h4>
        <p>{score} pts</p>
    </div>
    """, unsafe_allow_html=True)
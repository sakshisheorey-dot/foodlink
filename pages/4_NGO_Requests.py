import streamlit as st

from turtle import st


def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

from database import get_requests
from database import get_connection

st.title("📨 NGO Requests")

requests_df = get_requests()

if requests_df.empty:

    st.info("No requests found.")

    st.stop()

incoming, history = st.tabs(
    ["Incoming Requests",
     "Past Requests"]
)

# -----------------------------------
# Incoming Requests
# -----------------------------------

with incoming:

    pending = requests_df[
        requests_df["status"] == "Pending"
    ]

    for _, row in pending.iterrows():

        st.subheader(
            f"Request #{row['id']}"
        )

        st.write(
            f"Donation ID: {row['donation_id']}"
        )

        col1,col2 = st.columns(2)

        with col1:

            if st.button(
                f"Accept {row['id']}"
            ):

                conn = get_connection()

                cursor = conn.cursor()

                cursor.execute("""
                UPDATE requests
                SET status='Accepted'
                WHERE id=?
                """,(row["id"],))

                conn.commit()
                conn.close()

                st.rerun()

        with col2:

            if st.button(
                f"Reject {row['id']}"
            ):

                conn = get_connection()

                cursor = conn.cursor()

                cursor.execute("""
                UPDATE requests
                SET status='Rejected'
                WHERE id=?
                """,(row["id"],))

                conn.commit()
                conn.close()

                st.rerun()

        st.divider()

# -----------------------------------
# History
# -----------------------------------

with history:

    history_df = requests_df[
        requests_df["status"] != "Pending"
    ]

    st.dataframe(
        history_df,
        use_container_width=True
    )
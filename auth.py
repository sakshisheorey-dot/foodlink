import bcrypt
import streamlit as st

from database import (
    create_user,
    get_user_by_email
)


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def register_user(name, email, password, role):

    existing = get_user_by_email(email)

    if existing:
        return False

    hashed = hash_password(password)

    create_user(
        name,
        email,
        hashed,
        role
    )

    return True


def login_user(email, password):

    user = get_user_by_email(email)

    if not user:
        return None

    if verify_password(password, user[3]):

        st.session_state.user = {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[4]
        }

        return user

    return None


def logout():
    st.session_state.clear()
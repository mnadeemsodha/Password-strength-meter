import streamlit as st
import re

# Password validation function
def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True

# Streamlit app
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    if is_strong_password(password):
        st.success("✅ Your password is strong!")
    else:
        st.error(
            "❌ Weak password. Make sure it has:\n"
            "- At least 8 characters\n"
            "- Upper & lowercase letters\n"
            "- At least one number\n"
            "- One special character (!@#$%^&*)"
        )

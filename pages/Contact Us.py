import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="my_form"):
    user_email = st.text_input("Enter your email")
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    submit = st.form_submit_button(label="Submit")

    if submit:
        send_email(message)
        st.success("Your message has been submitted")

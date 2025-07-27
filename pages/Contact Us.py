import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="my_form"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Enter your message")
    message = message + "\n" + user_email
    submit = st.form_submit_button(label="Submit")

    if submit:
        send_email(message)
        st.success("Your message has been submitted")

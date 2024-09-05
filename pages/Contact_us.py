import streamlit as st
from send_email import send_email

st.header("contact Me")

with st.form(key='contact_form'):
    user_email = st.text_input("yuor email address")
    message = st.text_area("your message")
    message=user_email+"\n"+message
    button = st.form_submit_button("Submit")
    if button:
       send_email(message)




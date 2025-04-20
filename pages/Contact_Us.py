
import  streamlit as st
from Emailing import email

st.header("Contact Me")

with st.form(key = "contact_form"):
    user_email = st.text_input("E-mail address ")
    raw_message = st.text_area("Enter Message")
    message = f"""
        Subject = A new Email from {user_email}  
         
        From = {user_email}
        {raw_message} 
    """
    button =st.form_submit_button("Submit")

if button:
    email(message)
    st.write("Your Email has been sent Successfully")
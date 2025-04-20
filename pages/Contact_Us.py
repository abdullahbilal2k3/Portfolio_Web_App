import  streamlit as st

st.header("Contact Me")

with st.form(key = "contact_form"):
    user_email = st.text_input("E-mail address ")
    message = st.text_area("Enter Message")
    button =st.form_submit_button("Submit")

if button:
    print("I am pressed")
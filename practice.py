import streamlit as st
import os

# Page configuration
st.set_page_config(layout="wide")

# Check if image exists
image_path = "My_Portfolio\AbdullahBilalprofile.jpg"

# Two column layout
col1, col2 = st.columns(2)

with col1:
    if os.path.exists(image_path):
        st.image(image_path, width= 400 )
    else:
        st.warning(f"Image file not found: {image_path}")

with col2:
    st.title("Abdullah Bilal")

    content1 = """
    As a passionate Computer Science student with hands-on experience in software development, UI/UX design, and web technologies, 
    I am eager to apply my skills in a professional setting. I have actively built projects and contributed to teams, showcasing my 
    ability to learn quickly, adapt to new technologies, and solve problems effectively. With a strong foundation in programming and a 
    genuine interest in innovation, I aim to gain real-world experience and grow within dynamic and collaborative environments.
    """
    st.info(content1)

    content2 = "Below is some of my applications and other work you may visit."
    st.write(content2)

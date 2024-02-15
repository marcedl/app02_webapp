import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width= 300)

with col2:
    st.title("Marcela DL")
    content = """  
    Hi! I am Marcela DL, Python programer, PhD, and Quality Manager. I am love to learn, and want to create a new 
    journey to programing, web creation and automation. 
    """
    st.write(content)

content2 = """
Below you can find some Python apps I had built. Feel free to take a look!
"""
st.write(content2)
import streamlit as st

st.set_page_config(layout="wide")

col1, col2  = st.columns(2)

with col1:
    st.image('images/photo.jpg',width=350)

with col2:
    st.title('Kartikey Goel')
    content = """
    Hi, I am Kartikey Goel and I love to code in python and Javascript.
    I also love to listen to music
    """
    st.info(content)
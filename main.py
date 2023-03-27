import streamlit as st
import pandas

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

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv',sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")


import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("hosein enayat")
    content="""
    for e in 
        Hi,I am hosein! I am a python programmer
        teacher and CEO of Farrigram social media,
        I graduated in 2022 from software engineer,
        """
    st.success(content)

content2="""
Below you can find some of apps I have built in python:
Feel free to contact me !
"""
st.write(content2)

col3, col4 = st.columns(2)
df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code] ({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code] ({row['url']})")



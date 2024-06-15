import streamlit as st

with st.popover("open popover"):
    st.markdown("hello world")
    name = st.text_input("What's your name")

st.write("your name :",name)    
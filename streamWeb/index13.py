import streamlit as st

if "lynn" not in st.session_state:
    st.session_state['lynn'] = 30

st.session_state["lynn"]    
st.session_state.lynn = 50
st.session_state.lynn
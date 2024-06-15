import streamlit as st
import time

placehoder = st.empty()

with placehoder:
    for s in range(5):
        st.write(f"{s} seconds have passed")
        time.sleep(1)

    st.write("1 minute over!")    

time.sleep(2)

placehoder.empty()
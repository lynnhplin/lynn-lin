import streamlit as st


# with notation 
with st.sidebar:
    with st.form("abc"):
        selected_value = st.selectbox(
        "How would you like to be contacted?",    
        ("Email","Home phone","Mobile phone")
            )
        radio_vale = st.radio(
            "Choose a shipping method",
            ("Standard(5-15 days)","express(2-3 days)")
            )
        
        st.form_submit_button("礭定")

st.write(selected_value,radio_vale)




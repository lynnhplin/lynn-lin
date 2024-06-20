import streamlit as st

st.title(" BMI值計算")
st.divider()
st.markdown('''
BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)

例如：一個52公斤的人，身高是155公分，則BMI為 :

52(公斤)/1.552 ( 公尺2 )= 21.6

體重正常範圍為  BMI=18.5～24
''')
st.divider()
col1,col2,col3 = st.columns([1,1,1])
                        

with col1:
    st.header("         ") 
    st.subheader("體重過輕")
    st.subheader("正常範圍")                       
    st.subheader("異常範圍")   

with col2:
    st.header("BMI-kg/m2") 
    st.subheader("BMI ＜ 18.5")
    st.subheader("18.5≦BMI＜24")   
    st.subheader("　　過重：24≦BMI＜27,輕度肥胖：27≦BMI＜30,中度肥胖：30≦BMI＜35,重度肥胖：BMI≧35")   

with col3:
    st.header("腰圍(cm)") 
    st.subheader("-")
    st.subheader("-")          
    st.subheader("男性：≧90公分,女性：≧80公分")    





with st.form("my form"):
 
    name = st.text_input("姓名:")
    height = st.number_input("身高:")
    weight = st.number_input("體重:")

    submitted = st.form_submit_button("Submit")
    if submitted:
       bmi = weight / ((height / 100) ** 2)   
       st.write("姓名 :",name,"身高 :",height,"體重 :",weight,"BMI -->", round(bmi,2))    
   




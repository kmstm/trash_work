from dotenv import load_dotenv 
load_dotenv() 

from langchain_openai import ChatOpenAI 
chat_model = ChatOpenAI()   

import streamlit as st

st.title("시 생성기")
subject = st.text_input("시의 주제를 입력하세요:")
st.write("주제:", subject)

if st.button("시 생성하기"):
    with st.spinner("시를 생성하는 중..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘.") 
        st.write("생성된 시:")


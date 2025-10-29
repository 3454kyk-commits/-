import streamlit as st
st.title('안녕하세요')
st.subheader('아앙아앙')
st.write('히히히히히')
st.write('https://naver.com')
st.link_button('네이버 바로가기','https://naver.com')

name= st.text_input('이름을 알려주세요!:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요')
    st.balloons
    st.image('')

import streamlit as st
st.title('안녕하세요')
st.subheader('환영합니다!')
st.write('welcom')
st.write('https://naver.com')
st.link_button('네이버 바로가기','https://naver.com')

name= st.text_input('이름을 알려주세요!:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요')
    st.balloons()
    st.image('https://www.chosun.com/resizer/v2/GGMF7OCIKAJ26C5SGJ23XZVOJU.jpg?auth=697d9fa0a5923b1d8c14816aa85807bfa0e3fd6a2b071acbe5a5c8ff60a064b3&width=616')

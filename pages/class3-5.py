import random
import streamlit as st
st.title("猜數字遊戲")
if "answer" not in st.session_state:
    st.session_state.text = ""
    st.session_state.answer = random.randrange(1,101)
    st.session_state.min = 1
    st.session_state.max = 100
    st.session_state.win = False
st.session_state.num = int(st.number_input(f"請輸入{st.session_state.min}到{st.session_state.max}的整數:", min_value=st.session_state.min, max_value=st.session_state.max, step=1, key=f"game1"))
if st.button("猜!",key=f"btn")and st.session_state.win == False: 
    if st.session_state.num > st.session_state.answer:
        st.session_state.text = ("太大了!")
        st.session_state.max = st.session_state.num
    elif st.session_state.num < st.session_state.answer:
        st.session_state.text = ("太小了!")
        st.session_state.min = st.session_state.num
    else: 
        st.session_state.text = ("答對了!")
        st.session_state.win = True

    st.rerun()
st.write(st.session_state.text)
    

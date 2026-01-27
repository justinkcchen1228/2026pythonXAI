import streamlit as st
st.title("數字金字塔")
number=st.number_input("請輸入一個整數(1到9)",min_value=1,max_value=9,step=1,key="數字金字塔")
for i in range(1, number+1):
    st.write(str(i)*i)
st.markdown("---")
st.title("箭頭金字塔")
number1=int(st.number_input("請輸入一個整數(1到9)",min_value=1,max_value=9,step=1,key="箭頭金字塔"))
for i in range (1, number1+5):
    if i<number1+1:
        st.write(" "*int(((number1-i)/2))+"a"*i+" "*int(((number1-i)/2)))
    else:
        st.write(" "*int(((number1-1)/2))+"a"+" "*int(((number1-1)/2)))
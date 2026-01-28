import streamlit as st
st.title("數字金字塔")
number=st.number_input("請輸入一個整數(1到9)",min_value=1,max_value=9,step=1,key="數字金字塔")
st.write("數字金字塔:")
for i in range(1, number+1):
    st.write(str(i)*i)
st.markdown("---")
st.title("箭頭金字塔")
number1=int(st.number_input("請輸入箭頭的層數",min_value=2,step=1,key="箭頭金字塔"))
a=""
for i in range(1, number1 + 1):
    a=a+(" " * (number1 - i) + "*"*(2 * i - 1)+"\n")

for i in range(number1):
    a=a+(" " * (number1 - 1) + "*"+ "\n")
st.markdown(f"```\n箭頭金字塔:\n{a}```")

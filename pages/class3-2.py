import streamlit as st
if st.button("重新整理", key="btn1"):
    st.rerun()

st.title("點餐機")

# 建立購物籃（只在第一次建立）
if "cart" not in st.session_state:
    st.session_state.cart = []
col1, col2 = st.columns(2)

# ===== 輸入餐點 =====
food = col1.text_input("請輸入餐點")

if col2.button("加入"):
    if food != "":
        st.session_state.cart.append(food)
st.markdown("### 購物籃")

# ===== 顯示購物籃內容 =====
for i in range(len(st.session_state.cart)):
        col1, col2 = st.columns([1, 1])
        col1.write(st.session_state.cart[i])
        if col2.button("刪除", key=f"del{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

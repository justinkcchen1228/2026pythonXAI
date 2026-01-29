import streamlit as st
import os

# =====================
# 標題
# =====================
st.title("購物平台")  # 網頁標題

# =====================
# 商品資料初始化
# =====================
if "products" not in st.session_state:
    st.session_state.products = {
        "apple":  {"price": 10, "stock": 10, "image": "image/apple.png"},
        "banana": {"price": 10, "stock": 10, "image": "image/banana.png"},
        "orange": {"price": 10, "stock": 10, "image": "image/orange.png"},
        "bg":     {"price": 10, "stock": 10, "image": "image/bg.png"},
    }

products = st.session_state.products  # 方便使用

# =====================
# 欄位數設定
# =====================
cols_num = st.number_input(
    "請輸入欄位數",
    min_value=1,
    max_value=5,
    step=1,
    value=2
)

# =====================
# 商品顯示區（順序固定）
# =====================
product_names = ["apple", "banana", "bg", "orange"]  # 固定順序
cols = st.columns(cols_num)

for i in range(len(product_names)):
    product = product_names[i]
    col = cols[i % cols_num]

    # 顯示商品圖片
    col.image(products[product]["image"], width=150)

    # 商品名稱改成第四級標題（####）
    col.markdown(f"#### {product}")

    # 顯示價格和庫存
    col.write(f"價格：{products[product]['price']} 元")
    col.write(f"庫存：{products[product]['stock']} 件")

    # 購買按鈕
    if col.button(f"購買 {product}", key=f"buy_{product}"):
        if products[product]["stock"] > 0:  # 庫存大於0才可以購買
            products[product]["stock"] -= 1  # 庫存扣1
            st.success("購買成功")           # 顯示購買成功訊息
        # 庫存不足不顯示任何訊息

# =====================
# 新增商品庫存區
# =====================
col1, col2 = st.columns(2)

with col1:
    select_product = st.selectbox(
        "選擇商品",
        product_names
    )

with col2:
    add_stock = st.number_input(
        "新增庫存數量",
        min_value=1,
        step=1,
        value=1
    )

if st.button("新增庫存"):
    products[select_product]["stock"] += add_stock  # 新增庫存

# =====================
# 顯示目前商品庫存
# =====================
st.write("目前商品庫存:")

for product in product_names:
    st.write(f"{product}：{products[product]['stock']} 件")

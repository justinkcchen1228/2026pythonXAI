
---

# 🐍 Python & Streamlit 筆記

---

## 一、箭頭金字塔（字串 + for 迴圈）

### 功能說明

👉 讓使用者輸入層數
👉 用 `*` 組成「箭頭形狀的金字塔」
👉 最後一次顯示出來

### 核心概念

* **字串可以相加**
* **字串可以乘數字**
* 用 `\n` 來換行

### 重點程式概念

```python
a = ""
a = a + "內容" + "\n"
```

### 金字塔邏輯

* 上半部：一層一層變寬
* 下半部：固定中間一條直線

📌 `(" " * (number - i))`
→ 用空白控制對齊位置

📌 `("*" * (2*i - 1))`
→ 控制星星數量

---

## 二、List（串列）是什麼？

### 1️⃣ List 就是一個「裝很多東西的盒子」

```python
[]
[1, 2, 3]
[1, "a", True]
```

👉 List 裡可以放：

* 數字
* 文字
* 布林值
* 甚至另一個 list

---

### 2️⃣ 用 index 讀取資料（從 0 開始）

```python
L = [1, 2, 3, "a"]
print(L[0])  # 1
print(L[3])  # a
```

📌 第一個元素是 `index 0`，不是 1！

---

### 3️⃣ List 切片（跟 range 很像）

```python
L = [1, 2, 3, "a", "b", "c"]

L[::2]      # 每隔一個取一次
L[1:4]      # 從 index 1 到 3
L[1:4:2]    # 從 index 1 到 3，每次跳 2
```

---

### 4️⃣ List 長度（有幾個元素）

```python
len(L)
```

📌 是「元素數量」，不是 index 最大值

---

## 三、走訪 List（for 迴圈）

### 方法一：用 index（適合需要位置）

```python
for i in range(len(L)):
    print(L[i])
```

### 方法二：直接取元素（最常用）

```python
for item in L:
    print(item)
```

---

## 四、Call by Value vs Call by Reference（超重要❗）

### 1️⃣ 數字：Call by Value（複製）

```python
a = 1
b = a
b = 2
```

👉 a 不會被改到

---

### 2️⃣ List：Call by Reference（共用）

```python
a = [1, 2, 3]
b = a
b[0] = 2
```

👉 a 也會被改！

---

### 3️⃣ 正確複製 List

```python
b = a.copy()
```

👉 a 跟 b 互不影響 👍

---

## 五、List 常用功能

### 1️⃣ 加資料：append

```python
L.append(4)
```

---

### 2️⃣ 刪資料：remove（刪內容）

```python
L.remove("a")
```

📌 只會刪「第一個」找到的

---

### 3️⃣ 刪資料：pop（刪位置）

```python
L.pop(0)  # 刪 index 0
L.pop()   # 刪最後一個
```

---

### 4️⃣ 排序：sort

```python
L.sort()
```

📌 會直接改原本的 list

---

## 六、檔案讀取（open）

### 常見模式

| 模式 | 說明 |
| -- | -- |
| r  | 讀取 |
| w  | 寫入 |
| a  | 附加 |

### 讀檔範例

```python
f = open("檔名.py", "r", encoding="utf-8")
content = f.read()
f.close()
```

📌 用完一定要 `close()`

---

## 七、多個 List 一起用（成績計算）

```python
midterm = [80, 95, 78]
final = [64, 73, 52]

平均 = (midterm[1] + final[1]) / 2
```

👉 用 index 對應同一個人

---

## 八、Streamlit：Columns（欄位排版）

### 1️⃣ 基本 columns

```python
col1, col2 = st.columns(2)
```

---

### 2️⃣ 不同寬度比例

```python
st.columns([1, 2])
```

👉 col2 比 col1 寬

---

### 3️⃣ with 語法（超重要）

```python
with col1:
    st.button("按鈕")
    st.write("文字")
```

📌 with 的意思是：
👉「接下來的東西，全部放在這個欄位裡」

---

### 4️⃣ 用 for 建立很多欄位

```python
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

---

## 九、文字輸入（text_input）

```python
text = st.text_input("請輸入文字", value="預設文字")
```

👉 使用者輸入的文字會存進 `text`

---

## 十、session_state（記住資料）

### 為什麼要用？

👉 Streamlit 每按一次按鈕
👉 程式就會「重新跑一次」
👉 一般變數會歸零 ❌

---

### 正確記住資料的方法

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1
```

---

### 按鈕加 1 範例

```python
if st.button("加1"):
    st.session_state.ans += 1
```

---

### 強制重新整理畫面

```python
st.rerun()
```

---

## 十一、點餐機（綜合應用🔥）

### 功能

* 輸入餐點
* 加入購物籃
* 顯示清單
* 可以刪除
* 用 session_state 記住資料

### 核心概念

✅ list
✅ session_state
✅ columns
✅ for 迴圈
✅ pop + rerun

---


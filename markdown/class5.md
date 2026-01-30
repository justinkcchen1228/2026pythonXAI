

---

## 全域變數與區域變數

* **全域變數**：寫在函式外面，整個程式都可以用
* **區域變數**：寫在函式裡面，只能在該函式內使用

```python
length = 5  # 全域變數

def calculate_square_area():
    area = length ** 2  # area 是區域變數
    print("面積是", area)
```

* 函式裡可以「使用」全域變數
* 但**不能直接修改全域變數**

```python
# 這樣會出錯
# length = length + 1
```

---

## 函式什麼時候才會執行

* **函式定義時不會執行**
* **一定要呼叫才會執行**

```python
length = 10
calculate_square_area()  # 面積是 100
```

👉 面積是在「呼叫函式那一刻」才計算的

---

## 區域變數不會影響全域變數

```python
length = 5
area = 100

def calculate_square_area():
    area = length ** 2  # 這是區域變數

calculate_square_area()
print(area)  # 100
```

* 函式內的 `area` 是區域變數
* 不會改到外面的 `area`

---

## 用 return 回傳結果（推薦寫法）

```python
def calculate_square_area() -> int:
    area = length ** 2
    return area

area = calculate_square_area()
print(area)  # 25
```

* 用 `return` 把結果交給外面
* 程式比較安全、好維護 👍

---

## 使用 global 修改全域變數（不常用）

```python
def calculate_square_area():
    global area
    area = length ** 2
```

* `global area` 代表「我要用外面的 area」
* 函式內可以直接改全域變數
* ⚠️ 新手不建議常用，容易看不懂程式流程

---

## 函數參數都是區域變數

```python
def hello(name: str):
    print(f"Hello, {name}!")
```

* `name` 只存在於函式裡
* 函式外面用不到

---

## 函數說明文件（docstring）

```python
def hello(name: str):
    """
    這是一個打招呼的函數
    參數:
    name: str - 姓名
    """
```

* 用三個雙引號 `""" """`
* 用來說明函式用途、參數、回傳值

---

## 使用 OpenAI API（基本流程）

### 載入套件與金鑰

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")
```

* `.env` 檔用來放 API 金鑰
* 不要直接寫在程式碼裡

---

### 終端機聊天範例（while）

```python
while True:
    user_input = input("你:")
    if user_input == "exit":
        break
```

* `while True` 代表一直執行
* `break` 用來跳出迴圈

---

## Streamlit 聊天介面基礎

### 顯示聊天泡泡

```python
st.chat_message("user").write("使用者訊息")
st.chat_message("assistant").write("AI 回應")
```

---

### 使用 session_state 存聊天紀錄

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

* `session_state` 可以記住資料
* 頁面重新整理資料不會消失

---

### 顯示聊天紀錄

```python
for message in st.session_state.history:
    st.chat_message(message["role"]).write(message["content"])
```

---

## Streamlit 版 AI 聊天機器人流程

1. 使用者輸入訊息
2. 存入 `session_state.history`
3. 呼叫 OpenAI API
4. 把 AI 回應存回 history
5. `st.rerun()` 重新整理畫面

---

## Streamlit 特效元件

```python
with st.spinner("處理中..."):
    time.sleep(3)

st.success("完成啦!")
```

* `spinner`：顯示載入中
* `success`：顯示成功訊息

---

## AI 圖像生成（Image API）

* 使用 `openai.images.generate`
* 可設定：

  * 圖片尺寸
  * 品質
  * 背景是否透明
* 回傳的是 **base64 圖片資料**
* 要先解碼才能顯示或下載

---

### 一句總結 🌟

* **區域變數只活在函式裡**
* **全域變數整個程式都能用**
* **推薦用 return，不要亂用 global**
* **Streamlit + session_state 可以做聊天系統**
* **API 金鑰一定要保護好**



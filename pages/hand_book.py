import streamlit as st
with st.expander("Class1 課堂筆記"):
    st.write(
        """
---

# 🐍 Python 基礎筆記（國二適用）

---

## 一、註解（給人看的說明）

👉 **註解不會被電腦執行，只是提醒人用的**

### 單行註解

```python
# 這是單行註解
```

### 多行註解

```python
'''
這是多行註解
'''
```

📌 小技巧：
**Ctrl + ?** 可以快速註解或取消註解

---

## 二、print()：顯示內容

`print()` 是用來**把文字或數字顯示在畫面上**的指令。

```python
print("Hello World")
print(123)
```

---

## 三、Python 的基本資料型態

| 型態    | 名稱  | 說明              |
| ----- | --- | --------------- |
| int   | 整數  | 沒有小數點的數字        |
| float | 浮點數 | 有小數點的數字         |
| str   | 字串  | 文字              |
| bool  | 布林值 | 只有 True 或 False |

範例：

```python
print(1)
print(1.23)
print("apple")
print(True)
print(False)
```

---

## 四、變數（裝資料的盒子）

👉 變數就像一個**有名字的盒子**，可以存東西

```python
a = 10
print(a)

a = "apple"
print(a)
```

📌 `=` 的意思是：
**把右邊的東西，存到左邊的變數裡**

---

## 五、運算子（數學運算）

| 符號 | 功能  |
| -- | --- |
| +  | 加法  |
| -  | 減法  |
| *  | 乘法  |
| /  | 除法  |
| // | 取商  |
| %  | 取餘數 |
| ** | 次方  |

```python
print(1 + 1)
print(5 // 2)
print(2 ** 3)
```

### 運算優先順序（很重要）

1️⃣ ()
2️⃣ **
3️⃣ * / // %
4️⃣ + -

---

## 六、字串運算（文字也能算）

```python
print("apple" + "pen")   # 合併文字
print("apple" * 3)       # 重複文字
```

---

## 七、字串格式化（f-string）

👉 可以把變數放進句子裡

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")
```

📌 `{}` 裡面可以放變數

---

## 八、常用函式

### len()：算長度

```python
print(len("apple"))
```

### type()：看資料型態

```python
print(type(1))
print(type("apple"))
```

---

## 九、型態轉換（資料變身）

```python
int(1.0)        # 變整數
float(1)        # 變小數
str(123)        # 變文字
bool(1)         # 變 True
```

⚠️ 注意：

```python
# int("hello")  # 會錯，因為不是數字
```

---

## 十、input()：讓使用者輸入資料

```python
a = input("請輸入一些文字:")
print(a)
print(type(a))
```

📌 **input() 輸入進來的一定是字串！**
要算數學一定要先轉型態。

```python
print(int(a) + 10)
```

---

## 十一、練習題整理

### 🟢 計算圓面積

```python
r = int(input("請輸入半徑:"))
pi = 3.14
area = pi * r ** 2
print(area)
```

---

### 🟢 計算平均成績

```python
a1 = int(input("請輸入國文期中成績"))
a2 = int(input("請輸入國文期末成績"))
print("平均:", (a1 + a2) / 2)
```

---

### 🟢 BMI 計算器

```python
height = float(input("請輸入身高(cm):")) / 100
weight = float(input("請輸入體重(kg):"))
bmi = weight / (height ** 2)
print("你的BMI為:", bmi)
```

---

## 十二、Streamlit（用 Python 做網頁）

👉 Streamlit 可以把 Python 變成簡單的網頁畫面

```python
import streamlit as st
```

### 常用指令

| 指令            | 功能           |
| ------------- | ------------ |
| st.title()    | 標題           |
| st.write()    | 幾乎什麼都能顯示     |
| st.text()     | 純文字          |
| st.markdown() | 可以用 Markdown |

範例：

```python
st.title("這是標題")
st.text("純文字")
st.markdown("**粗體文字**")
```
---
"""
    )
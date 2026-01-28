
---

# 🐍 Python 筆記

## 一、註解（給人看的說明文字）

註解是**寫給人看的**，電腦會直接忽略，不會執行。

### 1️⃣ 單行註解

```python
# 這是單行註解
```

### 2️⃣ 多行註解

```python
'''
這是多行註解
'''
```

📌 小技巧：
`Ctrl + ?` 可以快速**註解 / 取消註解**

---

## 二、print()：顯示文字或數值

`print()` 用來把內容顯示在畫面（終端機）上。

```python
print("Hello World")
print(123)
```

---

## 三、Python 的基本資料型態

| 型態    | 名稱  | 說明    | 範例           |
| ----- | --- | ----- | ------------ |
| int   | 整數  | 沒有小數點 | 1, -3, 0     |
| float | 浮點數 | 有小數點  | 1.5, 3.14    |
| str   | 字串  | 文字    | "apple"      |
| bool  | 布林值 | 只有對或錯 | True / False |

```python
print(1)
print(1.23)
print("apple")
print(True)
```

---

## 四、變數（用來存資料的盒子）

變數就像一個**有名字的盒子**，可以存東西。

```python
a = 10
print(a)

a = "apple"
print(a)
```

📌 `=` 不是數學的等於
👉 是「**把右邊的東西存到左邊**」

---

## 五、運算子（數學運算）

| 運算 | 符號       | 說明 |
| -- | -------- | -- |
| +  | 加法       |    |
| -  | 減法       |    |
| *  | 乘法       |    |
| /  | 除法       |    |
| // | 取商（不含小數） |    |
| %  | 取餘數      |    |
| ** | 次方       |    |

```python
print(2 + 3)
print(5 // 2)
print(2 ** 3)
```

### ✨ 運算優先順序（很重要）

1️⃣ ()
2️⃣ **
3️⃣ * / // %
4️⃣ + -

---

## 六、字串運算（文字也能算）

```python
print("apple" + "pen")   # 合併文字
print("hi" * 3)          # 重複文字
```

---

## 七、字串格式化（f-string）

可以把變數「放進文字裡」。

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")
```

📌 `{}` 裡面可以放變數

---

## 八、常用函式

### 1️⃣ len()：算長度

```python
print(len("apple"))  # 5
```

### 2️⃣ type()：看資料型態

```python
print(type(1))
print(type("apple"))
```

---

## 九、型態轉換（資料變身）

```python
int(1.9)        # 變整數
float(1)        # 變小數
str(123)        # 變文字
bool(1)         # 變 True
```

⚠️ 注意：

```python
# int("hello")  # ❌ 會錯，因為不是數字
```

---

## 十、input()：讓使用者輸入資料

```python
a = input("請輸入一些文字:")
print(a)
print(type(a))
```

📌 **input() 得到的一定是字串！**
要算數學一定要轉型態。

```python
print(int(a) + 10)
```

---

## 十一、練習題整理

### 🟢 圓面積

```python
r = int(input("請輸入半徑:"))
pi = 3.14
area = pi * r ** 2
print(area)
```

---

### 🟢 平均成績

```python
a1 = int(input("期中成績:"))
a2 = int(input("期末成績:"))
print((a1 + a2) / 2)
```

---

### 🟢 BMI 計算器

```python
height = float(input("身高(cm):")) / 100
weight = float(input("體重(kg):"))
bmi = weight / (height ** 2)
print(bmi)
```

---

## 十二、Streamlit（做簡單網頁）

Streamlit 可以把 Python 程式變成**網頁畫面**。

```python
import streamlit as st
```

### 常用指令

| 指令            | 功能          |
| ------------- | ----------- |
| st.title()    | 標題          |
| st.write()    | 什麼都能顯示      |
| st.text()     | 純文字         |
| st.markdown() | 支援 Markdown |

```python
st.title("這是標題")
st.text("純文字")
st.markdown("**粗體**")
```

---

## ✅ 重點快速記憶

✔ input() → 一定是字串
✔ 算數前要 int / float
✔ print() 用來顯示
✔ 變數像盒子
✔ f-string 很好用

---


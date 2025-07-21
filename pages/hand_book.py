import streamlit as st

st.write(
    """
---

# 🐍 Python 初學筆記：第一堂課

## 💬 註解是什麼？

註解是寫給「人」看的，不會影響程式的運作。

* `#` 是單行註解
*  是多行註解

```python
# 這是單行註解
\"""
這是多行註解
可以寫好幾行喔！
\"""
```

---

## 📤 用 `print()` 把東西印出來

```python
print(123)         # 印出數字
print(3.14)        # 印出小數
print(True)        # 印出布林值「真」
print(False)       # 印出布林值「假」
print("Hello!")    # 印出字串（文字）
```

---

## 📦 變數（就像裝東西的盒子）

```python
a = 10
print(a)           # 印出 10

a = "apple"        # 把 a 改成蘋果
print(a)           # 印出 apple
```

你可以用變數做數學運算：

```python
x = 4
x = x + 3          # x 變成 7
x = x * 2          # x 變成 14
```

---

## ➕ 算數運算

```python
print(7 + 3)     # 加法：10
print(7 - 3)     # 減法：4
print(7 * 3)     # 乘法：21
print(7 / 3)     # 除法：2.333...
print(7 // 3)    # 整除：2（只看整數）
print(7 % 3)     # 餘數：1
print(2 ** 3)    # 次方：2的3次方 = 8
```

---

## 🧮 小數計算要小心

```python
v1 = 0.1
v2 = 0.2
print(v1 + v2)   # 有時候結果會不是 0.3，這是電腦的精度問題
```

---

## ✨ 字串（文字）的魔法

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)            # 印出 Hello World
print(s1 + s2 * 3)   # 印出 HelloWorldWorldWorld
```

---

## 🧑‍💻 f-string 可以讓文字變聰明！

```python
name = "python"
age = 31
print(f"我是 {name}, 今年 {age} 歲")
```

---

## 📏 看字的長度

```python
print(len("Hello"))  # 印出 5
print(len(" "))      # 印出 1（空白也是字！）
```

---

## 🔍 看資料的類型（type）

```python
print(type(123))       # int（整數）
print(type(3.14))      # float（小數）
print(type("Hi"))      # str（字串）
print(type(True))      # bool（布林值）
```

---

## 🔄 不同資料可以互相轉換

```python
print(int(True))     # 1
print(float("123"))  # 123.0
print(bool(0))       # False
print(bool("hello")) # True
print(str(1000))     # "1000"
```

❗ 注意：不能把 "hello" 這樣的文字轉成數字，會錯誤喔！

---

## ⌨️ 輸入資料 input()

```python
get = input("請輸入一些內容: ")
print(get)
print(type(get))  # 注意：輸入進來的東西都是字串喔！
```

---

## 🧠 小挑戰：算圓面積

```python
r = int(input("請輸入圓半徑長度: "))
area = 3.14 * r ** 2
print(f"圓面積為: {area}")  # 用 f-string
print("圓面積為:", area)    # 用逗號
```

---

## 📄 使用 Streamlit 畫網頁（初步）

```python
import streamlit as st

st.title("這是標題")
st.write("這是 write 寫的內容")
st.text("這是 text 寫的內容")
```

---

## 📝 Markdown 可以排版文字

````python
st.markdown(
* **粗體文字**
* *斜體文字*
* [連結](https://example.com)
* 程式碼:
```python
print("Hello World!")
````

# 這是大標題

## 這是中標題

### 小一點的標題

#### 更小的標題

"""
)

with st.expander("Class 2 課堂筆記"):
st.write(
"""

---

## 🐍 Python 第 2 堂課 學習筆記（簡單版）

### 🧮 一、比較運算子（比大小）

比較兩個東西，看看是不是一樣、誰比較大或比較小：

```python
print(1 == 1)   # 等於 → True
print(1 != 1)   # 不等於 → False
print(1 >= 2)   # 大於或等於 → False
print(1 <= 2)   # 小於或等於 → True
print(1 > 2)    # 大於 → False
print(1 < 2)    # 小於 → True
```

---

### 🧠 二、邏輯運算子（True 和 False 的遊戲）

```python
print(not True)      # 不是 → False
print(not False)     # 不是 → True

print(True and True)     # 兩個都要 True → True
print(True and False)    # 一個是 False → False
print(False or True)     # 只要一個是 True → True
print(False or False)    # 全部都是 False → False
```

---

### 🔐 三、密碼判斷（if...else）

```python
password = input("請輸入密碼: ")

if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
```

你也可以判斷多個密碼：

```python
if password == "1234":
    print("歡迎 Ray")
elif password == "5678":
    print("歡迎小明")
elif password == "abcd":
    print("歡迎小華")
else:
    print("密碼錯誤，請重新輸入")
```

---

### 🌍 四、判斷閏年

閏年規則比較複雜，我們用 if 判斷：

```python
year = int(input("請輸入年份: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("閏年")
        else:
            print("平年")
    else:
        print("閏年")
else:
    print("平年")
```

---

### 🖥️ 五、Streamlit 練習（做出互動畫面）

Streamlit 是一種讓程式變成漂亮網頁的工具。

#### 🎮 輸入數字並顯示

```python
import streamlit as st

nuber = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)
st.write(f"你輸入的數字是: {nuber}")
```

#### 💯 分數等級判斷

```python
score = st.number_input("請選擇分數", min_value=0, max_value=100, value=60, step=1)

if score >= 90:
    st.write("A級")
elif score >= 80:
    st.write("B級")
elif score >= 70:
    st.write("C級")
elif score >= 60:
    st.write("D級")
else:
    st.write("E級")
```

#### 🎈 點按鈕會有動畫

```python
st.button("點我", key="button1")

if st.button("點我", key="button2"):
    st.balloons()  # 放氣球動畫

if st.button("點我", key="button3"):
    st.snow()  # 下雪動畫
```

---

### 🔁 六、for 迴圈（重複做事情）

```python
for i in range(10):
    print(i)  # 從 0 到 9

for i in range(2, 6):
    print(i)  # 從 2 到 5

for i in range(2, 10, 2):
    print(i)  # 從 2 開始，每次加2，到 8
```

---

### 🏯 七、金字塔程式

#### 數字金字塔

```python
for i in range(1, 數字 + 1):
    print(str(i) * i)
```

輸入 3 →

```
1
22
333
```

#### 箭頭金字塔

使用空白 + 星星 `*` 來畫出圖形！

```python
for i in range(1, 層數 + 1):
    print(" " * (層數 - i) + "*" * (i * 2 - 1))

for i in range(層數):
    print(" " * (層數 - 1) + "*")
```

---

### 📦 八、串列 List（放很多資料）

```python
L1 = []  # 空串列
L2 = ["蘋果"]
L3 = ["蘋果", "香蕉", "橘子"]
L4 = [1, 2, 3, 4, 5]
L5 = [1, "蘋果", True, 3.14]  # 不同類型也可以放
L6 = [1, 2, 3, ["蘋果", "香蕉"]]  # 裡面還有串列！
```

#### 取資料

```python
print(L6[1])        # 取出第2個（從0開始）
print(L6[3][0])     # 取出第4個裡面的第1個
```

#### 切資料（切片）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[1:4:2])  # 每兩個取一次 → [2, "a"]
print(L[1:4])    # 從第2到第4（不包含第4） → [2, 3, "a"]
print(L[::2])    # 每兩個取一個 → [1, 3, "b"]
```

---

如果你是用 Streamlit 可以把這些做成互動小網頁，非常有趣！

需要我幫你改成卡片版圖文講義也可以喔 🙌
還有不懂的地方也可以再問我～
"""
)

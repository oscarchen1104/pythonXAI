---
# 🐍 第四堂 Python 課筆記：字典、圖片、函式、骰子遊戲
---

## 🔑 一、字典（dictionary）

字典就像一個小本子，可以用「關鍵字」找到對應的「內容」。

```python
d = {"apple": "蘋果", 2: "二", 3: "three"}
```

- `d["apple"]` → 找到的是「蘋果」
- `d[2]` → 找到的是「二」

### ⭐ 認識字典的東西：

```python
for key in d.keys():   # 顯示所有「關鍵字」
    print(key)

for value in d.values():  # 顯示所有「值」
    print(value)

for key, value in d.items():  # 同時顯示 key 和 value
    print(key, ":", value)
```

### ⭐ 修改與刪除字典：

```python
d[2] = "二"          # 改變2的內容
d[4] = "four"        # 加入新內容
d.pop(1)             # 刪掉key為1的項目
```

### ⭐ 查詢與長度：

```python
print(2 in d)          # 看看有沒有這個 key
print("three" in d)    # 注意只能找 key，不能找 value
print(len(d))          # 字典裡有幾個項目
```

---

## 🖼️ 二、用 Streamlit 顯示圖片

### `streamlit` 是可以做「互動網頁」的小工具！

```python
import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)  # 把 image 資料夾裡的圖片名稱存起來

img_size = st.number_input("圖片大小", min_value=50, max_value=500, value=300, step=50)

for img in files:
    st.image(f"{file_path}/{img}", width=img_size)
```

---

## 🛒 三、建立購物平台（Streamlit 進階）

### 建立商品資訊：

每個商品有名字、價格、圖片、庫存。

### 可以：

- 顯示商品
- 按鈕購買（庫存會減少）
- 增加庫存數量
- 顯示目前的庫存

這就是一個簡單的「購物網頁」啦！

---

## 🧠 四、函式（function）

函式就是幫你包好「一段會做事的程式碼」，以後要用的時候直接叫名字就好！

```python
def hello():
    print("hello")

def hello2(name):
    print("hello", name)

def my_max(a, b):
    if a > b:
        return a
    else:
        return b
```

### ⭐ 圓形面積函式：

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi
```

### ⭐ 區域變數與全域變數：

```python
def calculate_square_area():
    area = length ** 2  # 自己函式裡的變數，不會改外面的

def calculate_square_area3():
    global area
    area = length ** 2  # 會改全域變數的值
```

---

## 📏 五、計算距離（使用函式與 input）

```python
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
```

使用者輸入兩個點的座標，就可以算出它們之間的距離。

---

## 🎲 六、骰子遊戲

### 用 Python 模擬擲骰子好多次！

```python
import random

def roll_dice(n):  # 擲骰子n次
    save = []
    for i in range(n):
        number = random.randint(1, 6)
        save.append(number)
    return save
```

接著統計每個數字出現幾次：

```python
for num in outcomes:
    if num == 1:
        n1 += 1
    elif num == 2:
        n2 += 1
    ...
```

這樣就能知道哪個點數最常出現啦！

---

📘 **結語：**
今天學到的東西很多喔！從字典、圖片到函式和遊戲，我們已經能寫出很有趣的小程式了，繼續加油學習吧 💪！

---

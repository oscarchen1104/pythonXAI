---

# 🐍 Python 程式筆記（第 3 堂課）

## 🧮 1. 清單（List）

清單就像一個可以放很多東西的盒子，可以放水果、數字、文字等等。

```python
["蘋果", "香蕉", "橘子"]
[1, 2, 3]
```

### ➤ 看清單有幾個東西

```python
print(len([]))  # 結果是 0
print(len(["蘋果"]))  # 結果是 1
print(len(["a", "b"]))  # 結果是 2
```

### ➤ 一個一個把清單的東西拿出來看

```python
l = [1, 2, 3]

for i in range(len(l)):
    print(l[i])  # 用索引取值

for element in l:
    print(element)  # 直接把每個東西印出來
```

### ➤ 改清單裡的東西

```python
l[0] = "A"
l[2] = "c"
```

### ➤ 清單的影子（複製和引用）

```python
a = [10, 20, 30]
b = a      # b 只是 a 的影子，改 b 也會改到 a
b[1] = 200
print(a)   # a 也會變

c = [40, 50, 60]
d = c[:]   # d 是真的複製，改 d 不會影響 c
d[1] = 500
print(c)   # c 不會變
```

### ➤ 常用清單方法

```python
l.append(4)         # 加東西
l.remove("b")       # 刪掉「第一次」出現的 b
l.pop()             # 把最後一個東西拿掉
l.pop(1)            # 把第 1 個位置的東西拿掉
l.sort()            # 排序（數字從小到大、文字從 A 到 Z）
```

---

## 🧱 2. Streamlit 製作網頁互動小工具

### ➤ 顯示標題和按鈕

```python
st.title("我的網頁標題")
st.button("按我一下")
```

### ➤ 欄位排版（像分左右兩邊）

```python
col1, col2 = st.columns(2)
col1.button("左邊的按鈕")
col2.button("右邊的按鈕")
```

### ➤ 文字輸入框

```python
text = st.text_input("請輸入文字")
st.write("你輸入的是:", text)
```

### ➤ 記住變數（session_state）

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

if st.button("加 1"):
    st.session_state.var1 += 1
    st.rerun()
```

---

## 🍔 3. 點餐機（互動式購物籃）

```python
food = st.text_input("請輸入餐點")
if st.button("加入"):
    st.session_state.order.append(food)

# 顯示購物籃內容
for i in range(len(st.session_state.order)):
    st.write(st.session_state.order[i])
    if st.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
```

---

## 🔁 4. while 和 for 迴圈

### ➤ 重複做事情的 while 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### ➤ 提早停止 break

```python
while i < 5:
    if i == 3:
        break
```

---

## 🎲 5. 隨機數字（random）

```python
import random

print(random.randrange(1, 4))  # 隨機從 1~3 中選一個
print(random.randint(10, 20))  # 隨機從 10~20 中選一個（包含頭尾）
```

### ➤ 投票統計小遊戲

```python
count1 = 0
count2 = 0
count3 = 0

for i in range(30):
    n = random.randrange(1, 4)
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    elif n == 3:
        count3 += 1
```

---

## 🎯 6. 猜數字遊戲

```python
target = random.randint(1, 100)

while True:
    guess = int(input("請猜一個數字: "))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜對了")
        break
```

---

## 🏆 7. 一番賞抽獎遊戲

```python
table = [0] * 100  # 準備 100 張獎券
target = random.randint(1, 100)  # 有一張是中獎的
table[target - 1] = 1

while True:
    pick = random.randint(1, 100)
    if table[pick - 1] == 1:
        print("恭喜你抽中了！")
        break
    elif table[pick - 1] == 2:
        print("這張抽過了")
    else:
        print("沒有中，再抽一次")
    table[pick - 1] = 2
```

---

import streamlit as st

with st.expander("Class 1 課堂筆記"):
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

with st.expander("Class 2 課堂筆記"):
    st.write(
        """
---

## 🐍 Python 第2堂課 學習筆記（簡單版）

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

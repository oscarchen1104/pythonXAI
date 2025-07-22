import streamlit as st

st.write("## 數字金字塔")
nuber = st.number_input(
    "請輸入一個數字(1到9)", min_value=1, max_value=9, value=1, step=1
)

st.write(f"數字金字塔: {nuber}")
for i in range(1, nuber + 1):
    st.write(str(i) * i)

st.write("## 箭頭金字塔")
num2 = st.number_input("請輸入箭頭層數", min_value=1, value=1, step=1)
arrow = ""
for i in range(1, num2 + 1):
    arrow = arrow + (" " * (num2 - i) + "*" * (i * 2 - 1) + "\n")
for i in range(num2):
    arrow = arrow + (" " * (num2 - 1) + "*" + "\n")
st.write(
    f"""
```
箭頭金字塔:
{arrow}    
```
"""
)

# import streamlit as st

# nuber = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)

# st.write(f"你輸入的數字是: {nuber}")


import streamlit as st

nuber = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)

st.write(f"你輸入的數字是: {nuber}")

st.write("## 練習")
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

st.button("點我", key="button1")

if st.button("點我", key="button2"):
    st.balloons()

if st.button("點我", key="button3"):
    st.snow()

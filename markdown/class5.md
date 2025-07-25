---
# 🧠 第五堂課：AI 聊天機器人與互動遊戲筆記 ✨

今天我們學到的內容，主要是怎麼用 Python 做出可以跟我們說話的 AI 機器人，還能做出聊天畫面，甚至玩遊戲唷！以下是我們今天學到的重點：
---

## 📦 一開始要做的事：導入工具

```python
import openai
import streamlit as st
import os
```

- `import` 就像打開工具箱，讓我們可以用工具來寫程式。
- `openai` 是用來跟 AI 說話的工具。
- `streamlit` 是用來做網頁介面（可以點按鈕、輸入訊息的畫面）。
- `os` 和 `dotenv` 是幫助我們找到「金鑰」🔑（就是讓 AI 機器人能正常運作的密碼）。

---

## 🧠 做出簡單的聊天機器人（class5-1 & class5-2）

```python
user_input = input("你要問的問題: ")
```

- 這行是請使用者輸入問題。
- 如果使用者打「exit」或「quit」，就會離開。

機器人會用 `openai.chat.completions.create()` 回答問題，就像你正在和 ChatGPT 說話一樣！

---

## 💬 聊天畫面（class5-3）

使用 `streamlit` 來做出有「聊天泡泡」的畫面！

```python
st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是 AI 的回應")
```

- `user` 是使用者，`assistant` 是 AI。
- 還可以用表情符號當作頭像：😊 🤖

---

## 📜 記住聊天紀錄（class5-4）

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

- 我們用 `session_state` 來記住每次的聊天內容，不會馬上消失。
- 當使用者輸入新訊息，就把它存起來。

---

## ⚙️ 加入更多功能的聊天機器人（class5-5）

這是進階版的 AI 聊天畫面，功能更強大：

✅ 可以設定系統訊息（讓 AI 知道要用中文回應）
✅ 可以選擇不同的 AI 模型（像是 "gpt-4o" 或 "gpt-4o-mini"）
✅ 可以按一下 🗑️ 來清空聊天記錄！

---

## 🖼️ 上傳圖片，請 AI 幫忙看圖說話（class5-6）

```python
st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])
```

- 使用者可以上傳一張圖片 📷。
- AI 不只會看文字，還會分析圖片喔！
- 輸入文字+圖片給 AI，它就會用文字告訴你圖片的內容。

---

## 🧩 海龜湯遊戲（class5-7）

這個特別好玩！讓 AI 當成「遊戲主持人」，你當猜謎人！

- 遊戲主題會從 JSON 檔案讀進來。
- AI 會依照你問的問題，只回答「是」、「不是」、「無關」或提示。
- 如果你猜得很接近，AI 會公布答案並結束遊戲 🎉

---

## 🧠 學到的新東西整理

| 名稱                               | 用法                 | 功能說明                     |
| ---------------------------------- | -------------------- | ---------------------------- |
| `openai.chat.completions.create()` | 給 AI 問題，請它回答 | 跟 ChatGPT 對話的方式        |
| `st.chat_message()`                | 顯示聊天泡泡         | 做出聊天的畫面               |
| `st.session_state`                 | 記住資料             | 記得聊天內容或設定           |
| `st.file_uploader()`               | 上傳圖片             | 讓使用者傳圖給 AI 看         |
| `base64`                           | 把圖片變成文字碼     | 讓圖片能被 AI 理解           |
| `json.load()`                      | 讀入題目資料         | 讓 AI 玩遊戲前先知道題目內容 |

---

## ❤️ 小提醒

- 要讓 AI 能運作，要有「API 金鑰」，記得放在 `.env` 或 `st.secrets` 中。
- 當使用者輸入訊息時，要記得存起來，才能讓 AI 有聊天記憶喔！
- 用 `st.rerun()` 可以重新整理畫面，讓聊天即時更新！

---

📘 **今天我們已經會做一個能聊天、有記憶，還能玩遊戲和看圖說故事的 AI 介面囉！好厲害！👏👏👏**

---

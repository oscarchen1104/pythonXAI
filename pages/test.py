import streamlit as st
import openai
import json
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

with open("question/quizzes.json", "r", encoding="utf-8") as f:
    deta = json.load(f)
    pick = random.randrange(len(deta))
    quiz = deta[pick]

print(
    f"你是一名海龜湯遊戲的主持人,你只能回答(是/不是/無關),或在必要時給提示,如果玩家描述很接近正解,則輸出遊戲結束並講完整正解\n題目:{quiz['title']}\n正解:{quiz['answers']}"
)

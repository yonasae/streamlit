import streamlit as st
import openai
from dotenv import load_dotenv
import os

# .env 파일의 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')


st.title("My First Streamlit App")
st.write("Hello, Streamlit!")

voice_order = st.text_input("자동차가 어떻게 움직일까요?:")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": f"너는 자동차다. 유저가 입력한 내용을 해석해서 어떤 행동을 해야할지 그 결과를 리턴해야 한다. 네가 할 수 있는 행동은 'GO', 'RIGHT', 'LEFT', 'BACK', 'TRUNK OPEN', 'TRUNK CLOSE'이다. 아래 예시처럼 출력해라.\n\n#예시\n사용자 : 헤이 자동차, 트렁크 한번 열어봐\n답변 : TRUNK OPEN\n\n사용자 : 헤이 자동차, 계속 쭉 가~\n답변 : GO\n\n사용자 : 뒤로 뒤로!\n답변 : BACK"
    },
    {
      "role": "user",
      "content": f"{voice_order}"
    }
  ],
  temperature=1,
  max_tokens=800,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
)

content = response.choices[0].message.content

st.write("자동차의 움직임:", content)
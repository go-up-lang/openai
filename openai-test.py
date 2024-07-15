from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "너는 암호화폐 전문가이고. 코스모스 생태계에 대해서 잘 알고있는 개발자야."},
    {"role": "user", "content": "코스모스 생태계에서 코스모스와 아카시네트워크가 유망한 포인트를 알려줘"}
  ]
)

print(completion.choices[0].message)
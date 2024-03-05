from openai import OpenAI
import os
# import json

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello! I'm Taiga."}
#     ]
# )
#
# print(json.dumps(json.loads(response.model_dump_json()), indent=4))

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! I'm Taiga."}
    ],
    stream=True,
)
for chunk in stream:
    choice = chunk.choices[0]
    if choice.delta.content is not None:
        # print(choice.delta.content, end="")
        print(choice.delta.content)

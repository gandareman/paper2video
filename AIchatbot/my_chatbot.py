#%%
import os
import json
import openai
#%%
def get_value(filename, key):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get(key)
#%%
# gpt-3 key, organization 정보를 가져와서 openai에 연결
filename = "C:\C\gpt.json"
key = get_value(filename,'key')
Organization_ID = get_value(filename,'Organization_ID')
openai.api_key = key
openai.organization = Organization_ID
#%%
messages = []
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    assistant_content = response['choices'][0]['message']['content'].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    print(assistant_content)

#%%
#%%
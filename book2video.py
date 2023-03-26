#%%
import re
import json # key, organization get from json file
import fitz # pdf2text
from tqdm import tqdm # progress bar
import openai # GPT-3 connection

#%%
def get_value(filename, key):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get(key)
#%%
book_path = 'papers/Demian.pdf'
doc = fitz.open(book_path)
text = doc.get_page_text(pno=2) # 2nd page2text
print(text)
#%%
# gpt-3 key, organization 정보를 가져와서 openai에 연결
filename = "C:\C\gpt.json"
key = get_value(filename,'key')
Organization_ID = get_value(filename,'Organization_ID')
openai.api_key = key
openai.organization = Organization_ID
#%%
start_pno = 2
summarize_every = 15
summary_list = [{
    'role': 'system',
    'content': 'You are a helpful assistant for summarizing books'
}]
count = 0
content = ''

#%%
for pno in tqdm(range(start_pno, doc.page_count)):
    text = doc.get_page_text(pno=pno)

    # Preprocess text
    text = re.sub(r"\s+", " ", text)
    text = text.replace('Downloaded from https://www.holybooks.com', '').strip()
    # Remove page number
    text = ' '.join(text.split(' ')[:-1])

    if count == summarize_every:
        messages = [{
            'role': 'system',
            'content': 'You are a helpful assistant for summarizing books.'
        }, {
            'role': 'user',
            'content': f'Summarize this: {content}'
        }]

        res = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', # [todo] gpt-4 사용 권한이 주어지면 변경해야 됨
            messages=messages
        )

        msg = res['choices'][0]['message']['content']

        summary_list.append({
            'role': 'user',
            'content': msg
        })

        count = 0
        content = ''
    else:
        content += text + ' '
        count += 1
#%%
summary_list
#%%
# %%

#%%
# 이 코드는 OpenAI API를 사용하여 사용 가능한 모델 목록을 가져오고 출력하는 예제
import openai
import pprint


GPT4 = ''
# GPT4 = 'text-davinci-002'
# GPT4 = 'gpt-4-0314'
MODEL_NAME = GPT4
model = openai.Model(MODEL_NAME)

def list_all_models():
    model_list = openai.Model.list()['data']
    model_ids = [x['id'] for x in model_list]
    model_ids.sort()
    pprint.pprint(model_ids)

if __name__ == '__main__':
    list_all_models()
#%%
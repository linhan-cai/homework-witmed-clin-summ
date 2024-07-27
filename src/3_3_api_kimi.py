import openai
import os
import json 
from dotenv import dotenv_values
config = dotenv_values(".env")

def main():

    client = openai.OpenAI(
        api_key=config["KIMI_KEY"],
        base_url="https://api.moonshot.cn/v1",
    )

    # model_list = client.models.list()
    # model_data = model_list.data
    
    # for i, model in enumerate(model_data):
    #     print(f"model[{i}]:", model.id)
    
    # return 

    prompt_files = (
        ("./dataset/chq_prompt.jsonl", "./dataset/chq_kimi_result.jsonl", 100),
        ("./dataset/d2n_prompt.jsonl", "./dataset/d2n_kimi_result.jsonl", 20),
        ("./dataset/opi_prompt.jsonl", "./dataset/opi_kimi_result.jsonl", 100), 
    )

    # Define the system message
    system_msg = 'you are a knowledgeable medical professional. '
                                            
    for (file, result_file, limit) in prompt_files:
        with open(file, "r+") as fd, open(result_file, "a+") as fd_write:
            for i, row in enumerate(fd):
                # 先处理前100条
                if i >= limit:
                    break
                
                data = json.loads(row)
                prompt_text = data["prompt"]
                print(len(prompt_text))
                resp = client.chat.completions.create(
                    model="moonshot-v1-32k",
                    messages=[{"role": "user", "content": prompt_text}],
                    temperature=0.1,
                )
                fd_write.write(json.dumps({"output": {"text":resp.choices[0].message.content}}) + "\n")

if __name__ == "__main__":
    main()

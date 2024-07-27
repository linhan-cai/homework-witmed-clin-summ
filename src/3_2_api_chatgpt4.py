import openai
import os
import json 
from dotenv import dotenv_values
config = dotenv_values(".env")

def main():

    openai_client = openai.OpenAI(
        api_key=config["CHATGPT4_KEY"],
        base_url="https://api.aiguoguo199.com",
    )

    prompt_files = (
        ("./dataset/chq_prompt.jsonl", "./dataset/chq_chatgpt4_result.jsonl", 100),
        ("./dataset/d2n_prompt.jsonl", "./dataset/d2n_chatgpt4_result.jsonl", 20),
        ("./dataset/opi_prompt.jsonl", "./dataset/opi_chatgpt4_result.jsonl", 100), 
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
                resp = openai_client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt_text}],
                    temperature=0.1,
                )
                fd_write.write(json.dumps({"output": {"text":resp.output}}) + "\n")
                print(resp.output)
                break

if __name__ == "__main__":
    main()

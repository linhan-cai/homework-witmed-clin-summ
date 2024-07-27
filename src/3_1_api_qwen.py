import dashscope
import os
import json 
from dotenv import dotenv_values
config = dotenv_values(".env")

def main():

    dashscope.api_key = config["QWEN_KEY"]

    prompt_files = (
        ("./dataset/chq_prompt.jsonl", "./dataset/chq_qwen_result.jsonl", 100),
        ("./dataset/d2n_prompt.jsonl", "./dataset/d2n_qwen_result.jsonl", 20),
        ("./dataset/opi_prompt.jsonl", "./dataset/opi_qwen_result.jsonl", 100), 
    )

    for (file, result_file, limit) in prompt_files:
        with open(file, "r+") as fd, open(result_file, "w+") as fd_write:
            for i, row in enumerate(fd):
                # 先处理前100条
                if i >= limit:
                    break
                
                data = json.loads(row)
                prompt_text = data["prompt"]
                print(len(prompt_text))
                resp = dashscope.Generation.call(
                    model='qwen-plus',
                    temperature=0.1,
                    prompt=prompt_text
                )
                fd_write.write(json.dumps({"output": resp.output}) + "\n")
                print(resp.output)

if __name__ == "__main__":
    main()

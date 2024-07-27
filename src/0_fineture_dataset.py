import requests
import json 

from dotenv import dotenv_values
config = dotenv_values(".env")


def main():
    
    files = [
        ("./dataset/chq.jsonl", "./dataset/fineture/chq.json"), 
        ("./dataset/d2n.jsonl", "./dataset/fineture/d2n.json"),
        ("./dataset/opi.jsonl", "./dataset/fineture/opi.json"),
    ]

    for source_file, target_file in files:
        with open(source_file, "r") as fd_r, open(target_file, "a+") as fd_w:
            for row in fd_r:
                dct = json.loads(row)
                sample = {'conversations': [{'role': 'user', 'content': dct['inputs']},
                                            {'role': 'assistant', 'content': dct['target']}]}
                fd_w.write(json.dumps(sample, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()

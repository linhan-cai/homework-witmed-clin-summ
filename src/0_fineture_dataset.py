import json 
import os

from dotenv import dotenv_values
config = dotenv_values(".env")


def main():
    
    output_path = "./dataset/fineture"
    files = [
        ("./dataset/chq.jsonl", 100, 200), 
        ("./dataset/d2n.jsonl", 20, 30),
        ("./dataset/opi.jsonl", 100, 200),
    ]

    dev_file = os.path.join(output_path, "dev.json")
    train_file = os.path.join(output_path, "train.json")
    for source_file, test_i, dev_i in files:
        with open(source_file, "r") as fd_r, open(dev_file, "a+") as fd_dev, open(train_file, "a+") as fd_train:
            for i, row in enumerate(fd_r):
                if i < test_i:
                    continue

                dct = json.loads(row)
                sample = {
                    'conversations': [
                        {'role': 'user', 'content': dct['inputs']},
                        {'role': 'assistant', 'content': dct['target']}
                    ]
                }
                
                if i < dev_i:
                    fd_dev.write(json.dumps(sample, ensure_ascii=False) + "\n")
                else:
                    fd_train.write(json.dumps(sample, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()

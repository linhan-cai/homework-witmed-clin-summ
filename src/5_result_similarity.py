import numpy as np

import requests
import json 

session = requests.Session()

from dotenv import dotenv_values
config = dotenv_values(".env")
embedding_api = config["EMBEDDING_API"]

def main():

    files = [
        ("./dataset/chq_target_embedding.jsonl", "./dataset/chq_qwen_result_embedding.jsonl", "./dataset/chq_qwen_score.jsonl"), 
        ("./dataset/d2n_target_embedding.jsonl", "./dataset/d2n_qwen_result_embedding.jsonl", "./dataset/d2n_qwen_score.jsonl"), 
        ("./dataset/opi_target_embedding.jsonl", "./dataset/opi_qwen_result_embedding.jsonl", "./dataset/opi_qwen_score.jsonl"), 

        ("./dataset/chq_target_embedding.jsonl", "./dataset/chq_kimi_result_embedding.jsonl", "./dataset/chq_kimi_score.jsonl"), 
        ("./dataset/d2n_target_embedding.jsonl", "./dataset/d2n_kimi_result_embedding.jsonl", "./dataset/d2n_kimi_score.jsonl"), 
        ("./dataset/opi_target_embedding.jsonl", "./dataset/opi_kimi_result_embedding.jsonl", "./dataset/opi_kimi_score.jsonl"), 

        ("./dataset/chq_target_embedding.jsonl", "./dataset/chq_chatgpt4_result_embedding.jsonl", "./dataset/chq_chatgpt4_score.jsonl"), 
        ("./dataset/d2n_target_embedding.jsonl", "./dataset/d2n_chatgpt4_result_embedding.jsonl", "./dataset/d2n_chatgpt4_score.jsonl"), 
        ("./dataset/opi_target_embedding.jsonl", "./dataset/opi_chatgpt4_result_embedding.jsonl", "./dataset/opi_chatgpt4_score.jsonl"), 
    ]

    for source_file, target_file, score_file in files:
        with open(source_file, "r") as fd_source, open(target_file, "r") as fd_target, open(score_file, "w+") as fd_w:
            for row_target in fd_target:

                row_source = fd_source.readline()

                data_source = json.loads(row_source)
                data_target = json.loads(row_target)

                similarity = cosine_similarity(data_source["embedding"], data_target["result_embedding"])
                print(similarity)
                fd_w.write(json.dumps({"similarity": similarity}, ensure_ascii=False) + "\n")


def cosine_similarity(vec1, vec2):
    # 计算点积
    dot_product = np.dot(vec1, vec2)
    
    # 计算每个向量的范数
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # 计算余弦相似度
    similarity = dot_product / (norm_vec1 * norm_vec2)
    
    # 计算余弦距离
    return similarity
    

if __name__ == "__main__":
    main()



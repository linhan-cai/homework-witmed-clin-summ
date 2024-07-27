import numpy as np
from dotenv import dotenv_values
config = dotenv_values(".env")
import requests
import json 

session = requests.Session()



embedding_api = config["EMBEDDING_API"]

def main():

    files = [
        ("./dataset/chq_qwen_result.jsonl", "./dataset/chq_qwen_result_embedding.jsonl"), 
        ("./dataset/d2n_qwen_result.jsonl", "./dataset/d2n_qwen_result_embedding.jsonl"), 
        ("./dataset/opi_qwen_result.jsonl", "./dataset/opi_qwen_result_embedding.jsonl"), 

        ("./dataset/chq_kimi_result.jsonl", "./dataset/chq_kimi_result_embedding.jsonl"), 
        ("./dataset/d2n_kimi_result.jsonl", "./dataset/d2n_kimi_result_embedding.jsonl"), 
        ("./dataset/opi_kimi_result.jsonl", "./dataset/opi_kimi_result_embedding.jsonl"), 

        ("./dataset/chq_chatgpt4_result.jsonl", "./dataset/chq_chatgpt4_result_embedding.jsonl"), 
        ("./dataset/d2n_chatgpt4_result.jsonl", "./dataset/d2n_chatgpt4_result_embedding.jsonl"), 
        ("./dataset/opi_chatgpt4_result.jsonl", "./dataset/opi_chatgpt4_result_embedding.jsonl"), 
    ]

    for source_file, target_file in files:
        with open(source_file, "r") as fd_r, open(target_file, "w+") as fd_w:
            for row in fd_r:
                entity = json.loads(row)
                print(entity)

                rsp_body = session.post(
                    url=embedding_api,
                    json={
                        "texts": [
                            entity["output"]["text"]
                        ],
                    }
                ).json()
                fd_w.write(json.dumps({"result_embedding": base64_to_float32_array(rsp_body["vectors"][0])}, ensure_ascii=False) + "\n")


def base64_to_float32_array(base64_encoded_data):
    import base64
    import struct

    binary_data = base64.b64decode(base64_encoded_data)

    # 使用struct.unpack解析二进制数据，并将其转换为浮点数数组
    float_array = []
    # 计算浮点数数组的长度
    num_floats = len(binary_data) // 4  # 每个浮点数占4个字节
    for i in range(num_floats):
        # 从二进制数据中提取一个浮点数，并将其解析为float类型，然后添加到浮点数数组中
        float_value = struct.unpack('f', binary_data[i * 4: (i + 1) * 4])[0]
        float_array.append(float_value)
    return float_array


if __name__ == "__main__":
    main()


def cosine_distance(vec1, vec2):
    # 计算点积
    dot_product = np.dot(vec1, vec2)
    
    # 计算每个向量的范数
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # 计算余弦相似度
    cosine_similarity = dot_product / (norm_vec1 * norm_vec2)
    
    # 计算余弦距离
    cosine_distance = 1 - cosine_similarity
    
    return cosine_distance
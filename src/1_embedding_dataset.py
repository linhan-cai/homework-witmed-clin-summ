import requests
import json 

from dotenv import dotenv_values
config = dotenv_values(".env")
embedding_api = config["EMBEDDING_API"]

session = requests.Session()
# mixedbread-ai/mxbai-embed-large-v1



def main():
    
    files = [
        ("./dataset/chq.jsonl", "./dataset/chq_target_embedding.jsonl"), # done
        ("./dataset/d2n.jsonl", "./dataset/d2n_target_embedding.jsonl"), # done
        ("./dataset/opi.jsonl", "./dataset/opi_target_embedding.jsonl"), # done
    ]

    for source_file, target_file in files:
        with open(source_file, "r") as fd_r, open(target_file, "a+") as fd_w:
            for row in fd_r:
                entity = json.loads(row)
                print(entity)

                rsp_body = session.post(
                    url=embedding_api,
                    json={
                        "texts": [
                            entity["target"]
                        ],
                    }
                ).json()
                fd_w.write(json.dumps({"embedding": base64_to_float32_array(rsp_body["vectors"][0])}, ensure_ascii=False) + "\n")


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

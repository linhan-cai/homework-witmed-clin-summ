import numpy as np 
import json 
import faiss

def main():


    files = [
        ("./dataset/chq.jsonl", "./dataset/chq_embedding.jsonl"),
        ("./dataset/d2n.jsonl", "./dataset/d2n_embedding.jsonl"),
        ("./dataset/opi.jsonl", "./dataset/opi_embedding.jsonl"),
    ]
    
    dimension = 1024
    top_k = 5

    index = faiss.IndexFlatL2(dimension)
    for source_file, embedding_file in files:
        
        dict_entities = {}
        dict_embedding = {}

        with open(source_file, "r") as fd_source:
            for i, row in enumerate(fd_source):
                dict_entities[i] = json.loads(row)

        embeddings = []
        with open(embedding_file, "r") as fd_embedding:
            for i, row in enumerate(fd_embedding):
                data = np.array(json.loads(row)["embedding"], dtype=np.float32)
                embeddings.append(data)
                dict_embedding[i] = json.loads(row)


        index.add(np.array(embeddings))
        _, result_ids = index.search(np.array(embeddings[:1]), top_k)
        for id in result_ids[0]:
            print(id)
            print(dict_entities[int(id)])
            print("\n")

        print(result_ids)
    

if __name__ == "__main__":
    main()

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import pickle

class Indexer:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = None

    def create_index(self, documents: List[Dict[str, str]]):
        texts = [doc['text'] for doc in documents]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype('float32'))
        self.documents = documents

    def save(self, index_path: str, data_path: str):
        faiss.write_index(self.index, index_path)
        with open(data_path, 'wb') as f:
            pickle.dump(self.documents, f)

    def load(self, index_path: str, data_path: str):
        self.index = faiss.read_index(index_path)
        with open(data_path, 'rb') as f:
            self.documents = pickle.load(f)

    def search(self, query: str, k: int = 5) -> List[Dict[str, str]]:
        query_embedding = self.model.encode([query])[0]
        distances, indices = self.index.search(query_embedding.reshape(1, -1).astype('float32'), k)
        return [self.documents[i] for i in indices[0]]
import os
import nltk
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

nltk.download('punkt', quiet=True)

class DocumentProcessor:
    def __init__(self, documents_dir: str):
        self.documents_dir = documents_dir

    def process_documents(self) -> List[Dict[str, str]]:
        documents = []
        with ThreadPoolExecutor() as executor:
            futures = []
            for filename in os.listdir(self.documents_dir):
                if filename.endswith('.txt'):
                    future = executor.submit(self._process_file, filename)
                    futures.append(future)
            
            for future in as_completed(futures):
                documents.extend(future.result())
        
        return documents

    def _process_file(self, filename: str) -> List[Dict[str, str]]:
        file_documents = []
        filepath = os.path.join(self.documents_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = nltk.sent_tokenize(content)
            for sentence in sentences:
                if len(sentence.strip()) > 10:
                    file_documents.append({
                        'text': sentence.strip(),
                        'source': filename
                    })
        return file_documents
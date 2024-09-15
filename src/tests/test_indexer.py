import unittest
from src.model.indexer import Indexer
import tempfile
import os

class TestIndexer(unittest.TestCase):
    def setUp(self):
        self.indexer = Indexer()
        self.documents = [
            {'text': 'This is a test sentence.', 'source': 'doc1.txt'},
            {'text': 'This is another test sentence.', 'source': 'doc2.txt'},
        ]
        self.indexer.create_index(self.documents)

    def test_search(self):
        results = self.indexer.search("test sentence", k=2)
        self.assertEqual(len(results), 2)
        self.assertIn(results[0]['text'], [doc['text'] for doc in self.documents])

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            index_path = os.path.join(temp_dir, "test_index.faiss")
            data_path = os.path.join(temp_dir, "test_data.pkl")
            
            self.indexer.save(index_path, data_path)
            
            new_indexer = Indexer()
            new_indexer.load(index_path, data_path)
            
            self.assertEqual(len(new_indexer.documents), len(self.documents))
            self.assertEqual(new_indexer.documents[0]['text'], self.documents[0]['text'])

if __name__ == '__main__':
    unittest.main()
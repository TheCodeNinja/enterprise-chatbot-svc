import unittest
from src.data.document_processor import DocumentProcessor
import tempfile
import os

class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        with open(os.path.join(self.temp_dir, "test_doc.txt"), "w") as f:
            f.write("This is a test sentence. This is another test sentence.")

    def tearDown(self):
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_process_documents(self):
        processor = DocumentProcessor(self.temp_dir)
        documents = processor.process_documents()
        
        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[0]['text'], "This is a test sentence.")
        self.assertEqual(documents[1]['text'], "This is another test sentence.")
        self.assertEqual(documents[0]['source'], "test_doc.txt")

if __name__ == '__main__':
    unittest.main()
import unittest
from src.model.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_generate_response(self):
        query = "What is the capital of France?"
        context = [
            {'text': 'Paris is the capital of France.', 'source': 'doc1.txt'},
            {'text': 'France is a country in Europe.', 'source': 'doc2.txt'},
        ]
        
        response = self.chatbot.generate_response(query, context)
        
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertIn("Paris", response)

if __name__ == '__main__':
    unittest.main()
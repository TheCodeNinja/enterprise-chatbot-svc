import argparse
from src.data.document_processor import DocumentProcessor
from src.model.indexer import Indexer

def main(documents_dir, index_path, data_path):
    # Process documents
    doc_processor = DocumentProcessor(documents_dir)
    documents = doc_processor.process_documents()

    # Create and save index
    indexer = Indexer()
    indexer.create_index(documents)
    indexer.save(index_path, data_path)

    print(f"Indexed {len(documents)} documents")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index documents for the chatbot")
    parser.add_argument("--documents_dir", required=True, help="Directory containing the documents")
    parser.add_argument("--index_path", default="data/document_index.faiss", help="Path to save the FAISS index")
    parser.add_argument("--data_path", default="data/document_data.pkl", help="Path to save the document data")
    
    args = parser.parse_args()
    main(args.documents_dir, args.index_path, args.data_path)
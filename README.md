# Enterprise Chatbot

This project implements an enterprise-grade chatbot API using FastAPI, FAISS for document indexing, and a fine-tuned language model for response generation.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/enterprise-chatbot.git
cd enterprise-chatbot
```

2. Install the required packages:
pip install -e .

Copy

## Usage

1. Index your documents:
index-documents --documents_dir /path/to/your/documents

Copy

2. (Optional) Fine-tune the language model:
train-model --output_dir /path/to/save/model --train_file /path/to/training/data.txt

Copy

3. Run the API:
uvicorn src.api.main:app --host 0.0.0.0 --port 8000

Copy

## Docker

To build and run the Docker container:

docker build -t enterprise-chatbot .
docker run -p 8000:8000 enterprise-chatbot

Copy

## Kubernetes Deployment

Apply the Kubernetes configurations:

kubectl apply -f k8s/dev/ # For development environment
kubectl apply -f k8s/prod/ # For production environment

Copy

## Testing

Run the tests using:

python -m unittest discover tests

Copy

## License

This project is licensed under the MIT License - see the LICENSE file for details.
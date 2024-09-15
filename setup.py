from setuptools import setup, find_packages

setup(
    name="enterprise-chatbot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.68.0",
        "uvicorn==0.15.0",
        "redis==3.5.3",
        "faiss-cpu==1.7.1",
        "sentence-transformers==2.1.0",
        "torch==1.9.0",
        "transformers==4.11.3",
        "nltk==3.6.3",
        "pydantic==1.8.2",
    ],
    entry_points={
        "console_scripts": [
            "index-documents=scripts.index_documents:main",
            "train-model=scripts.train_model:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An enterprise-grade chatbot API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/enterprise-chatbot",
)
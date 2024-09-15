from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.model.indexer import Indexer
from src.model.chatbot import Chatbot
import redis
from functools import lru_cache
import os
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=0,
    decode_responses=True
)

@lru_cache()
def get_indexer():
    indexer = Indexer()
    indexer.load('data/document_index.faiss', 'data/document_data.pkl')
    return indexer

@lru_cache()
def get_chatbot():
    return Chatbot()

class Query(BaseModel):
    text: str

@router.post("/chat")
async def chat(query: Query, indexer: Indexer = Depends(get_indexer), chatbot: Chatbot = Depends(get_chatbot)):
    try:
        # Check cache
        cached_response = redis_client.get(query.text)
        if cached_response:
            logger.info(f"Cache hit for query: {query.text}")
            return {"response": cached_response}

        # Search similar documents
        similar_docs = indexer.search(query.text)

        # Generate response
        response = chatbot.generate_response(query.text, similar_docs)

        # Cache the response
        redis_client.setex(query.text, 3600, response)  # Cache for 1 hour

        logger.info(f"Processed query: {query.text}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
from fastapi import FastAPI
from src.api.routes import router
from src.utils.logging_config import setup_logging

app = FastAPI(title="Enterprise Chatbot API", version="1.0.0")
app.include_router(router)

setup_logging()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
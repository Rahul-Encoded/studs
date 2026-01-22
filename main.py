from fastapi import FastAPI
from routes.routes import endpoints
import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()


SERVER_URL = os.getenv("SERVER_URL", "127.0.0.1")
PORT = os.getenv("PORT", "8000")
ENV = os.getenv("ENV", "dev")

app = FastAPI()

app.include_router(endpoints)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=SERVER_URL, 
        port=int(PORT), 
        reload=(ENV == "dev")
    )

import uvicorn
from fastapi import FastAPI
from src.nltk.router import router as router_ntlk

app = FastAPI(title="FastAPI with NLTK", version="0.1.0")


@app.get("/", summary="Root Endpoint", description="This is the root endpoint of the API.")
async def root():
    return {"message": "Hello Guys!"}

app.include_router(router_ntlk, prefix="/nltk")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "assistant ia ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )

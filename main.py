from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "main page"}

@app.get("/health")
def health():
    return {
        "health": "ok"
    }
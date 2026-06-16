from fastapi import FastAPI
from routers.tasks import router as tasks_router

app = FastAPI()
app.include_router(tasks_router)


@app.get("/")
def main():
    return {"message": "main page"}


@app.get("/health")
def health():
    return {"health": "ok"}
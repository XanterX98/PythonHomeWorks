from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    pass


@app.get("/ping")
def ping_view():
    return {"message": "pong"}

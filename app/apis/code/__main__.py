from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import uvicorn

app = FastAPI()

@app.post("/api")
def helloa():
    return {"message": "Hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get("/api/health")
def get_health():
    return {"message": "Ok"}


# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app="__main__:app", host="localhost", port=8888, reload=True)

import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Response, Request

from utils import get_stock_info


app = FastAPI()

# app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

template_obj = Jinja2Templates(directory="../frontend")


@app.get("/api/health")
def get_health():
    return {"message": "Ok"}


# http://127.0.0.1:8000/api/thing?thing=35325
@app.get("/api/thing")
async def stock_info(request: Request, thing):
    company_info = get_stock_info(thing)

    if not company_info:
        return template_obj.TemplateResponse(
            name="index.html",
            context={"request": request, "info": {"error": "nothing found"}},
        )

    return template_obj.TemplateResponse(
        name="index.html",
        context={"request": request, "info": company_info},
    )


# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app="__main__:app", host="localhost", port=8888, reload=True)

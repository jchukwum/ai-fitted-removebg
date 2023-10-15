from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from services.remove_bg import remove_bg_of_img
app = FastAPI()

class Item(BaseModel):
    url: str

@app.post("/api/v1/removebg")
def fetch(item: Item):
    try:
        no_bg = remove_bg_of_img(item.url)
        return {"image": no_bg}
    except:
        return {"content": "Unknown error", "status":500}

@app.get("/api/v1/status")
def status():
    return {"status": "RUNNING"}


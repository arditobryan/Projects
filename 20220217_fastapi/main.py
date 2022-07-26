from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import asyncio
#from sentence_transformers import SentenceTransformer

#from sentence_transformers import SentenceTransformer
#model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
current = dict()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(num):
    #add to queue
    value_list = current.values()
    if num not in value_list:
        dict_len = len(value_list)
        current[dict_len+1] = num

        #run code
        await asyncio.sleep(3)

        #remove from queue
        del current[dict_len+1]

        return int(num)*2
        #return {"response" : model.encode(sentence).tolist()}
    else:
        return str(num)+' already running'

@app.get("/current/")
async def root():
    return current

#running fastapi on the port we want
if __name__ == "__main__":
    #main is the name of the file
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

#to work, it should be called this way: 
#   python3 main.py
#if there is an error, for any reason: 
#   uvicorn main:app --port 3000

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

#from sentence_transformers import SentenceTransformer
#model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

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
async def create_item(sentence):
    return {"response" : model.encode(sentence).tolist()}

#running fastapi on the port we want
if __name__ == "__main__":
    #main is the name of the file
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

#to work, it should be called this way: 
#   python3 main.py
#if there is an error, for any reason: 
#   uvicorn main:app --port 3000

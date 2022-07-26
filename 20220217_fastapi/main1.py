from typing import Optional
from fastapi import Request, FastAPI
from requests import request
import uvicorn
# import asyncio
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/num")
async def create_item(request : Request):
    var1 = await request.body()
    var1 = json.loads(var1)
    return {"message": var1}

#running fastapi on the port we want
if __name__ == "__main__":
    #main is the name of the file
    uvicorn.run("main1:app", host="127.0.0.1", port=3000, reload=True)

#to work, it should be called this way: 
#   python3 main.py
#if there is an error, for any reason: 
#   uvicorn main1:app --port 3000 --reload

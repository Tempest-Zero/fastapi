from fastapi import FastAPI
from fastapi.params import Body 
app = FastAPI()

@app.get("/root")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data: This is your posts"}

@app.post("/posting")
async def to_post(payLoad : dict = Body(...)):
    print(payLoad)
    return {
        "new_post" : f"name: {payLoad['name']} goal :{payLoad['goal']}"
    }














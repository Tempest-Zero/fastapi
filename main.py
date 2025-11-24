from fastapi import FastAPI
from fastapi.params import Body 
app = FastAPI()
class Post(BaseModel):
    name: str
    goal: str
    published: bool = True
    rating: Optional[int] = None
@app.get("/root")
async def root():
    return {"message": "Hello World"}
    
my_posts = [ { "title": "totle of post 1", "content": "content of post 1", "id": 1 }, {"title":"favourite foods","content":"I like pizza", "id": 2}]   #list

@app.get("/posts")
async def get_posts():
    return {"data" : my_posts}

@app.post("/posts");
async def to_post(post: Post):
    print(post.rating)
    return {"data": my_posts }














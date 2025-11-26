from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel
from random import randrange
app = FastAPI()


class Post(BaseModel):
    name: str
    goal: str
    published: bool = True
    rating: Optional[int] = None
 
my_posts = [ { "title": "title of post 1", "content": "content of post 1", "id": 1 }, {"title":"favourite foods","content":"I like pizza", "id": 2}]   #list
@app.get("/root")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump(); #we are not using databases rn so we will have to generate id from software
                                   #otherwise the database handles ids
    post_dict['id'] = randrange(0,1000000) #selecting from a very large range
                                           #ensures there's a very small probability
                                           #of getting the same number twice
    my_posts.append(post_dict)
    
@app.get("/posts/{id}") #id field represents a path parameter
                        #path parameters will be returned as strings instead of integers
                        #even though they're represented as integers

def get_post(id:int, response: Response):      
    print(id)       
    post = find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"post with id : {id} was not found")
    #  response.status_code = status.HTTP_404_NOT_FOUND
    #  return {'message': f"post with id: {id} was not found"}
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id);
    if index == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist ")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post :Post):
    index = find_index_post(id);
    if index == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist ")
    post_dict = post.model_dump();
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}     

















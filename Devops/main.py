from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello") #@=decorator,/=url
def hello_world(name : str , age : int):
    print("Data-->",name,age)
    return{"Message":f"Hello {name}"}


@app.get("/hello/{name}/{age}") #@=decorator,/=url
def hello_world(name : str , age : int):
    print("Data-->",name,age)
    return{"Message":f"Hello {name}-{age}!"}

# Browse http url in chrome then in url /hello lakhvanu to see output http://127.0.0.1:8000/hello
# Browse http url in chrome then in url /docs lakhvanu to execute like get/post http://127.0.0.1:8000/docs

class PostHello(BaseModel):
    name:str
    age:int

@app.post("/hey") #@=decorator,/=url
def hello_world(posthello:PostHello):
    print("Data-->",posthello)
    return{"Message":f"Hello, {posthello.name}-{posthello.age}!"}
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my api!"}

@app.get("/posts")
def read_posts():
    return {"message": "Here are all the posts"}
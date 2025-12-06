from fastapi import FastAPI 


app = FastAPI()


@app.get("/")
def index():
    return {'message':"Hello, FastAPI!"}



# uvicorn main:app --reload
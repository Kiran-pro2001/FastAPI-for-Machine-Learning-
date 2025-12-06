from fastapi import FastAPI  # from fastapi module, impor the FastAPI class.
from pydantic import BaseModel # for type checking 

# pydantic model 
class User(BaseModel):
    id : int
    name : str 


app = FastAPI()  # create the object of FastAPI Class. 
@app.get("/user", response_model=User)    # response_model is used for mentioning the return should be this data type -- that is User data type. 
def get_user():
    return User(id=1, name="Kiran")    # hardcode we are adding the data 


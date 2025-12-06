from fastapi import FastAPI

app = FastAPI()

# defining the route - end point 
# decorator - app -- app name, get is a method. 
@app.get("/")
def home():
    return {'message': "Hello FastAPI!"}     # we have to return a dictionary - as it gets converted to json 



# when the / endpoint gets hit, automatically the home function gets call, and then it returns the response as json - {'message': "Hello FastAPI!"} 
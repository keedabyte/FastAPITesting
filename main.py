from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a decorator
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a route with path parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

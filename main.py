from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.requests import Request


# Create an instance of the FastAPI class

@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    """Asynchronous context manager for managing the lifespan of a FastAPI application."""
    await startup()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)

async def startup():
    print('starting the server')
    from ultralytics import YOLO
    app.model = YOLO('yolov8m_detect_usdl.pt')


async def shutdown():
    print('shutting down the server')

# Define a route using a decorator
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Define a route with path parameters
@app.get("/predict")
async def read_item(request: Request, image_url: str):

    model = request.app.model

    print('model loaded successfully')

    return {'image_url': image_url}
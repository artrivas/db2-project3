import pickle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from routes.sequential import routes_sequential
from routes.highd import routes_highd
from routes.rtree import routes_rtree

from handlers.SequentialHandler import SequentialHandler
from handlers.RTreeHandler import RTreeHandler
from handlers.HighdHandler import HighdHandler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

handlers: dict = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with open('embeds/collection.pkl', mode='rb') as collection_file:
            collection_data = pickle.load(collection_file)

        handlers['sequential'] = SequentialHandler(collection_data)
        handlers['rtree'] = RTreeHandler(M=5, D=128, collection_data=collection_data)
        handlers['highd'] = HighdHandler(num_bits=1000, D=128, collection_data=collection_data)
        handlers['invidx'] = InvIdxHandler()
        yield

    except Exception as e:
        print(f"Error: {e}")

    finally:
        handlers.clear()

app = FastAPI(lifespan=lifespan)

app.include_router(routes_sequential, prefix="/sequential")
app.include_router(routes_rtree, prefix="/rtree")
app.include_router(routes_highd, prefix="/highd")
app.include_router(routes_highd, prefix="/invidx") #
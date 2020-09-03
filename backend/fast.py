from os import path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from motor_odm import Document
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

from models import Slug, Production, Person
from routers import production, people


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncIOMotorClient(
    "mongodb://192.168.1.3:27017",
    # "mongodb://127.0.0.1:27017",
    serverSelectionTimeoutMS=1000,
    uuidRepresentation="standard",
)
db = client.norloc


@app.on_event("startup")
async def connect_to_mongo():
    # global client
    # print("CONNECTING TO DATABASE")
    # client = AsyncIOMotorClient("")

    Document.use(db)

    await Slug.init_indexes()
    await Production.init_indexes()
    await Person.init_indexes()


@app.exception_handler(ServerSelectionTimeoutError)
async def pymongo_server_selection(
    request: Request,
    exc: ServerSelectionTimeoutError
):
    return JSONResponse(
        status_code=408,
        content={"message": "Could not connect to database"},
    )


@app.get("/media/{file_path:path}")
async def media(file_path: str):
    file_path = path.join("media", file_path)

    if not path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)


app.include_router(production.router, prefix="/productions")
app.include_router(people.router, prefix="/people")

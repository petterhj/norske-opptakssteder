from fastapi import APIRouter, HTTPException, status
from typing import List, Union, Dict
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError, BulkWriteError

from models import Person


router = APIRouter()


@router.get("/")
async def people():
    people = [p async for p in Person.find({})]

    return people


@router.post("/")
async def add_person():
    try:
        p = Person(**{
            "name": "Jens Lien"
        })
        test = await Person.insert(p)

    except DuplicateKeyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )

    return test
import random
from slugify import slugify

from fastapi import APIRouter, HTTPException, status
from typing import List, Union, Dict
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError, BulkWriteError

from models import Slug, Production, ProductionType


router = APIRouter()


@router.get("/")
async def productions(type: ProductionType = None):
    query = {}

    if type:
        query["type"] = type

    try:
        productions = [p async for p in Production.find(
            query
        )]
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors()
        )

    for production in productions:
        print(production)

    return productions


@router.post("/")
async def add_production(data: Production):
    try:
        production = await Production.insert(data)

    except DuplicateKeyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )

    slug = None
    slug_base = production.title
    slug_attempt = 0

    while not slug:
        print("creating slug", slug_base, slug_attempt, slug)
        # if attempts > 3:
        #     raise HTTPException(
        #         status_code=status.HTTP_409_CONFLICT, detail="Could not generate slug"
        #     )

        try:
            slug = await Slug(
                slug=slugify(slug_base, to_lower=True),
                object_id=str(production.id)
            ).insert()
        except DuplicateKeyError as e:
            slug_base = f"{production.title}-{production.year}"
        slug_attempt += 1


    # 
    # print(s)
    

    """
    production = await Production.find_one({"slug": "budbringeren"})
    print(production.id, type(production.id))

    
    # print(s.object_id)

    production = await Production.find_by_id(s.object_id)
    print(production)
    """
    # return production
    return production
    # return s#.json()

"""
async def add_production(data: Union[Production, List[Production]]):
    if isinstance(data, list):
        try:
            await Production.insert_many(*data, ordered=False)

        except BulkWriteError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=[
                    er["errmsg"] for er in e.details.get('writeErrors', [])
                ]
            )

    try:
        await Production.insert(data)

    except DuplicateKeyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )

    return data
"""


@router.get("/{slug}")
async def production(slug: str):
    # productions = [str(p.slug) async for p in Production.find()]
    # print(slug)
    # print(productions)

    slug = await Slug.find_one({"slug": slug})
    production = await Production.find_by_id(slug.object_id)
    """
    print(production)

    if not production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Production not found",
        )

    return production
    """
    return production


@router.put("/{slug}")
async def update_production(slug: str, data: Dict):
    try:
        production = await Production.find_one({"slug": slug})
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors()
        )


    if not production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Production not found",
        )

    try:
        updated = Production(**production.copy(update=data).dict())
        await updated.save()

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors()
        )
    except DuplicateKeyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )

    return updated

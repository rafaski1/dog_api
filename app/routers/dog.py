from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Optional

from app.schemas import Dog, Output
from app.enums import Gender
from app.redis_operations import get, store, delete

router = APIRouter()

REDIS_KEY = "dogs"


@router.get("/get", response_model=Output)
async def get_dog(
    request: Request,
    name: Optional[str] = None,
    breed: Optional[str] = None,
    age: Optional[int] = None,
    gender: Optional[Gender] = None,
    city: Optional[str] = None,
    country: Optional[str] = None
):
    all_dogs = get(key=REDIS_KEY)
    if all_dogs is None:
        return Output(success=False, message="No dogs")
    else:
        input_query = dict(request.query_params)
        matching_dogs = []
        for dog in all_dogs:

            # condition_results = []
            # for k, v in input_query.items():
            #     condition_results.append(dog[k] == v)
            # if False not in condition_results:
            #     matching_dogs.append(dog)

            if all([
                dog[k] == v for k, v in input_query.items()
            ]):
                matching_dogs.append(dog)

    return Output(success=True, results=matching_dogs)


@router.get("/get_all", response_model=Output)
async def get_all_dogs(request: Request) -> JSONResponse:
    all_dogs = get(key=REDIS_KEY)
    output = Output(success=True, results=all_dogs)
    return JSONResponse(
        content=output.dict(),
    )


@router.post("/add", response_model=Output)
async def add(request: Request, dog: Dog):
    new_dog = dog.to_dict()
    all_dogs = get(key=REDIS_KEY)
    if all_dogs is None:
        store(key=REDIS_KEY, value=[new_dog])
    else:
        if new_dog not in all_dogs:
            all_dogs.append(new_dog)
            store(key=REDIS_KEY, value=all_dogs)
    return Output(success=True, results=all_dogs)


@router.delete("/delete", response_model=Output)
async def delete_dog(request: Request, dog: Dog):
    all_dogs = get(key=REDIS_KEY)
    if all_dogs is not None:
        all_dogs.remove(dog.dict())
        if not all_dogs:
            delete(key=REDIS_KEY)
        else:
            store(key=REDIS_KEY, value=all_dogs)
    return Output(success=True, results=all_dogs)


@router.delete("/delete_all", response_model=Output)
async def delete_all(request: Request):
    delete(key=REDIS_KEY)
    return Output(success=True)


@router.put("/update/{dog_id}", response_model=Output)
async def update_dog(request: Request, dog_id: str, updated_dog: Dog):
    all_dogs = get(key=REDIS_KEY)
    if all_dogs is not None:
        for dog in all_dogs:
            if dog["id"] == dog_id:
                dog.update(updated_dog)
                store(key=REDIS_KEY, value=all_dogs)
                break
    return Output(success=True, results=all_dogs)

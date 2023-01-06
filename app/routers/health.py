import redis
from fastapi import APIRouter

from app.redis_operations import ping
from app.schemas import Output

router = APIRouter()


@router.get("/ping", response_model=Output)
async def health_check():
    try:
        if ping():
            return Output(success=True, message="Pong")
    except redis.ConnectionError:
        return Output(success=False, message="Raised connection error")

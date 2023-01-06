import redis
import json
from typing import List, Any, NoReturn

from app.settings import REDIS_PORT, REDIS_HOST

redis_connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


def get(key: str) -> Any:
    results = redis_connection.get(key)
    if results is not None:
        results = json.loads(results)
    return results


def store(key: str, value: List[dict]) -> None:
    redis_connection.set(name=key, value=json.dumps(value))


def delete(key: str) -> None:
    redis_connection.delete(key)


def ping() -> bool | NoReturn:
    return redis_connection.ping()

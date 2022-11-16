import redis
import json
from typing import List, Any, NoReturn

redis_connection = redis.Redis(host="127.0.0.1", port=6379)


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

#!/usr/bin/env python3
"""import libraries"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Writing Data to Redis"""
    def __init__(self):
        """init the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """take data argument and return key"""
        random_key: str = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Callable = None) -> Union[str, float, bytes, int, None]:
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
        else:
            None

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=str)
    
    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)

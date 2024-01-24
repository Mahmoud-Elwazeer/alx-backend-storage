#!/usr/bin/python3
"""import libraries"""
import redis
import uuid
from typing import Union


class Cache:
    """Writing Data to Redis"""
    def __init__(self):
        """init class"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """take data argument and return key"""
        self.key: str = str(uuid.uuid4())
        if (isinstance(data, (str, bytes))):
            self._redis.set(self.key, data)
        elif (isinstance(data, (int, float))):
            self._redis(self.key, str(data))

        return self.key

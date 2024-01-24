#!/usr/bin/python3
"""import libraries"""
import redis
import uuid
from typing import Union


class Cache:
    """Writing Data to Redis"""
    def __init__(self):
        """init class"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """take data argument and return key"""
        random_key: str = str(uuid.uuid4())
        # if (isinstance(data, (str, bytes))):
        #     self._redis.set(key, data)
        # elif (isinstance(data, (int, float))):
        #     self._redis(key, str(data))

        self._redis.set(random_key, data)

        return random_key

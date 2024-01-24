#!/usr/bin/env python3
"""import libraries"""
import redis
import uuid
from typing import Union


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

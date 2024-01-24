#!/usr/bin/python3
"""import libraries"""
import redis
import uuid
from typing import Any


class Cache():
    """Writing Data to Redis"""
    def __init__(self):
        """init class"""
        self._redis: redis.StrictRedis = redis.Redis()
        self._redis.flushdb

    def store(self, data: [str, float, bytes, int]) -> str:
        """take data argument and return key"""
        self.key: str = str(uuid.uuid4())
        self._redis.set(self.key, data)

        return self.key

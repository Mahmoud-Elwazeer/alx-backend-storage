#!/usr/bin/env python3
"""import libraries"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    "define decorator  how many times methods of the Cache class"
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper function"""
        # Increment the count for the qualified name of the method
        key = method.__qualname__
        self._redis.incr(key)
        # Increment the overall call count for the instance
        wrapper.calls += 1
        return method(self, *args, **kwds)
    wrapper.calls = 0
    return wrapper


def call_history(method: Callable) -> Callable:
    """define decorator to add to list inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.rpush("{}:inputs".format(method.__qualname__), *args)
        key = method(self, *args, **kwds)
        self._redis.rpush("{}:outputs".format(method.__qualname__), key)
        return key
    return wrapper


class Cache:
    """Writing Data to Redis"""
    def __init__(self):
        """init the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, float, bytes, int]) -> str:
        """take data argument and return key"""
        random_key: str = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Callable = None) -> Union[
                        str, float, bytes, int, None]:
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
            else:
                return value
        else:
            None

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=str)

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)

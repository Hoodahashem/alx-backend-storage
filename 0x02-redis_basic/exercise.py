#!/usr/bin/env python3
"""
redis module
"""
import redis
from uuid import uuid4
from typing import Callable, Union, Optional


class Cache:
    """
    cache class to work with redis
    """

    def __init__(self) -> None:
        """initialize the class with creating the redis client"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store function to store the data in the redis Client"""
        key = str(uuid4())
        self.__redis.set(key, data)
        return key

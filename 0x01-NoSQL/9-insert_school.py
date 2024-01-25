#!/usr/bin/env python3
"""import libraries"""


def insert_school(mongo_collection, **kwargs):
    """new document in a collection based on kwargs"""
    elemnt = {**kwargs}
    id = mongo_collection.insert_one(elemnt).inserted_id
    return id

#!/usr/bin/env python3
"""ist of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """search in collection depend on topic"""
    return mongo_collection.find({'topics': topic})

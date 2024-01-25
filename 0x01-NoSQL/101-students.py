#!/usr/bin/env python3
"""import libraries"""
from pymongo import DESCENDING

def top_students(mongo_collection):
    """returns all students sorted by average score"""
    get_all = mongo_collection.find()

    for i in get_all:
        topics = i.get("topics")
        average = 0
        for j in topics:
            average += j.get('score')
        mongo_collection.update_many(
            i,
            {'$set':{
                'averageScore': average / len(topics)
            }})
    
    out = mongo_collection.find().sort('averageScore', DESCENDING)
    return out

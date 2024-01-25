#!/usr/bin/env python3
"""import libraries"""
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client.logs
col = db.nginx

all_logs = col.estimated_document_count()
print("{} logs".format(all_logs))

print("Methods:")

method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for i in method:
    num_methods = col.count_documents({'method': i})
    print('\tmethod {}: {}'.format(i, num_methods))

#!/usr/bin/env python3
"""list all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Return a list of docs if not empty"""
    result = mongo_collection.school.find()
    if result:
        return result
    return []

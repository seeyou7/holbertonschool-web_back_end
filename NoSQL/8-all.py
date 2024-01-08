#!/usr/bin/env python3
""" fuc to list all doc in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """ return list of doc or emty list if no doc"""
    result = mongo_collection.school.find()
    if result:
        return result
    return []

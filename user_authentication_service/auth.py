#!/usr/bin/env python3
"""
    the auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with a randomly-generated salt
    and returns the salted, hashed password.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

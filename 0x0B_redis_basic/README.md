# Redis Basics

![Flowchart of Redis Python Tasks](image/flowchart.webp)

This repository covers the fundamentals of Redis using Python. Redis is an in-memory data structure store often used as a cache or message broker. Through the tasks in this repository, you will learn how to perform basic operations with Redis, leverage it as a cache, and create a robust data management system with Redis commands and decorators in Python.

---

## Tasks

### 0 - Writing Strings to Redis
**Purpose**: Create a `Cache` class to store arbitrary data in Redis.
**Description**: Initializes a Redis client instance and flushes the database. The `store` method allows for storing data with a randomly generated key, making Redis useful for caching and quick data storage.

### 1 - Reading from Redis and Recovering Original Type
**Purpose**: Retrieve and convert stored data to its original format.
**Description**: Implements a `get` method that accepts a conversion function (`fn`) to decode Redis data into its original type, along with `get_str` and `get_int` for automatic conversion. This ensures data consistency when using Redis as a cache.

### 2 - Incrementing Values
**Purpose**: Track how many times certain methods are called.
**Description**: Uses the Redis `INCR` command to count method calls with a `count_calls` decorator. This enables function call tracking, which is useful for monitoring and analytics within applications.

### 3 - Storing Lists
**Purpose**: Store input and output history for specific functions.
**Description**: Defines a `call_history` decorator to record inputs and outputs of a function using Redis lists (`RPUSH` and `LPUSH`). This allows tracking of function call history, which is helpful for debugging and understanding usage patterns.

### 4 - Retrieving Lists
**Purpose**: Display the history of calls for a specific function.
**Description**: Implements a `replay` function that retrieves and displays the input/output history for a function, using data stored from previous tasks. This functionality is useful for auditing and tracking usage over time.

---

## Resources

- **Redis Commands**: Core Redis commands that power data storage and manipulation.
- **Redis Python Client**: How to connect and interact with Redis using Python.
- **Using Redis as a Cache**: Techniques for leveraging Redis as an efficient, temporary data store.

---

### Requirements

- **Environment**: Ubuntu 20.04 LTS, Python 3.9
- **Code Style**: Pycodestyle 2.5 for maintaining readable, consistent code.
- **Documentation**: Modules, classes, functions, and methods must include detailed docstrings.

This README provides a structured guide for using Redis with Python, focusing on data storage, retrieval, and monitoring in a caching context.

Developed by Younes SABER[https://github.com/seeyou7]
# Caching Algorithms Project

## Background Context
In this project, you will learn about different caching algorithms and implement them in Python.

## Resources
Here are some useful resources to read or watch before starting:
- **Cache replacement policies - FIFO**: Learn about First-In, First-Out caching policy.
- **Cache replacement policies - LIFO**: Learn about Last-In, First-Out caching policy.
- **Cache replacement policies - LRU**: Learn about Least Recently Used caching policy.
- **Cache replacement policies - MRU**: Learn about Most Recently Used caching policy.
- **Cache replacement policies - LFU**: Learn about Least Frequently Used caching policy.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:
- What a caching system is
- The definitions of FIFO, LIFO, LRU, MRU, and LFU
- The purpose of a caching system
- The limitations of a caching system

## Requirements

### Python Scripts
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.9)**.
- All files must end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project is mandatory.
- Code must follow the **pycodestyle** style guide (version 2.5).
- All files must be executable.
- File lengths will be tested using `wc`.
- All modules should have documentation (using `__doc__`).
- All classes and functions (inside and outside a class) should have documentation explaining their purpose.

### BaseCaching Class
All caching classes must inherit from the `BaseCaching` class. The `BaseCaching` class provides:
- A constant `MAX_ITEMS = 4` representing the maximum number of items that can be stored in the cache.
- A dictionary `cache_data` to store the cached data.
- Methods `put()` and `get()` which must be implemented in child classes.

Here is an example of `BaseCaching`:

```python
#!/usr/bin/python3
""" BaseCaching module """

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data is stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache data """
        self.cache_data = {}

    def print_cache(self):
        """ Print the current cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")


# Caching System Project

## Tasks

### 0. Basic Dictionary Cache (BasicCache)
Create a class `BasicCache` that inherits from `BaseCaching` and implements a caching system with no limit. The `put()` method is responsible for adding items to the cache, while the `get()` method retrieves items by their key. If the provided key or item is `None`, the method should do nothing.

**File:** `0-basic_cache.py`

### 1. FIFO Caching (FIFOCache)
Create a class `FIFOCache` that inherits from `BaseCaching`. This class implements the **FIFO (First-In, First-Out)** caching system, where the oldest item is removed from the cache once it exceeds the limit specified by `MAX_ITEMS`.

**File:** `1-fifo_cache.py`

### 2. LIFO Caching (LIFOCache)
Create a class `LIFOCache` that inherits from `BaseCaching`. This class implements the **LIFO (Last-In, First-Out)** caching system, where the most recently added item is removed from the cache when the cache exceeds the `MAX_ITEMS` limit.

**File:** `2-lifo_cache.py`

### 3. LRU Caching (LRUCache)
Create a class `LRUCache` that inherits from `BaseCaching`. This class implements the **LRU (Least Recently Used)** caching system, where the least recently accessed item is discarded when the cache is full and exceeds the `MAX_ITEMS` limit.

**File:** `3-lru_cache.py`

### 4. MRU Caching (MRUCache)
Create a class `MRUCache` that inherits from `BaseCaching`. This class implements the **MRU (Most Recently Used)** caching system, where the most recently accessed item is removed when the cache exceeds its `MAX_ITEMS` limit.

**File:** `4-mru_cache.py`

---

## Repository
- GitHub repository: `holbertonschool-web_back_end`
- Directory: `caching`
Younes SABER
#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system that follows FIFO rule """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()  # Call the parent class's constructor
        self.cache_order = []  # List to maintain the insertion order

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # Add the item in the cache
        if key not in self.cache_data:
            self.cache_order.append(key)
        self.cache_data[key] = item

        # If the cache exceeds the max size, remove the first item (FIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first item added (FIFO)
            first_key = self.cache_order.pop(0)
            # Remove the first item from the cache
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

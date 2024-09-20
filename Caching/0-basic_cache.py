#!/usr/bin/python3
"""    
    BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ 
        BasicCache defines a caching system that has no limit on items stored
    """

    def put(self, key, item):
        """ 
            Add an item in the cache
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ 
            Get an item by key
            If key is None or if the key doesn’t
            exist in self
            cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

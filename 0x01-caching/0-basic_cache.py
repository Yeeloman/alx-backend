#!/usr/bin/env python3
"""task 0"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key) if key else None

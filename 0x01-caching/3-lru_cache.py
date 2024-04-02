#!/usr/bin/env python3
"""task 3"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.checked = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.checked.pop(0)
                self.cache_data.pop(lru_key)
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.checked.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.checked.remove(key)
            self.checked.append(key)

            return self.cache_data.get(key)

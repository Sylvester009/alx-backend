#!/usr/bin/env python3

"""
LIFO cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class that inherits from Base Caching
    """

    def __init__(self):
        """ Initialize LIFO Cache
        """
        super().__init__()
        self.caches = []

    def put(self, key, item):
        """ Add an item in the cache following LIFO """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.caches.pop()  # discard last item (LIFO)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.caches.append(key)
        self.cache_data[key] = item  # assign item to key in cache_data

    def get(self, key):
        """
        Get an item by key and
        Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

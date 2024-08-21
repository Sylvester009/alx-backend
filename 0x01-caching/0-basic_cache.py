#!/usr/bin/python3
"""Basic Cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache class that inherits from Base Caching
    """

    def __init__(self):
        """Initialize BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        If key is None or key does not exist in cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

#!/usr/bin/env python3

"""
MRU cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class that inherits from Base Caching
    """

    def __init__(self):
        """ Initialize MRU Cache """
        super().__init__()
        self.caches = []  # List to maintain the order of keys (MRU)

    def put(self, key, item):
        """ Add an item in the cache following MRU """
        if key is None or item is None:
            return

        """If the key is already in cache,
        update it and move it to the end of the list
        """
        if key in self.caches:
            self.caches.remove(key)

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.caches.pop(-1)  # Discard the MRU
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new key to the cache and mark it as recently used
        self.caches.append(key)
        self.cache_data[key] = item  # Assign item to key in cache_data

    def get(self, key):
        """ Get an item by key following MRU """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the list (most recently used)
        self.caches.remove(key)
        self.caches.append(key)

        return self.cache_data.get(key)

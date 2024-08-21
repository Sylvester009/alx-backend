#!/usr/bin/env python3

"""
LRU cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache class that inherits from Base Caching
    """

    def __init__(self):
        """ Initialize LRU Cache
        """
        super().__init__()
        self.caches = []

    def put(self, key, item):
        """ Add an item in the cache following LRU """
        if key is None or item is None:
            return

        # If the key is already in cache, update it and move it to the end of the list
        if key in self.caches:
            self.caches.remove(key)

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.caches.pop(0)  # Discard the least recently used item (LRU)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new key to the cache and update its position
        self.caches.append(key)
        self.cache_data[key] = item  # Assign item to key in cache_data

    def get(self, key):
        """ Get an item by key following LRU """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the list (most recently used)
        self.caches.remove(key)
        self.caches.append(key)
        
        return self.cache_data.get(key)

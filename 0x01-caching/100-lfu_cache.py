#!/usr/bin/env python3

"""
LFU cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize LFU Cache """
        super().__init__()
        self.freqs = {}  # To store frequencies of items
        self.timestamps = []  # To track insertion order for LRU when frequencies are tied

    def put(self, key, item):
        """ Add an item in the cache following LFU """
        if key is None or item is None:
            return

        # If the key is already in the cache, update its value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freqs[key] += 1
            self.timestamps.remove(key)  # Update position in timestamps for LRU
            self.timestamps.append(key)  # Reinsert to end to mark it as recently used
        else:
            # Check if cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the key with the lowest frequency
                min_freq = min(self.freqs.values())
                # Collect all keys with the minimum frequency
                lfu_keys = [k for k, v in self.freqs.items() if v == min_freq]

                # If multiple LFU keys exist, use LRU to remove the oldest
                if len(lfu_keys) > 1:
                    for k in self.timestamps:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                # Remove the least frequently used (or least recently used) key
                del self.cache_data[lfu_key]
                del self.freqs[lfu_key]
                self.timestamps.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new key to the cache and initialize its frequency
            self.cache_data[key] = item
            self.freqs[key] = 1
            self.timestamps.append(key)  # Track insertion order

    def get(self, key):
        """ Get an item by key following LFU """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and timestamps
        self.freqs[key] += 1
        self.timestamps.remove(key)  # Update position in timestamps for LRU
        self.timestamps.append(key)  # Reinsert to end to mark it as recently used

        return self.cache_data.get(key)

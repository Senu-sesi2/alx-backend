#!/usr/bin/env python3
"""
Basic caching module.
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Basic caching system without a limit.
    Inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        Args:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            # Assign the item value for the given key in the cache_data dictionary
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Args:
            key (str): The key to look for in the cache.
        Returns:
            The value in self.cache_data linked to key, or None if key is None or not found.
        """
        if key is None:
            # If the key is None, return None
            return None
        # Return the value linked to the key, or None if the key doesn't exist in cache_data
        return self.cache_data.get(key)


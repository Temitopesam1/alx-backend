#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A caching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item is not None:
            self.cache_data[key] = item
        return

    def get(self, key):
        """ Get an item by key
        """
        try:
            return self.cache_data[key]
        except Exception:
            return None

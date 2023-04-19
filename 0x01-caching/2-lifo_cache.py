#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A caching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item is not None:
            if (key not in self.cache_data.keys()) and \
                    (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                print(f'DISCARD: {list(self.cache_data)[-1]}')
                self.cache_data.popitem()
            self.cache_data[key] = item
        return

    def get(self, key):
        """ Get an item by key
        """
        try:
            return self.cache_data[key]
        except Exception:
            return None

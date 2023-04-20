#!/usr/bin/python3
""" LRUCache module """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A Caching System
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if (key not in self.cache_data.keys()) and \
                    (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                print(f'DISCARD: {list(self.cache_data)[-1]}')
                self.cache_data.popitem()
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        return

    def get(self, key):
        """ Get an item by key
        """
        try:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        except Exception:
            return None

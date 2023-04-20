#!/usr/bin/python3
"""LFU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system
    """
    def __init__(self):
        super().__init__()
        self.freq_dict = {}
        self.age = 1

    def update(self, dictionary, key):
        """ Update dictionary
        """
        if key not in dictionary.keys():
            dictionary[key] = 1
        else:
            dictionary[key] += 1

    def least_used_key(self, dictionary):
        """ Get least used key in dictionary
        """
        value_list = sorted(dictionary.values())

        for key, value in dictionary.items():
            if value == value_list[0]:
                return key

    def key_to_remove(self, key):
        """ Remove an item by key
        """
        print(f'DISCARD: {key}')
        self.cache_data.pop(key)
        self.freq_dict.pop(key)

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if (key not in self.cache_data.keys()) and \
                    (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                least_frequence = self.least_used_key(self.freq_dict)
                self.key_to_remove(least_frequence)
            self.cache_data[key] = item
            self.update(self.freq_dict, key)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys():
            self.update(self.freq_dict, key)
            return self.cache_data[key]
        else:
            return None

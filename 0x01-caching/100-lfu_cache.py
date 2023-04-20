#!/usr/bin/python3
"""LFU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system
    """
    def __init__(self):
        super().__init__()
        self.age_dict = {}
        self.freq_dict = {}
        self.age = 1
    
    def update(self, dict1, dict2, key):
        dict1[key] = self.age
        self.age += 1
        if key not in dict2.keys():
            dict2[key] = 1
        else:
            dict2[key] += 1
        
        
    def least_used_key(self, dictionary):
        value_list = sorted(dictionary.values())
        
        for key, value in dictionary.items():
            if value == value_list[0]:
                return key
    
    def key_to_remove(self, key):
        print(f'DISCARD: {key}')
        self.cache_data.pop(key)
        self.age_dict.pop(key)
        self.freq_dict.pop(key)
        
        
    def put(self, key, item):
        if key and item:
            
        
            if (key not in self.cache_data.keys()) and (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            
                least_recently = self.least_used_key(self.age_dict)
                least_frequently = self.least_used_key(self.freq_dict)
                
                if least_recently == least_frequently:
                    self.key_to_remove(least_recently)
                else:
                    least_val = min(self.freq_dict[least_frequently], self.age_dict[least_recently])
                    if self.freq_dict[least_frequently] == least_val:
                        self.key_to_remove(least_frequently)
                    else:
                        self.key_to_remove(least_recently)

                
            self.cache_data[key] = item
            self.update(self.age_dict, self.freq_dict, key)
            # print ('LRU', self.age_dict)
            # print('LFU', self.freq_dict)
        
        
        
    def get(self, key):
        if key and key in self.cache_data.keys():
            self.update(self.age_dict, self.freq_dict, key)
            # print ('LRU', self.age_dict)
            # print('LFU', self.freq_dict)
            return self.cache_data[key]
        else:
            return None

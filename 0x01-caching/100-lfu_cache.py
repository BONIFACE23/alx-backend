#!/usr/bin/python3
""" LFUCache module
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.lfu_data = {}

    def __pop(self):
        """discard the least frequency used item"""
        keys = {}
        k = ''
        for key, val in self.lfu_data.items():
            if len(keys) == 0:
                k = key
            if self.lfu_data[k][0] > val[0]:
                keys.pop(k)
                k = key
            if self.lfu_data[k][0] == val[0]:
                keys[k] = val[1]
        if len(keys) > 1:
            k = min(keys, key=keys.get)
        print("DISCARD:", k)
        self.lfu_data.pop(k)
        self.cache_data.pop(k)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if key not in self.lfu_data.keys():
                self.__pop()
            else:
                print("DISCARD:", key)
        if key not in self.lfu_data.keys():
            self.lfu_data[key] = [0, datetime.now()]
        else:
            self.get(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.lfu_data.keys():
            self.lfu_data[key][0] += 1
            self.lfu_data[key][1] = datetime.now()
        return self.cache_data.get(key)

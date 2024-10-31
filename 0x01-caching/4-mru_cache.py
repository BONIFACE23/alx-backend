#!/usr/bin/python3
""" MRUCache module
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.mru_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k = max(self.mru_data, key=self.mru_data.get)
            print("DISCARD:", k)
            self.mru_data.pop(k)
            self.cache_data.pop(k)
        self.mru_data[key] = datetime.now()

    def get(self, key):
        """ Get an item by key
        """
        if key in self.mru_data.keys():
            self.mru_data[key] = datetime.now()
        return self.cache_data.get(key)

#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k = self.keys.pop(0)
            print("DISCARD:", k)
            self.cache_data.pop(k)
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

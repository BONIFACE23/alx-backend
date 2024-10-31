#!/usr/bin/python3
""" BaseCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

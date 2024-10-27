#!/usr/bin/env python3
""" Model for index_range function and class  Server"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Return a tuple of size two containing a start index
    and an end index of page """
    end_idx: int = page_size * page
    start_idx: int = end_idx - page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """inisialaize data"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a list based on page and page_size"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        self.dataset()
        if end_idx > len(self.__dataset):
            return []
        return self.__dataset[start_idx:end_idx]

#!/usr/bin/env python3
""" Model for index_range function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Return a tuple of size two containing a start index
    and an end index of page """
    end_idx: int = page_size * page
    start_idx: int = end_idx - page_size
    return (start_idx, end_idx)

#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ define type-annotated function sum_mixed_list"""
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum

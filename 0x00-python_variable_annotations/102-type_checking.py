#!/usr/bin/env python3
"""
This module provides a function to safely get
a value from a dictionary.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of the input tuple by repeating each
    element a given number of times.

    Args:
        lst (Tuple): The input tuple to be zoomed in.
        factor (int): The number of times each element in the tuple should
        be repeated. Default is 2.

    Returns:
        List: A list containing the elements of the input tuple
        repeated by the given factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

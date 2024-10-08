#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string to be used as the first element of the tuple.
        v (Union[int, float]): The number to be squared and used as
        the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the input
        string and the square of the input number.
    """
    return (k, float(v ** 2))

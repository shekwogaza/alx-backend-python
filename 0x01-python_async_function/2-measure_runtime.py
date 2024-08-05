#!/usr/bin/env python3
"""
This module provides a function to measure the execution time of the wait_n coroutine.
"""

import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay to be used in wait_n.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    
    return total_time / n

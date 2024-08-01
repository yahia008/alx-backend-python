#!/usr/bin/env python3
"""Module for Task 8."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Defines a function for multiplying numbers.
    """
    return lambda x: x * multiplier

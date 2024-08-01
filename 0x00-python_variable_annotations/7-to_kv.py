#!/usr/bin/env python3
"""Module for Task 7."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Transforms a key and its corresponding value into a
    tuple containing the key and the square of the value.
    """
    return (k, float(v**2))

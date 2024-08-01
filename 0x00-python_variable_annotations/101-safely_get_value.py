#!/usr/bin/env python3
"""Module for Task 11.
More involved type annotations"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary.
    Returns: The value from the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default

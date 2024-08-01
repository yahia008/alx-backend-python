#!/usr/bin/env python3
"""Module for Task 10.
Duck typing - first element of a sequence
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the initial element of a list
    or `None` if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

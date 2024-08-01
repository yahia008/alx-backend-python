#!/usr/bin/env python3
"""Module for Task 9."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the total number of elements in a list of sequences.
    """
    return [(i, len(i)) for i in lst]

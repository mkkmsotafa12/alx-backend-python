#!/usr/bin/env python3
""" Basic annotations - to string """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples of sequence and length """
    return [(i, len(i)) for i in lst]

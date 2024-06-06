#!/usr/bin/env python3
""" type annotations tasks """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return function """
    def addMultiplier(value: float):
        """ nested function """
        return value * multiplier
    return addMultiplier

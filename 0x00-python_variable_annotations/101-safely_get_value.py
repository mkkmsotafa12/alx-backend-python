#!/usr/bin/env python3
""" safely get value """
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Return value of key if it exists, otherwise return default """
    if key in dct:
        return dct[key]
    else:
        return default

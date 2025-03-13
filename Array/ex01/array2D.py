import numpy as np


def error_check(lst: list, start: int, end: int):
    """function that raise exception if assertion of type is not ok"""
    if not isinstance(lst, list):
        raise AssertionError("Assertion error : not a list")
    if not isinstance(start, int):
        raise AssertionError("Assertion error : not an int")
    if not isinstance(end, int):
        raise AssertionError("Assertion error : not an int")


def slice_me(family: list, start: int, end: int) -> list:
    """function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided
    start and end arguments"""
    try:
        error_check(family, start, end)
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        res = np.array(family)[start:end]
        print(f"My new shape is : ({len(res)}, {len(res[0])})")
        return res
    except Exception as e:
        print(e)

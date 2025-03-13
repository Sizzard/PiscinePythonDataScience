def calulcate_bmi(height: int, weight: float) -> int | float:
    """function to calculate bmi"""
    return weight / pow(height, 2)


def error_check(lst: list[int | float]):
    """function that raise exception if assertion of type is not ok"""
    if not isinstance(lst, list):
        raise AssertionError("Assertion error : not a list")
    for i in lst:
        if not isinstance(i, int) and not isinstance(i, float):
            raise AssertionError("Assertion error : not a valid type of lst")


def give_bmi(
        height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """function to give bmi"""
    try:
        error_check(height)
        error_check(weight)
        if len(height) != len(weight):
            raise AssertionError("Assertion error : lists not the same size")
        idx = 0
        res = []
        while idx < len(height):
            res.append(calulcate_bmi(height[idx], weight[idx]))
            idx += 1
        return res
    except Exception as e:
        print(e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """function to apply limit"""
    try:
        error_check(bmi)
        res = []
        for item in bmi:
            if item > limit:
                res.append(True)
            else:
                res.append(False)
        return res
    except Exception as e:
        print(e)

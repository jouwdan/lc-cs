"""Reference for the original course mock; not an SEC starter or solution file."""
import math
from numbers import Real


def valid_number(value):
    return isinstance(value, Real) and not isinstance(value, bool) and math.isfinite(value)


def analyse(readings, threshold):
    if not valid_number(threshold) or any(not valid_number(value) for value in readings):
        raise ValueError("readings and threshold must be finite real numbers, excluding booleans")
    count = len(readings)
    total = sum(readings)
    qualifying = current_run = best_run = 0
    # Consecutive runs depend on the original order, so do not sort this traversal.
    for value in readings:
        if value >= threshold:
            qualifying += 1
            current_run += 1
            best_run = max(best_run, current_run)
        else:
            current_run = 0
    ordered = sorted(readings)
    if not count:
        median = None
    elif count % 2:
        median = ordered[count // 2]
    else:
        median = (ordered[count // 2 - 1] + ordered[count // 2]) / 2
    return {"count": count, "mean": total / count if count else None,
            "at_or_above": qualifying, "longest_run": best_run, "median": median}


def self_check():
    assert analyse([], 22) == {"count": 0, "mean": None, "at_or_above": 0, "longest_run": 0, "median": None}
    source = [18, 21, 23, 24, 19, 25]
    result = analyse(source, 22)
    assert result == {"count": 6, "mean": 130 / 6, "at_or_above": 3, "longest_run": 2, "median": 22}
    assert source == [18, 21, 23, 24, 19, 25]
    assert analyse([1, 5, 6, 7], 5)["longest_run"] == 3
    assert analyse([5, 5, 1, 5], 5)["at_or_above"] == 3
    assert analyse([5, 5, 1, 5], 5)["longest_run"] == 2
    assert analyse([9, 1, 3], 2)["median"] == 3
    for readings, threshold in [([2, "bad"], 1), ([True], 1), ([float("inf")], 1), ([1], "bad"), ([1], float("nan"))]:
        try:
            analyse(readings, threshold)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid numeric input accepted")


if __name__ == "__main__":
    self_check()
    print(analyse([18, 21, 23, 24, 19, 25], 22))

"""Original Topic 08 algorithms; each sort preserves its input."""
import math
import random


def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target):
    """Precondition: values are ascending; return any match or -1."""
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def search_probes(values, target, binary=False):
    """Count inspected items, not every low-level comparison."""
    probes = 0
    if not binary:
        for value in values:
            probes += 1
            if value == target:
                break
        return probes
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        probes += 1
        if values[middle] == target:
            break
        if target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return probes


def bubble_sort(values):
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        changed = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                changed = True
        if not changed:
            break
    return result


def selection_sort(values):
    result = values.copy()
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        result[start], result[smallest] = result[smallest], result[start]
    return result


def insertion_sort(values):
    result = values.copy()
    for index in range(1, len(result)):
        item = result[index]
        position = index - 1
        while position >= 0 and result[position] > item:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = item
    return result


def quicksort(values):
    if len(values) <= 1:
        return values.copy()
    pivot = values[len(values) // 2]
    smaller = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    larger = [value for value in values if value > pivot]
    return quicksort(smaller) + equal + quicksort(larger)


def factorial(number):
    if type(number) is not int or number < 0:
        raise ValueError("Factorial needs a non-negative integer")
    if number == 0:
        return 1
    return number * factorial(number - 1)


def gcd_iterative(a, b):
    if type(a) is not int or type(b) is not int:
        raise ValueError("GCD needs integer arguments")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if type(a) is not int or type(b) is not int:
        raise ValueError("GCD needs integer arguments")
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def winning_position(counters):
    """Remove 1 or 2; taking the final counter wins. Small teaching inputs."""
    if type(counters) is not int or counters < 0:
        raise ValueError("Use a non-negative whole counter count")
    if counters == 0:
        return False
    # shortcut: recursion repeats states, use the derived rule or memoisation for large games.
    return any(not winning_position(counters - move) for move in (1, 2) if move <= counters)


def fibonacci_terms(count):
    """Return count terms, using the lesson's one-indexed 1, 1 starting pair."""
    if type(count) is not int or count < 0:
        raise ValueError("Term count must be a non-negative integer")
    result = []
    previous, current = 1, 1
    for _ in range(count):
        result.append(previous)
        previous, current = current, previous + current
    return result


def self_check():
    rng = random.Random(42)
    cases = [[], [4], [1, 2, 3], [3, 2, 1], [4, 4, 4], [7, 2, 5, 1, 5], [-3, 0, -3]]
    cases += [[rng.randrange(-10, 11) for _ in range(20)] for _ in range(15)]
    for original in cases:
        before = original.copy()
        for sort in [bubble_sort, selection_sort, insertion_sort, quicksort]:
            assert sort(original) == sorted(original)
            assert original == before
        ordered = sorted(original)
        for target in range(-12, 13):
            linear = linear_search(original, target)
            assert linear == (original.index(target) if target in original else -1)
            binary = binary_search(ordered, target)
            if target in ordered:
                assert 0 <= binary < len(ordered) and ordered[binary] == target
            else:
                assert binary == -1
    assert binary_search([3, 7, 11, 18, 23, 31, 42], 23) == 4
    assert binary_search([3, 7, 11, 18, 23, 31, 42], 24) == -1
    assert [search_probes(list(range(n)), n + 1, True) for n in [8, 16, 32]] == [4, 5, 6]
    assert [search_probes(list(range(n)), n + 1) for n in [8, 16, 32]] == [8, 16, 32]
    assert factorial(0) == 1 and factorial(4) == 24
    for a in range(-20, 21):
        for b in range(-20, 21):
            assert gcd_iterative(a, b) == gcd_recursive(a, b) == math.gcd(a, b)
    assert [winning_position(n) for n in range(10)] == [n % 3 != 0 for n in range(10)]
    for call in [lambda: factorial(-1), lambda: gcd_iterative(1.5, 2), lambda: gcd_recursive(1, "2"), lambda: winning_position(-1)]:
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid argument accepted")
    assert fibonacci_terms(0) == []
    assert fibonacci_terms(1) == [1]
    assert fibonacci_terms(2) == [1, 1]
    assert fibonacci_terms(8) == [1, 1, 2, 3, 5, 8, 13, 21]
    a, b = 1, 0
    totals = []
    for _ in range(7):
        totals.append(a + b)
        a, b = b, a + b
    assert totals == fibonacci_terms(7)
    print("Topic 08 checks passed")


if __name__ == "__main__":
    self_check()

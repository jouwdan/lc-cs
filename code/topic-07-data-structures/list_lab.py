"""Completed core collection functions for the guided lab."""
def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count = count + 1
    return count

def median(values):
    if len(values) == 0:
        return None
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2

if __name__ == "__main__":
    print(count_above([4, 8, 8, 2], 5))
    assert count_above([], 5) == 0
    assert count_above([5, 5], 5) == 0
    assert count_above([8, 8], 5) == 2
    for values in [[9, 2, 7], [9, 2, 7, 4], [6], []]:
        print(median(values))
    original = [9, 2, 7, 4]
    before = original.copy()
    assert median(original) == 5.5
    assert original == before

"""Completed searches for the guided lab."""
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

if __name__ == "__main__":
    assert linear_search([6, 3, 8, 2], 8) == 2
    assert linear_search([6, 3, 8, 2], 5) == -1
    assert linear_search([], 5) == -1
    assert linear_search([8], 8) == 0
    assert linear_search([8], 5) == -1
    assert linear_search([6, 3, 8, 2], 2) == 3
    print("Linear checks passed")
    values = [3, 7, 11, 18, 23, 31, 42]
    assert binary_search(values, 23) == 4
    assert binary_search(values, 24) == -1
    assert binary_search([], 23) == -1
    assert binary_search([23], 23) == 0
    assert binary_search([23], 24) == -1
    assert binary_search(values, 3) == 0
    assert binary_search(values, 42) == 6
    assert binary_search([3, 7, 7, 11], 7) in [1, 2]
    print("Binary checks passed")

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

original = [7, 2, 5, 1]
print(bubble_sort(original))
print(original)

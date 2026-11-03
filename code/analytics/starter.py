"""Change only values first. Run in Python 3; no file or package setup needed."""
values = [4, 6, 6, 12]
count = len(values)
if count == 0:
    average = None
    median = None
else:
    ordered = sorted(values)
    average = sum(values) / count
    middle = count // 2
    if count % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

print("Values:", values)
print("Count:", count)
print("Mean:", average)
print("Median:", median)

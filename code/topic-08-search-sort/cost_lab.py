from solutions import search_probes

for size in [8, 16, 32]:
    values = list(range(size))
    target = size + 1
    linear = search_probes(values, target)
    binary = search_probes(values, target, binary=True)
    print(size, linear, binary)

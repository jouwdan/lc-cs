def are_anagrams(first, second):
    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")
    return sorted(first) == sorted(second)

print(are_anagrams("Dormitory", "Dirty room"))
print(are_anagrams("abc", "abd"))

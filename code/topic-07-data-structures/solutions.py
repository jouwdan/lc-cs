"""Original Topic 07 collection models; no external dependencies."""
import csv
import io
import random
from pathlib import Path


def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count += 1
    return count


def median(values):
    if not values:
        return None
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def longest_increasing_run(values):
    if not values:
        return []
    current = [values[0]]
    best = current.copy()
    for value in values[1:]:
        if value > current[-1]:
            current.append(value)
        else:
            current = [value]
        if len(current) > len(best):
            best = current.copy()
    return best


def are_anagrams(first, second):
    return sorted(first.lower().replace(" ", "")) == sorted(second.lower().replace(" ", ""))


def check_digit(text):
    if not text or any(char not in "0123456789" for char in text):
        raise ValueError("Use a non-empty ASCII digit string")
    return str(sum(int(char) for char in text) % 10)


def weighted_check_digit(text):
    if not text or any(char not in "0123456789" for char in text):
        raise ValueError("Use a non-empty ASCII digit string")
    total = 0
    for index, char in enumerate(text):
        weight = 3 if index % 2 == 0 else 1
        total += int(char) * weight
    return str((10 - total % 10) % 10)


def valid_practice_id(text):
    return (len(text) == 5 and all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in text[:3])
            and all(char in "0123456789" for char in text[3:]))


def password_practice_score(text):
    return sum([len(text) >= 10, any(c.isupper() for c in text), any(c.islower() for c in text),
                any(c in "0123456789" for c in text), any(c in "!?@#" for c in text)])


def die_frequencies(values):
    counts = {face: 0 for face in range(1, 7)}
    for value in values:
        if type(value) is not int or value not in counts:
            raise ValueError("A die result must be an integer from 1 to 6")
        counts[value] += 1
    return counts


def read_scores(source):
    """Read a text stream; reject bad rows instead of silently dropping data."""
    reader = csv.DictReader(source)
    if reader.fieldnames is None or not {"name", "score"}.issubset(reader.fieldnames):
        raise ValueError("CSV needs name and score headers")
    scores = []
    for row in reader:
        if None in row or row.get("name") is None or not row["name"].strip():
            raise ValueError(f"Row {reader.line_num}: invalid name or extra fields")
        try:
            value = int(row["score"])
        except (TypeError, ValueError) as error:
            raise ValueError(f"Row {reader.line_num}: score must be an integer") from error
        if not 0 <= value <= 100:
            raise ValueError(f"Row {reader.line_num}: score must be from 0 to 100")
        scores.append(value)
    return scores


def add_bonus(score):
    score = score + 5
    return score


def frequency_chart(counts):
    return "\n".join(f"{face}: {'*' * counts[face]}" for face in range(1, 7))


def self_check():
    assert count_above([4, 8, 8, 2], 5) == 2
    assert count_above([], 5) == 0
    assert count_above([5, 5], 5) == 0
    for values, expected in [([9, 2, 7], 7), ([9, 2, 7, 4], 5.5), ([6], 6), ([], None), ([2, 2], 2)]:
        before = values.copy()
        assert median(values) == expected
        assert values == before
    for values, expected in [([3, 5, 2, 4, 7, 7, 9], [2, 4, 7]), ([], []), ([9], [9]),
                             ([3, 2, 1], [3]), ([1, 2, 1, 2], [1, 2]), ([4, 4], [4])]:
        before = values.copy()
        assert longest_increasing_run(values) == expected
        assert values == before
    assert are_anagrams("Dormitory", "Dirty room")
    assert not are_anagrams("abc", "abd")
    assert not are_anagrams("aab", "abb")
    assert are_anagrams("", "")
    assert check_digit("472") == "3"
    assert check_digit("005") == "5"
    assert check_digit("472") == check_digit("742")
    assert weighted_check_digit("472") == "5"
    assert weighted_check_digit("742") == "9"
    assert weighted_check_digit("000") == "0"
    assert weighted_check_digit("427") == "5"
    assert valid_practice_id("ABC42")
    assert not valid_practice_id("AB42")
    assert not valid_practice_id("AbC42")
    assert password_practice_score("MapleTree7!") == 5
    assert password_practice_score("abc") == 1
    assert die_frequencies([1, 3, 3, 6, 1, 3]) == {1: 2, 2: 0, 3: 3, 4: 0, 5: 0, 6: 1}
    assert sum(die_frequencies([]).values()) == 0
    with Path(__file__).with_name("scores.csv").open(newline="", encoding="utf-8") as source:
        assert read_scores(source) == [42, 67, 90, 67]
    assert read_scores(io.StringIO('name,score\n"Ava, A",50\n')) == [50]
    assert read_scores(io.StringIO("name,score\n")) == []
    for bad in ["person,mark\nA,50\n", "name,score\nA,101\n", "name,score\nA,no\n", "name,score\n,50\n", "name,score\nA\n"]:
        try:
            read_scores(io.StringIO(bad))
        except ValueError:
            pass
        else:
            raise AssertionError("Bad CSV accepted")
    for bad in ["", "4X2", "１２"]:
        try:
            check_digit(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Bad digit string accepted")
    score = 10
    assert add_bonus(score) == 15 and score == 10
    counts = die_frequencies([1, 3, 3, 6, 1, 3])
    assert frequency_chart(counts) == "1: **\n2: \n3: ***\n4: \n5: \n6: *"
    items = ["pear", "plum", "apple"]
    first_rng, second_rng = random.Random(42), random.Random(42)
    first = [first_rng.choice(items) for _ in range(20)]
    second = [second_rng.choice(items) for _ in range(20)]
    assert first == second and all(item in items for item in first)
    print("Topic 07 checks passed")


if __name__ == "__main__":
    self_check()

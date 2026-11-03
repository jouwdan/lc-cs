# 1. Learn: Lists & files

Use text, lists, functions and files.

Work through sections 1–6 before the collection lab. Use sections 7–9 for text and files. Save the extension patterns for another session; each is a reusable exam skill.

## 1. Find an item by its index

An **index** is a position. Python starts at zero.

| Character | C | O | M | P | U | T | E | R |
|---|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

For `word = "COMPUTER"`, `word[0]` gives `C` and `word[-1]` gives the last character, `R`. `len(word)` is 8, so `word[8]` is outside the string and raises `IndexError`.

A **slice** selects a section: `word[1:4]` includes indices 1, 2 and 3, giving `OMP`. The stop index is excluded.

**Try:** predict `word[:3]` and `word[4:]`.

**Check:** `COM` and `UTER`. Omitting the start means start at the beginning; omitting the stop means continue to the end.

## 2. Strings return new values

Strings are **immutable**: individual characters cannot be changed in place. `word[0] = "c"` fails. Build a new string with `word = "c" + word[1:]` instead.

| Method | Result | What it changes |
|---|---|---|
| `"Ava".lower()` | `"ava"` | Letter case |
| `"Ava".upper()` | `"AVA"` | Letter case |
| `"  Ava  ".strip()` | `"Ava"` | Surrounding whitespace |
| `"Dirty room".replace(" ", "")` | `"Dirtyroom"` | All ordinary spaces |

A **method** is an operation attached to a value, written after the dot. These methods return a new string; save that result if you need it. `.strip()` does not remove spaces between words.

**Try:** run `name = "AVA"` followed by `name.lower()` and `print(name)`.

**Check:** it still prints `AVA`. Use `name = name.lower()` to keep the lower-case result.

## 3. Lists can change

A **list** is an ordered collection: `scores = [42, 67, 67, 90]`. It has length 4 and `scores[2]` is 67. Lists are **mutable**, meaning their contents can change.

- `scores[0] = 50` replaces an item.
- `scores.append(80)` adds one item to the end.
- `scores.pop()` removes and returns the final item.
- `scores.remove(67)` removes the first matching 67; it raises an error if absent.

Duplicate values are still separate items. Do not discard one merely because it matches another.

### Alias or copy?

```python
a = [4, 7]
b = a
b.append(9)
print(a)
```

This prints `[4, 7, 9]`. `a` and `b` are **aliases**: two names for the same list. Use `b = a.copy()` for a separate copy of this flat list.

**Try:** make that one-line change and rerun.

**Check:** `a` stays `[4, 7]`. A **shallow copy** copies the outer list; nested inner lists are still shared.

`sorted(values)` returns a sorted copy. `values.sort()` changes the existing list and returns `None`. Therefore `values = values.sort()` replaces your list variable with `None`.

## 4. Return a reusable result

A function's **contract** states the accepted inputs and promised output. Here: count values strictly above a limit; return 0 for an empty list; keep the list unchanged.

```python
def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count = count + 1
    return count

print(count_above([4, 8, 8, 2], 5))
```

Output: 2. The parameter names are `values` and `limit`; the arguments are `[4, 8, 8, 2]` and 5. `return` supplies the result to the caller. `print` only displays it. A function with no explicit return gives `None`.

**Try:** change the arguments to `[5, 5]` and 5.

**Check:** 0. “Above” uses `>`, not `>=`.

### Local names and shared objects

```python
score = 10

def add_bonus(score):
    score = score + 5
    return score

result = add_bonus(score)
print(score, result)
```

Output: `10 15`. The parameter is a **local** name. Assigning a new integer to it does not reassign the outside name. In contrast, mutating a list received as an argument can change the caller's shared list. Prefer explicit parameters and return values to hidden global changes.

## 5. Separate the common calculation patterns

| Task | Initial value | Update |
|---|---|---|
| Count matches | 0 | Add 1 for a match |
| Sum values | 0 | Add the current value |
| Find a minimum | First value, after checking non-empty input | Replace it if a smaller value appears |
| Mean | Sum and number of values | Divide sum by count, if count is not zero |

Starting a minimum at 0 fails for `[4, 8]`: 0 was never an input. Empty data has no arithmetic mean; choose an explicit result such as `None`, rather than calling its mean zero. Validate types and units before measurement calculations.

**Try:** for `[4, 8, 8, 2]`, find count above 5, sum, minimum and mean.

**Check:** 2, 22, 2 and 5.5. These are different questions about the same data.

## 6. Find a median

The **median** is the middle of the ordered data. Sort a copy first.

| Original | Ordered | Middle index/indices | Median |
|---|---|---|---|
| `[9, 2, 7]` | `[2, 7, 9]` | 1 | 7 |
| `[9, 2, 7, 4]` | `[2, 4, 7, 9]` | 1 and 2 | `(4 + 7) / 2 = 5.5` |

For length `n`, let `middle = n // 2`.

1. If `n == 0`, return `None` before using an index.
2. Odd `n`: use `ordered[middle]`.
3. Even `n`: average `ordered[middle - 1]` and `ordered[middle]`.

**Try:** `[6]`, `[]` and `[2, 2]`.

**Check:** 6, `None`, 2. Test that the original list remains unchanged too.

## 7. Compare text under stated rules

An **anagram** uses the same characters in another order. Our practice rule ignores case and ordinary spaces, but keeps other characters.

```python
first = "Dormitory".lower().replace(" ", "")
second = "Dirty room".lower().replace(" ", "")
print(sorted(first) == sorted(second))
```

Output: `True`. Sorting characters gives lists, so repeated letters are counted. A set would lose repetitions and wrongly treat `aab` and `abb` as equivalent.

**Try:** compare `"abc"` with `"abd"`, then two empty strings.

**Check:** `False`, then `True` under this exact contract. If punctuation should be ignored, state that extra rule rather than silently removing it.

### Format checks and check digits

A classroom ID could require three uppercase ASCII letters followed by two digits: `ABC42` passes; `AB42` and `AbC42` fail. This is a practice format, not a complete real-world identifier specification.

A **check digit** is an extra digit used to detect some accidental changes. Our simple rule is `sum of payload digits MOD 10`. For `472`, the sum is 13, the check digit is 3, and the combined text is `4723`.

**Try:** calculate the check digit for `005` and then `742`.

**Check:** 5 and 3. Preserve leading zeroes as text. Swapping digits leaves their sum unchanged, so this scheme misses every transposition. A check digit is neither encryption nor proof of who created the data.

## 8. Read a CSV file

**CSV** means comma-separated values. The first row commonly names the columns. Save this fictional data in `scores.csv`:

```csv
name,score
Ava,42
Ben,67
Cian,90
Dara,67
```

Python's standard `csv` module handles quoted commas, unlike simply splitting every line at a comma:

```python
import csv
with open("scores.csv", newline="", encoding="utf-8") as source:
    rows = csv.DictReader(source)
    for row in rows:
        print(row["name"], int(row["score"]))
```

Run from the folder containing the file. `with` closes the file when the block ends. `DictReader` uses each header as a key; each field begins as text. Expected first line: `Ava 42`; the remaining three records follow.

Parsing reads the structure; **validation** still checks meaning. Require the headers `name` and `score`, non-empty names, whole-number scores and range 0–100. Report the row that failed. A missing file, missing header and invalid value are different faults.

Do not silently skip an invalid row and report a misleading overall result. The lab's contract rejects the file if any record is invalid. Keep the original file and experiment with a copy.

## 9. Count frequencies and draw a simple chart

A **dictionary** stores key/value pairs. Here each die face is a key and its observed count is the value:

```python
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for face in [1, 3, 3, 6, 1, 3]:
    counts[face] = counts[face] + 1
for face in range(1, 7):
    print(f"{face}: {'*' * counts[face]}")
```

The bars contain 2 stars for 1, 3 stars for 3 and 1 star for 6. Other faces still get labels with empty bars. **Total frequency must equal the number of observations:** here 6.

For unknown categories, `counts.get(item, 0)` retrieves an existing count or 0 if absent. Test fixed observations before using random ones.

## 10. Extension: preserve a consecutive run

A **consecutive run** uses neighbouring items in their original order. In `[3, 5, 2, 4, 7, 7, 9]`, the longest strictly increasing run is `[2, 4, 7]`. Equal neighbours break a strictly increasing run. Sorting would destroy the adjacency information.

Keep two lists: `current`, the run ending here, and `best`, the longest so far.

1. Start both with the first item; return `[]` first if input is empty.
2. If the next value is greater than the last current value, append it.
3. Otherwise start a new current run containing that value.
4. Replace `best` with `current.copy()` only when current is **longer**. This keeps the earliest run on a tie.

**Try:** trace `[1, 2, 1, 2]`.

**Check:** the first `[1, 2]` remains best. Copying protects it from later changes to the current list.

## 11. Extension: a weighted check digit

A **weight** is a multiplier for one position. Our original practice scheme uses 3, 1, 3, 1… from the left, then chooses `c = (10 - total % 10) % 10`.

| Digit in `472` | Weight | Product |
|---:|---:|---:|
| 4 | 3 | 12 |
| 7 | 1 | 7 |
| 2 | 3 | 6 |

Total 25 needs check digit 5 to reach a multiple of 10. The final `% 10` makes a total of 0 produce digit 0, not 10.

**Try:** calculate totals and check digits for `742`, `000` and `427`.

**Check:** totals 31, 0, 35; check digits 9, 0, 5. The scheme detects the first swap from `472` to `742`, but misses `472` to `427`. Follow the direction, weights and modulus in the actual question; other schemes differ.

## 12. Extension: independent conditions and random choices

A practice password score may award one point each for length at least 10, uppercase, lowercase, a digit and a symbol from `!?@#`. Use five independent `if` checks; `if/elif` would stop after one. Use invented strings, never real passwords. Passing these rules does not guarantee security.

For repeatable simulated choices:

```python
import random
rng = random.Random(42)
items = ["pear", "plum", "apple"]
choices = [rng.choice(items) for _ in range(5)]
print(choices)
```

The bracketed expression repeats a choice five times to build a list. The seed 42 makes repeated runs of this code reproducible. The choices all belong to `items`; a short run need not contain every item or equal counts. `choice` requires a non-empty sequence. Check counting separately from random generation.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-07-data-structures/book-01-practice">2. Practise: process a small dataset</a>. <a href="https://tutors.dev/note/lc-cs/topic-07-data-structures/note-02-feedback">Open the answers</a>.

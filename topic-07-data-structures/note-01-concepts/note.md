# Working with collections and reusable functions

Transform small pieces of data with clear contracts, then combine the pieces into a complete program.

## Strings are sequences

A string is an ordered sequence of characters. Python uses zero-based indexing: in `word = "COMPUTER"`, `word[0]` is `C`, `word[3]` is `P`, and `word[-1]` is `R`. `len(word)` is 8, so the final non-negative index is 7. An index of 8 raises `IndexError`. A slice `word[1:4]` returns `OMP`: the start is included and the stop is excluded, just as with `range`.

Strings are immutable. You cannot assign `word[0] = "c"`; construct a new string instead, for example `word = "c" + word[1:]`. Methods such as `.lower()`, `.upper()`, and `.strip()` return strings rather than editing the original in place. `"  Ava  ".strip()` removes surrounding whitespace but preserves internal spaces. Avoid removing characters unless the task says they are irrelevant.

String comparisons are case-sensitive. Decide whether a task treats `A` and `a` as equivalent, then normalise consistently. For a deliberately simplified anagram task, ignore spaces and letter case, retain all other characters, and compare sorted characters. `"Dormitory"` and `"Dirty room"` match under those rules. If punctuation should also be ignored, state that different contract explicitly. A solution should not invent cleaning rules to make a particular pair match.

## Lists, mutation, and aliases

A list stores an ordered collection. `scores = [42, 67, 67, 90]` has length 4, and `scores[2]` is 67. Unlike strings, lists are mutable: `scores[0] = 50` changes the first item. `append(value)` adds one item; `pop()` removes and returns the final item; `remove(value)` removes the first matching value and raises an error if absent. A list can contain repeated values, which must not disappear accidentally during processing.

Assignment does not automatically copy a list:

```python
a = [4, 7]
b = a
b.append(9)
print(a)
```

The output is `[4, 7, 9]` because both names refer to the same list. For a separate shallow copy of a flat list, use `b = a.copy()` or `b = a[:]`. For a list containing nested lists, a shallow copy still shares the inner objects; this distinction is useful when tracing a supplied program.

`sorted(values)` returns a sorted copy, while `values.sort()` changes the existing list and returns `None`. Thus `values = values.sort()` loses the list binding. Choose whether your function may modify its input and document that choice. Preserving the original is useful when you must display both initial and sorted data.

## Functions: parameters and results

A function packages a named task. A parameter is the name in the definition; an argument is the actual value passed by a call. `return` sends a result back to the caller and ends the function. `print` displays text and is not a substitute for returning a value. A function that reaches its end without `return` returns `None`.

```python
def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count += 1
    return count

answer = count_above([4, 8, 8, 2], 5)
print(answer)
```

The output is `2`. `values` and `limit` are parameters, the list and 5 are arguments, and `count` is local state. Passing different arguments reuses the same rule. Keep input prompts outside this calculation so tests can call it without simulating a keyboard. A small function is easier to test when it has one clear job and a stated output.

## Counting, totals, and frequencies

Counting qualifying items, summing values, and finding a minimum are different patterns. A count begins at zero and adds one for each match. A sum begins at zero and adds each value. A minimum can start with the first value, but then the empty-list case must be handled first. Initialising the minimum to zero fails for a list of positive values because zero was never present.

For a mean, divide the total by `len(values)`, not by a hard-coded number from an example. An empty list has no arithmetic mean. Return a stated absence value such as `None` or raise a documented error; do not claim its mean is zero. For measurement data, validate that each item has the required numeric type and units before calculating.

A dictionary can count frequencies efficiently. For each item, `counts[item] = counts.get(item, 0) + 1` increases the stored count or starts it at one. A six-sided die experiment might count results 1 through 6, including zero counts for faces not observed. Total frequency must equal the number of trials. This invariant catches lost or duplicated observations. Random output changes between runs, so test counting with a fixed list before using random samples.

## Median and consecutive runs

The median needs a sorted copy. If there are `n` values and `n` is odd, the middle index is `n // 2`. If `n` is even, average indices `n // 2 - 1` and `n // 2`. For `[9, 2, 7]`, sorting gives `[2, 7, 9]` and the median is 7. For `[9, 2, 7, 4]`, sorting gives `[2, 4, 7, 9]` and the median is 5.5. Handle `n == 0` before indexing.

A longest **consecutive increasing run** must preserve adjacency. In `[3, 5, 2, 4, 7, 7, 9]`, the longest strictly increasing run is `[2, 4, 7]`. Equal neighbouring values break a strictly increasing run. Sorting the list destroys the order information needed for this problem. Define ties: the lab returns the earliest run when several have the same maximum length.

Maintain `current`, the run ending at the current item, and `best`, the longest run found so far. Extend `current` only when the new value is greater than the previous value; otherwise start a new run. Replace `best` only when `current` is longer. Use a copy when storing the best run so later appends do not change it unexpectedly. Empty input returns `[]`; a single value returns that one-item run.

## Validation strings and check digits

A format check can test length, character classes, and positions. A classroom identifier might require three uppercase ASCII letters followed by two digits: `ABC42` passes and `AB42` fails. This rule is only a practice format, not a complete Eircode specification. Real identifier systems can have permitted-prefix tables and exceptions; implement the rules the question actually supplies.

A simple teaching check digit can be `sum(digits) % 10`. For `472`, the digit sum is 13 and the check digit is 3, giving `4723`. This detects some errors but does not detect swapping two digits because their sum is unchanged. A check digit detects certain accidental changes; it is not encryption or proof of authenticity. Reject a non-digit character before conversion and keep leading zeroes as text.

A password-scoring exercise might award one point each for sufficient length, an uppercase letter, a lowercase letter, a digit, and a permitted symbol. These are classroom rules, not a guarantee of real security. Keep each condition independent if several points can be earned. An `if`/`elif` chain would award at most one condition and therefore implement a different rule. Never use real passwords in classroom datasets or submission files.

## Read files as structured data

Use a context manager so a file is closed reliably:

```python
import csv
with open("scores.csv", newline="", encoding="utf-8") as source:
    rows = csv.DictReader(source)
    for row in rows:
        print(row["name"], int(row["score"]))
```

The `csv` module handles quoted commas correctly; splitting every line on commas does not. Specify expected headers and validate missing or malformed fields. Distinguish a missing file, a missing column, a non-numeric value, and an out-of-range value. A clear row number makes an error actionable. Do not overwrite the input file while experimenting; write a separately named output when required.

## Practice sequence and exam transfer

Start by tracing a five-character string and a four-item list. Then write one function that returns a result without input or printing. Test ordinary, boundary, and empty cases. Only then connect file reading or user input. This keeps a parsing fault from being confused with an algorithm fault.

The archived Higher Level Section C tasks include password rules (2020), anagrams (2021), dice outcomes (2022), and list statistics with a consecutive-run extension (2025). These are instances of the reusable patterns above. Consult each paper's exact rules, then its matching scheme; do not transfer an old question's assumptions into a new task. See [the archive year index](https://www.betterexams.ie/leaving-cert/computer-science).

## Extension workshop: a weighted check digit

A weighted check digit assigns different importance to positions. For an original practice scheme, multiply payload digits by alternating weights 3, 1, 3, 1 from the left. Add the products. Choose a final check digit `c = (10 - total % 10) % 10`, so weighted payload total plus `c` is divisible by 10. This is a specified classroom scheme, not a claim to implement a particular commercial standard.

For payload `472`:

| Position | Digit | Weight | Product |
|---:|---:|---:|---:|
| 0 | 4 | 3 | 12 |
| 1 | 7 | 1 | 7 |
| 2 | 2 | 3 | 6 |

The total is 25. The required check digit is 5, because 25 + 5 = 30. The final modulo in the formula ensures that a total already divisible by 10 produces digit 0 rather than the two-character value 10. Preserve leading zeroes in the payload string.

Changing `472` to `742` changes the weighted total to 31, so the old check digit 5 fails. However, `427` has weighted total 35 and still accepts check digit 5. Weighting detects this first transposition but misses the second. Explain the actual limitation rather than claiming that weighting catches every error.

When tracing a supplied check-digit algorithm, write one row per digit with position, weight, product, and running total. Follow the specified direction of weighting and final modulus exactly. Swapping left-to-right for right-to-left or using `% 10` instead of the required complement implements a different rule.

## Short transfer drills: scope, choices, and charts

A function parameter is a local binding. Reassigning a scalar parameter does not reassign an outside name:

```python
score = 10

def add_bonus(score):
    score = score + 5
    return score

result = add_bonus(score)
print(score, result)
```

This prints `10 15`. The parameter starts by referring to the integer passed in; the local assignment then binds it to a new integer. The outside `score` stays 10. Contrast this with mutating a list passed as an argument: the caller and function can refer to the same mutable list. Avoid using global variables when an explicit parameter and return value explain the data flow.

A frequency dictionary can generate a simple horizontal chart without a plotting library:

```python
counts = {1: 2, 2: 0, 3: 3, 4: 0, 5: 0, 6: 1}
for face in range(1, 7):
    print(f"{face}: {'*' * counts[face]}")
```

The non-empty bars are `1: **`, `3: ***`, and `6: *`; faces 2, 4, and 5 still get labelled empty lines. One star represents one observation, so total stars must equal total trials. A chart with only observed faces can hide the fact that some possible outcomes had zero observations.

For a choice-based simulation, `rng.choice(items)` selects one element from a non-empty sequence, for example `items = ["pear", "plum", "apple"]`. With `rng = random.Random(42)`, repeated runs of the same code use a reproducible pseudo-random sequence. Test that each selected value belongs to the available choices; do not assert that a short sample must contain every choice or perfectly equal counts. Selecting from an empty list raises an error, so define or validate the available choices first. Random simulations and deterministic frequency counting are separate parts that should be checked separately.

# 4. Answers: Lists & files

Check your reasoning and repair one gap.

Use this after an attempt. Find the question or lab step you missed, explain the correction in one sentence, then rerun that case yourself.

## Quiz explanations

1. **`OMP`.** Indices 1, 2, 3 are included; index 4 is excluded.
2. **`[4, 7, 9]`.** `b = a` aliases the same list. Mutating it through either name changes the shared object.
3. **`None`.** `.sort()` mutates in place. `sorted(values)` produces a new sorted list.
4. **False.** Printing is an output side effect; returning supplies a value to the caller. Without an explicit return, the function returns `None`.
5. **5.5.** Sorted data are `[2, 4, 7, 9]`; average the values at indices 1 and 2.
6. **An empty list.** Index zero does not exist, so the contract must define an empty-data result before accessing it.
7. **`[2, 4, 7]`.** The values are adjacent and strictly increasing. Sorting or selecting non-adjacent values would answer a different question.
8. **False.** Swapping two digits preserves their sum, so this simple scheme cannot detect the swap.
9. **Quoted fields and headers.** Parsing is only the first step; numeric conversions and range checks remain your responsibility.
10. **False.** An `if`/`elif` chain stops after the first true branch. Independent criteria need independent checks.


## Collection answers

The indexing predictions are `OMP`, 3 and 2. A non-empty sequence of length `n` has non-negative indices 0 through `n-1`.

Replace `count = count + 0` with `count = count + 1`. `[4,8,8,2]` above 5 gives 2; empty input and `[5,5]` give 0; `[8,8]` gives 2.

Replace the median starter's final line with:

```python
return (ordered[middle - 1] + ordered[middle]) / 2
```

| Input | Ordered copy | Middle index/indices | Result |
|---|---|---|---|
| `[9,2,7]` | `[2,7,9]` | 1 | 7 |
| `[9,2,7,4]` | `[2,4,7,9]` | 1, 2 | 5.5 |
| `[6]` | `[6]` | 0 | 6 |
| `[]` | Not needed | None | `None` |

The original list remains unchanged because `sorted` creates a new list. Do not replace it with `values = values.sort()`: `.sort()` returns `None`.

## Text and file answers

Anagram results: Dormitory/Dirty room → True; abc/abd → False; aab/abb → False; empty/empty → True. Sorting preserves the number of repeated letters; a set would lose it.

The valid CSV produces `[42,67,90,67]`. Its middle pair is 67 and 67, so the example displays `Median: 67.0`. Numerically this is 67. Ben is physical CSV row 3 because row 1 is the header. Score 101 must raise a range error before any median is displayed. The changed `mark` header raises the header error.

The guided reader requires exactly `name,score` in that order. The fuller checked model requires both named columns and can accept additional named columns. Both contracts are stated explicitly; neither silently drops invalid score rows.

## Extension: longest run

Add:

```python
if len(current) > len(best):
    best = current.copy()
```

| Value | Current run | Best run |
|---:|---|---|
| 3 | `[3]` | `[3]` |
| 5 | `[3,5]` | `[3,5]` |
| 2 | `[2]` | `[3,5]` |
| 4 | `[2,4]` | `[3,5]` |
| 7 | `[2,4,7]` | `[2,4,7]` |
| 7 | `[7]` | `[2,4,7]` |
| 9 | `[7,9]` | `[2,4,7]` |

Equality breaks a strictly increasing run. Replacing best only on a greater length preserves the earliest tie; copying protects the saved run from mutation. Sorting would destroy the original adjacency.

## Other extension checks

- Simple check digits: `472` → 3; `005` → 5; `742` → 3. The swap is missed because the sum is unchanged.
- Weighted totals: 25, 31, 0 and 35 for `472`, `742`, `000`, `427`. Corresponding check digits: 5, 9, 0, 5. The second swap is still missed.
- Die frequencies: 2, 0, 3, 0, 0, 1; their sum is 6. Adding a 6 gives its face two observations and total 7.
- Practice password scores: `MapleTree7!` → 5; `abc` → 1. These independent criteria require independent checks, and do not prove security.
- Local scope: `add_bonus(10)` returns 15 while the caller's original score stays 10.

[Completed guided files and checked models](https://github.com/jouwdan/lc-cs/tree/main/code/topic-07-data-structures) let you compare one function at a time. Running `solutions.py` prints `Topic 07 checks passed`.

**Repair one gap:** label indices from zero if slicing failed. Draw names pointing to list objects if mutation surprised you. For empty input, state the required result before any indexing.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-07-data-structures/note-03-exam-practice">5. Exam practice: apply one skill</a>. <a href="https://tutors.dev/note/lc-cs/topic-07-data-structures/note-02-feedback">Open the answers</a>.

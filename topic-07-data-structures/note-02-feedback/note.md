# Collections: feedback and worked answers

Use each explanation to connect a result to the data structure and contract.

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

## Median model

| Input | Sorted copy | Middle index/indices | Result |
|---|---|---|---|
| `[9, 2, 7]` | `[2, 7, 9]` | 1 | 7 |
| `[9, 2, 7, 4]` | `[2, 4, 7, 9]` | 1 and 2 | 5.5 |
| `[6]` | `[6]` | 0 | 6 |
| `[]` | Not needed | None | `None` |

A compact correct approach checks empty input, sorts a copy, computes `middle = len(ordered) // 2`, and branches on odd/even length. The input order stays unchanged.

## Run trace

| Value processed | Current run | Best run |
|---:|---|---|
| 3 | `[3]` | `[3]` |
| 5 | `[3, 5]` | `[3, 5]` |
| 2 | `[2]` | `[3, 5]` |
| 4 | `[2, 4]` | `[3, 5]` |
| 7 | `[2, 4, 7]` | `[2, 4, 7]` |
| 7 | `[7]` | `[2, 4, 7]` |
| 9 | `[7, 9]` | `[2, 4, 7]` |

The equality at the second 7 breaks a strictly increasing run. Keeping the old best on equal lengths implements the earliest-tie rule. The model copies the current run when it becomes best, preventing later mutation from corrupting the saved result.

## Text and file model

Anagram normalisation lowercases and removes spaces, then compares sorted characters. It preserves repeated-character counts. A set comparison would incorrectly treat `aab` and `abb` as equal.

The check digits for `472` and `005` are `3` and `5`. The transposition `742` also produces `3`, demonstrating a limit. Validation is not authentication.

The CSV yields `[42, 67, 90, 67]` and median 67. The model uses `csv.DictReader`, requires the headers, validates names and integer ranges, and reports bad rows. It raises an error instead of quietly excluding an inconvenient result.

The complete [`solutions.py`](https://github.com/jouwdan/lc-cs/blob/main/code/topic-07-data-structures/solutions.py) includes median, runs, anagrams, frequencies, format checks, password practice, and CSV validation. Run `python3 code/topic-07-data-structures/solutions.py`; expect `Topic 07 checks passed`.

## Improve your next attempt

If indexing failed, label every position starting at zero. If a list unexpectedly changed, draw arrows from names to list objects. If aggregation failed only on empty input, state the empty-data contract before writing a loop. If a file error was unclear, include a row number and the violated rule rather than a generic “bad data” message.

## Weighted-check answer

`472` produces products 12, 7, 6, total 25, and complement digit 5. `742` produces 21, 4, 6, total 31, and complement digit 9. `000` produces total 0 and digit 0. `427` produces 12, 2, 21, total 35, and digit 5: the selected adjacent transposition is undetected. The checked `weighted_check_digit` function is included with the other models.


For the scope drill, the outer score remains 10 and the returned result is 15. Rebinding a scalar parameter changes the local name; it does not rebind the caller's variable. For the frequency chart, the three non-empty bars contain 2, 3, and 1 stars, summing to six observations. A seeded random choice is repeatable, but repeatability does not imply that every short sequence is evenly distributed.

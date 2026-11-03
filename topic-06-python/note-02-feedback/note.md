# Python fundamentals: feedback

Check the reasoning behind each expression, branch, and repeated step.

## Quiz explanations

1. **`str`.** A conversion is explicit; typing digits does not change `input()`'s return type.
2. **3.** For these positive operands, floor division gives the whole-number quotient. The remainder is 2.
3. **6.** `range(1, 4)` yields 1, 2, 3. The successive totals are 1, 3, 6; 4 is excluded.
4. **`0 <= score <= 100`.** Both limits must hold. The expression using `or` accepts values outside the range.
5. **True.** Later branches are skipped once a condition is satisfied. Independent `if` statements do not have that behaviour.
6. **`"34"`.** Both operands are strings, so `+` concatenates them.
7. **The wrong comparison boundary.** The program can run normally but produce an incorrect classification. Missing punctuation is syntax; invalid conversion and division by zero are runtime errors.
8. **False.** The condition is tested first. If false initially, there are zero iterations.
9. **`2.50`.** Fixed-point formatting with precision 2 displays two digits after the decimal point.
10. **To preserve earlier additions.** Resetting the total inside the body discards earlier work.

## Lab answers

The expression answers are 3, 2, 11, 14. The text expression is `"34"`; numeric addition gives 7.

| Age | Price in cents | Reason |
|---:|---:|---|
| 0 | 800 | Valid lower boundary; below 16 |
| 15 | 800 | Last child age |
| 16 | 1200 | First standard age |
| 64 | 1200 | Last standard age |
| 65 | 900 | First senior age |
| 120 | 900 | Valid upper boundary |
| -1, 121 | Error | Outside the accepted range |

The complete model rejects an invalid type or age before selecting a price. Within the valid range, `< 16`, then `< 65`, then the final branch cover all cases exactly once.

For `[12, 16, 70]`, prices are 800, 1200, 900, and running totals are 800, 2000, 2900. Displaying the final total produces `29.00`. Resetting before every addition leaves 900, which exposes a logical error. Empty input leaves the initial total at zero.

Sentinel input `[40, 60, -1, 99]` produces count 2 and total 100. Processing stops at -1, so 99 is not read as another score. An immediate -1 yields `(0, 0)`. Rejecting -2 separately shows that the sentinel is a deliberate protocol, not a general rule to accept any negative score.

The checked [`solutions.py`](https://github.com/jouwdan/lc-cs/blob/main/code/topic-06-python/solutions.py) includes the functions, a reusable prompt, and assertions. Run `python3 code/topic-06-python/solutions.py`; expect `Topic 06 checks passed`. The self-check does not prompt for input. To practise the interface, call `prompt_for_age()` explicitly and try `sixteen`, `16.5`, -1, and 16 in sequence.

## Review your evidence

A test record needs input, expected result, actual result, and a conclusion. “It works” is not a record. If a branch failed, add a neighbouring value on each side of its threshold. If an input failed to convert, state the conversion error separately from the range check. If a loop failed, trace its state before rewriting it.

---
order: 4
---
# 4. Answers: Python

Check your reasoning and repair one gap.

Use this after an attempt. Find the question or lab step you missed, explain the correction in one sentence, then rerun that case yourself.

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


## Stage 1: expressions and one ticket

The six expression lines are `3`, `2`, `11`, `14`, `34`, `7`. The fifth is text concatenation; the sixth is numeric addition.

The completed price selection, after the supplied validation, is:

```python
if age < 16:
    return 800
elif age < 65:
    return 1200
else:
    return 900
```

| Age | Expected cents | Why |
|---:|---:|---|
| 0 | 800 | Valid minimum; child band |
| 15 | 800 | Last child age |
| 16 | 1200 | First standard age |
| 64 | 1200 | Last standard age |
| 65 | 900 | First senior age |
| 120 | 900 | Valid maximum |
| -1, 121 | Error | Out of range |

The `< 16` → `<= 16` experiment puts 16 in the wrong band. The age-16 assertion exposes it; restoring `< 16` makes the test pass.

## Stage 2: input and totals

`input()` returns text. `int("-1")` succeeds but the range check fails. `int("sixteen")` and `int("16.5")` fail conversion. Each should produce a useful message rather than a made-up price.

| Age | Price | Running total |
|---:|---:|---:|
| 12 | 800 | 800 |
| 16 | 1200 | 2000 |
| 70 | 900 | 2900 |

The group display is `Group total: EUR 29.00`. Empty input leaves zero and displays `0.00`. Moving the initialisation into the loop discards earlier totals, leaving 900 cents and a display of `9.00`.

## Sentinel extension

Add `count = count + 1` only after the input has converted, passed the sentinel test and passed range validation. For 40, 60, -1, final lines are `Count: 2` and `Total: 100`. Immediate -1 leaves both zero. For -2, 101, hello, 50, -1, only 50 counts: count 1, total 50.

The sentinel is checked before addition so -1 is not treated as a real score. `while` suits an unknown number of entries; `for` suits the known ages list.

## Find the stage you need

The [completed guided files](https://github.com/jouwdan/lc-cs/tree/main/code/topic-06-python) match the lab filenames. Keep `tickets.py` beside `ticket_input.py` and `group_tickets.py` so the imports work. Run each file independently.

The older, fuller [solutions.py](https://github.com/jouwdan/lc-cs/blob/main/code/topic-06-python/solutions.py) provides reusable models and additional assertions. Its direct run prints `Topic 06 checks passed` and does not prompt. The guided `ticket_input.py` and `score_entry.py` are the files to run for keyboard practice.

**Repair one gap:** if the function was confusing, run `double(6)` from Learn and label parameter, argument and return value. If your loop failed, trace the running total before changing the code.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-06-python/note-03-exam-practice">5. Exam practice: apply one skill</a>. <a href="https://tutors.dev/note/lc-cs/topic-06-python/note-02-feedback">Open the answers</a>.

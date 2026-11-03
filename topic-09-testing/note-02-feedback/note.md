# Testing: feedback and model evidence

Make every conclusion traceable to a requirement and a particular check.

## Quiz explanations

1. **Accept 1–8 and reject other integers.** It defines observable boundaries and a result for invalid data.
2. **4, 5, 6.** These straddle the price-change boundary and reveal an incorrect exclusive comparison.
3. **Earlier behaviour still works.** Regression testing detects unintended effects of a change; it does not promise future perfection.
4. **False.** Components can be connected incorrectly or displayed misleadingly despite correct isolated calculations.
5. **The response-time threshold.** It concerns a quality of the behaviour. The other choices specify what the system does.
6. **True.** A hand calculation or independent reference can act as an oracle. Duplicating the same bug in an expected-value formula is a weak oracle.
7. **x = 5, y = 4.** Postfix increment produces the old value for assignment and then updates x.
8. **False.** Strict equality does not coerce the string to a number.
9. **Reduce and test a hypothesis.** This focuses the diagnosis and keeps cause and effect observable.
10. **False.** Coverage measures execution, not the correctness of requirements or every asserted result.

## Booking model

| Quantity | Expected cents | Faulty version cents | Corrected cents |
|---:|---:|---:|---:|
| 1 | 1200 | 1200 | 1200 |
| 2 | 2400 | 2400 | 2400 |
| 3 | 3600 | 3600 | 3600 |
| 4 | 4800 | 4800 | 4800 |
| 5 | 5000 | 6000 | 5000 |
| 6 | 6000 | 6000 | 6000 |
| 7 | 7000 | 7000 | 7000 |
| 8 | 8000 | 8000 | 8000 |

Quantity 5 is the smallest valid value exposing the comparison defect. The valid-input repair is changing `> 5` to `>= 5`. The complete function also validates type and range before choosing a rate; this addresses separate missing requirements in the deliberately limited specimen.

The function rejects numeric text because its contract requires an integer. The interface accepts that text, converts it, calls the function, and displays `Total: EUR 50.00` for five tickets. This division of responsibility makes both layers testable.

A unit check calls `booking_total_cents(5)` and expects 5000. An integration check calls `total_from_text("5")` and expects the formatted message. A hypothetical system check would complete a booking through all screens and verify the final stored record; that larger system does not exist in this exercise, so it has not been tested. An accessibility check could verify that an error is announced and associated with the input field during keyboard-only use.

## JavaScript trace

| After statement | x | before | after |
|---|---:|---:|---:|
| `let x = 4` | 4 | Not declared yet | Not declared yet |
| `let before = x++` | 5 | 4 | Not declared yet |
| `let after = ++x` | 6 | 4 | 6 |

JavaScript `3 === "3"` is false; loose `3 == "3"` is true. Python `3 == "3"` is false. JavaScript `"3" + 4` yields `"34"`; Python raises `TypeError` for that mixed-type addition. These results are checked in the corresponding runtime files.

Run the [`Python model`](https://github.com/jouwdan/lc-cs/blob/main/code/topic-09-testing/solutions.py) with `python3 code/topic-09-testing/solutions.py`, and the [`JavaScript checks`](https://github.com/jouwdan/lc-cs/blob/main/code/topic-09-testing/operator-checks.js) with `node code/topic-09-testing/operator-checks.js`. Expect `Topic 09 checks passed` and `JavaScript operator checks passed`.

## A defensible evaluation

“The corrected function passes all eight valid integer quantities and rejects the selected invalid ranges and types. The quantity-5 test reproduced the original bug and now passes. The text-conversion integration checks pass. No real booking store, payment flow, load test, or accessibility-tested interface is included, so no claim is made about those systems.”

That statement is more informative than “fully tested”. Add a new test when a new requirement or failure appears, then keep the useful regression cases.

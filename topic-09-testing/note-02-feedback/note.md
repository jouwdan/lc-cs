# 4. Answers: Testing

Check your reasoning and repair one gap.

Use this after an attempt. Find the question or lab step you missed, explain the correction in one sentence, then rerun that case yourself.

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


## The reproduced fault

The original function uses `quantity > 5`. Quantity 5 therefore gets price 1200 instead of 1000, so the total is 6000 instead of 5000. This is a logical boundary error; the code runs normally until the assertion reports the wrong result.

The repair is `quantity >= 5`. Validation is a separate addition needed to reject invalid types and quantities before choosing a price.

| Quantity | Expected cents | Faulty cents | Corrected cents |
|---:|---:|---:|---:|
| 1 | 1200 | 1200 | 1200 |
| 2 | 2400 | 2400 | 2400 |
| 3 | 3600 | 3600 | 3600 |
| 4 | 4800 | 4800 | 4800 |
| 5 | 5000 | 6000 | 5000 |
| 6 | 6000 | 6000 | 6000 |
| 7 | 7000 | 7000 | 7000 |
| 8 | 8000 | 8000 | 8000 |

Quantity 0 must be rejected. So must 9, -1, 2.5 and text passed directly to the function. The text interface converts `"5"` to integer 5, then correctly displays `Total: EUR 50.00`.

## Check the right layer

- **Unit:** `booking_total_cents(5)` returns 5000.
- **Integration:** enter text 5 and obtain the formatted total, exercising conversion, calculation and display.
- **Regression:** after repairing 5, confirm 1 still returns 1200.
- **Proposed system test:** complete a future booking flow and inspect the saved record. No storage exists in this exercise, so this remains a proposal.
- **Proposed accessibility check:** use only a keyboard to reach the field, submit invalid input and locate an understandable error without relying on colour.

The invalid-input tests expect `ValueError`. They must fail if no error is raised. Do not round a fractional quantity or silently substitute zero.

## JavaScript answer trace

| After statement | x | before | after |
|---|---:|---:|---:|
| `let x = 4` | 4 | Not declared | Not declared |
| `let before = x++` | 5 | 4 | Not declared |
| `let after = ++x` | 6 | 4 | 6 |

JavaScript `3 === "3"` is false; `3 == "3"` is true through coercion; `"3" + 4` produces string `"34"`. Python `3 == "3"` is False and `"3" + 4` raises TypeError. Use the language printed in the question.

## A model evaluation

“The corrected function passed all eight allowed integer quantities and rejected my selected invalid ranges and types. The quantity-5 assertion failed before the repair and passed afterwards. I also checked valid and invalid text through the input program. This calculator contains no booking store, payment flow or web interface, so I have not tested those.”

This records evidence without claiming that no bugs remain.

[Completed guided files](https://github.com/jouwdan/lc-cs/tree/main/code/topic-09-testing) match the lab names. `booking_lab.py` prints `Booking checks passed`. `faulty_booking.py` intentionally prints 6000 and raises AssertionError. The separate full `solutions.py` prints `Topic 09 checks passed`; `node operator-checks.js` prints `JavaScript operator checks passed`.

**Repair one gap:** write the expected answer by hand, then trace the exact branch taken by the smallest failing input. Keep the failed case as a future regression test.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-09-testing/note-03-exam-practice">5. Exam practice: apply one skill</a>. <a href="https://tutors.dev/note/lc-cs/topic-09-testing/note-02-feedback">Open the answers</a>.

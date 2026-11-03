# Original mock: worked marking guide

This is an educator's formative guide, **not an SEC marking scheme**. Accept equivalent correct reasoning. Award only the marks supported by the response and keep the original attempt. The total is A 20 + B 30 + C 50 = 100. Discuss genuinely ambiguous alternatives with a teacher.

## Section A — 20 marks

1. **00101101** and **2D**. One mark each. The binary place values are 32 + 8 + 4 + 1 = 45; hexadecimal 2 × 16 + 13 = 45.
2. Outputs **0, 0, 1, 0**. Half a mark each. Only A=1 and B=0 makes both A and NOT B true.
3. The program counter holds the address of the next instruction (1). The ALU performs arithmetic and logical operations (1). Do not confuse the address with the instruction's result.
4. RAM is volatile and normally loses its contents without power (1). An SSD provides non-volatile storage and retains stored data without power (1). Capacity or speed alone does not answer the requested comparison.
5. DNS resolves a domain/host name to an address such as an IP address (1). HTTPS protects traffic using TLS, for example encryption against reading in transit or integrity against undetected modification (1). It does not guarantee the website's claims are truthful.
6. **3**, then **1**. One mark each. `//` is integer floor division here; `%` gives the remainder.
7. A connected label provides a persistent accessible name, unlike disappearing placeholder text (1). A clear focus outline or equivalent visible keyboard-focus style is appropriate (1). “Make it green” without a focus mechanism is insufficient.
8. Sort to `1, 3, 3, 9`; the central values are 3 and 3 (1), so their average is **3** (1).
9. **9, 10, 20, 21**, half a mark each. These cover just below, at the lower boundary, at the upper boundary and just above.
10. The lookup allows an ID to be linked back to a named person (1), so replacing names does not prevent identification; this is pseudonymisation rather than guaranteed anonymity (1). Equivalent explanation earns credit without requiring the terminology.

## Question 11 — 15 marks

(a) Sum **124** (1), count **5** (1), mean **24.8** (1). A correct formula with an arithmetic slip can earn the supported method points.

(b) Median **6** (1). The large value 100 pulls the mean upward much more than it affects the ordered middle observation (1).

(c) A **line graph** is appropriate for successive sample times (1). Give a time axis with suitable units or a reading axis with its measurement units (1). A clearly justified equivalent representation can be accepted.

(d) Recognise that blank means missing rather than a measured zero (1). Exclude it with a reason, or use another explicitly justified policy appropriate to the investigation (1). Preserve/log the original row and the decision so the analysis can be reproduced (1). Unexplained replacement by zero earns no policy point.

(e) Association alone does not establish cause (1). Another variable, coincidental variation or a sampling issue could influence both; give one plausible explanation (1). For instance, lunch time may change both visitor numbers and activity types.

(f) One lunch sample cannot establish behaviour at all times or represent every relevant condition (1). Sample at different times/days using a planned method (1) and keep comparable locations, measurement procedure and units or collect an appropriately balanced sample (1). Accept two distinct relevant design improvements.

## Question 12 — 15 marks

(a) Analogue sensor or digital button as input (1); compare the calibrated value/enable state and update the warning decision (1); display warning as output (1).

(b) The ADC code represents a quantised voltage, not automatically the physical quantity (1). Calibration relates readings to known reference conditions or a meaningful scale and checks sensor behaviour (1).

(c) States **off, on, on, off** (2: one mark for the initial pair, one for the second pair). Hysteresis reduces rapid switching caused by fluctuations near one threshold (1). The middle reading 35 preserves the prior on state.

(d) Verification checks implementation against intended rules (1). Validation checks whether the model/system is suitable for the real purpose (1). Simulation does not prove physical wiring, voltage compatibility, actual calibration or sensor accuracy: give one (1).

(e) Award one each for a concrete benefit to a named stakeholder, a distinct risk, a relevant mitigation and a reason connecting the mitigation to the risk. Example: staff receive timely warnings; a faulty sensor could cause misleading warnings; detect implausible readings and show an error; this makes a measurement fault visible instead of presenting it as a normal condition. Generic “good/bad” statements need a mechanism to earn credit.

## Section C — 50 marks

A complete reference is `code/exam-practice/practice_readings.py`. Run `python3 code/exam-practice/practice_readings.py`; it includes assert-based checks and prints the sample summary. Read it after attempting the task.

### (a) Structure — 5 marks

Award 1 for an appropriate `analyse(readings, threshold)` function, 1 for using the provided sample/threshold correctly, and 3 for a returned dictionary containing the five required fields (all five: 3; three or four: 2; one or two: 1). Printing alone does not satisfy the return contract.

### (b) Count and mean — 5 marks

Count based on input length (1); total accumulated or calculated correctly (1); division by count for non-empty input (1); explicit empty decision (1); `None` mean for empty input without division by zero (1).

### (c) Threshold count — 5 marks

Initial count of zero (1); visit each reading (1); compare against the supplied threshold (1); include equality (1); update and return the correct count (1). A sum of Boolean comparisons is also valid if explained correctly.

### (d) Longest consecutive run — 10 marks

Initial current and best lengths (2); traverse in original order (2); increment current for a qualifying reading (2); reset current on a non-qualifying reading (2); maintain the maximum including a run ending at the final element (2). Sorting first changes adjacency and cannot earn original-order points. A total count is not the longest run.

Worked trace for the sample at threshold 22:

| Reading | Qualifies? | Current run | Best run |
|---|---|---:|---:|
| 18 | No | 0 | 0 |
| 21 | No | 0 | 0 |
| 23 | Yes | 1 | 1 |
| 24 | Yes | 2 | 2 |
| 19 | No | 0 | 2 |
| 25 | Yes | 1 | 2 |

### (e) Median — 10 marks

Use a sorted copy, preserving the input (2); handle empty input with `None` (2); identify correct central index (2); odd length uses its middle value (2); even length averages the two middle values (2). The sample sorts to `18,19,21,23,24,25`, so `(21+23)/2 = 22`.

### (f) Validation — 5 marks

Reject non-numeric readings (1), reject Boolean readings (1), reject non-finite readings (1), apply the equivalent rules to the threshold (1), and raise a clear `ValueError` instead of silently altering bad input (1). Checks should happen before results are presented.

### (g) Tests — 10 marks

Two marks for each required category: 1 for meaningful input and 1 for its correct expected result or expected error.

- Empty list, threshold 22: count 0, mean/median `None`, qualifying count 0, longest run 0.
- Sample `[18,21,23,24,19,25]`, threshold 22: count 6, mean `130/6`, qualifying count 3, run 2, median 22.
- Final run `[1,5,6,7]`, threshold 5: longest run 3.
- Equality `[5,5,1,5]`, threshold 5: qualifying count 3 and longest run 2.
- Invalid input such as `[2,'bad']`, `[True]`, an infinite reading or a non-numeric threshold: `ValueError`.

Additional checks for an unchanged input list, odd/even medians and non-finite values strengthen the evidence but do not increase this mock's maximum score.

## Turn the score into action

Choose a repair at the smallest useful level. If the run ended incorrectly, trace the final loop iteration. If the median used the original order, contrast adjacency with numerical ordering. If a societal answer was vague, rewrite one feature-to-consequence explanation. Retry a new question later without looking at the repair. The evidence of transfer matters more than repeatedly marking the same corrected answer.

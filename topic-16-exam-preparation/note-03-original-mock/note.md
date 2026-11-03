# Original mixed-topic mock: community technology

This is a new educator-written practice assessment, **not an SEC examination or marking scheme**. Total: 100 marks. Suggested duration: 120 minutes, with 60 minutes for written sections A/B and 60 for practical section C. Answer all questions. Use Python 3 for the practical. Keep your first attempt before opening the worked guide. Ordinary Level learners may use the support prompts at the end and record that support; Higher Level learners should attempt the full task independently.

## Section A — ten short questions, 20 marks

Each question is worth 2 marks.

1. Write decimal 45 as an eight-bit unsigned binary number and as hexadecimal.
2. Complete the output column for `A AND NOT B` with inputs `00`, `01`, `10`, `11` in that order.
3. State one role of the program counter and one role of the arithmetic logic unit (ALU).
4. Contrast RAM and an SSD in terms of what happens to their contents when power is removed.
5. State the role of DNS and one protection provided by HTTPS during communication.
6. State the two outputs, in order: `x = 7; print(x // 2); print(x % 2)`.
7. Give one reason a form field needs a connected text label rather than only placeholder text, and one way to make keyboard focus visible.
8. Find the median of `9, 1, 3, 3`, showing the ordered middle values.
9. A function accepts integers from 10 to 20 inclusive. Give four values that test immediately inside and outside its two boundaries.
10. A dataset replaces student names with IDs but retains a separate ID-to-name lookup. Explain why this is not necessarily anonymous data.

## Section B — two investigations, 30 marks

### Question 11: a data claim — 15 marks

A fictional reading-area sensor records `4, 6, 6, 8, 100` in consistent units. The team claims that its single lunch sample proves the area is always quiet.

(a) Calculate the mean, showing the sum and count. **3 marks**

(b) Calculate the median and explain briefly why it differs from the mean here. **2 marks**

(c) Choose a suitable graph to show how readings change over successive sample times, and name one required label. **2 marks**

(d) A further CSV row contains a blank reading. Describe a defensible handling policy, distinguishing the blank from zero and preserving evidence. **3 marks**

(e) Another dataset shows that noise and visitor numbers rise together. Explain why this alone does not establish that visitor numbers caused all the noise. **2 marks**

(f) Identify one weakness in the “always quiet” claim and propose two features of a fairer sampling plan. **3 marks**

### Question 12: an automated indicator — 15 marks

A fictional study room has an analogue sensor, a digital enable button and a display. A program shows a warning when a calibrated reading is low. A simulation is used before connecting hardware.

(a) Identify one input, the processing decision and one output in this system. **3 marks**

(b) Explain why the raw ADC value is not automatically a meaningful physical unit and what calibration contributes. **2 marks**

(c) The warning turns on below 30 and off above 40, preserving its state in between. Starting off, trace the warning for levels `45, 29, 35, 41`, and explain the purpose of this design. **3 marks**

(d) Distinguish verification from validation in this project and state one thing the software simulation cannot establish about the physical system. **3 marks**

(e) Explain one benefit and one risk of automation for a named stakeholder, then propose a mitigation and justify it. **4 marks**

## Section C — original programming task, 50 marks

Save your solution as `practice_readings.py`. This name is only for this original mock. Write a function:

```python
def analyse(readings, threshold):
    # Return the specified summary dictionary.
```

`readings` is a list of finite real numbers; `threshold` is a finite real number. Booleans are not accepted as numbers for this task. Reject invalid values with a clear `ValueError`. Do not alter the caller's list. The returned dictionary must contain:

- `count`: number of readings.
- `mean`: arithmetic mean, or `None` when there are no readings.
- `at_or_above`: number of readings greater than or equal to the threshold.
- `longest_run`: length of the longest **consecutive** run at or above the threshold, in the original order. A below-threshold reading breaks a run.
- `median`: median of the readings, or `None` for an empty list.

For `[18, 21, 23, 24, 19, 25]` with threshold `22`, the count is 6, the mean is `130/6`, three readings meet the threshold, the longest qualifying run is 2 and the median is 22.

Implement and explain the following parts:

(a) Function structure, input example and the five correctly named return fields. **5 marks**

(b) Count and mean with explicit empty-input handling. **5 marks**

(c) Count values at or above the threshold, including equality. **5 marks**

(d) Calculate the longest consecutive qualifying run without sorting the original sequence. **10 marks**

(e) Calculate the median correctly for odd, even and empty lists, preserving the original list. **10 marks**

(f) Reject invalid numeric inputs as specified. **5 marks**

(g) Write five meaningful tests with expected results: an empty list; the supplied mixed example; a run ending at the final item; values equal to the threshold; and invalid input. **10 marks**

Print a readable summary for the sample, and include a short comment explaining why the run calculation must happen in the original order. The worked guide contains one reference implementation; other correct algorithms are welcome.

## Optional supported route

For a supported attempt, start with only `count`, `mean` and `at_or_above`, then add one field at a time. Trace a `current_run` counter and a `best_run` counter on paper before coding. For the median, sort a copy, calculate the middle index and split empty/odd/even cases. Ask a teacher for a partially completed trace if needed. Record the support used, then retry independently later. These supports are learning choices, not official level boundaries.

## After the attempt

Use the separate worked marking guide. Identify three specific repairs and choose a fresh archived question for each. Do not claim a grade conversion from this original assessment: its mark allocation was designed for feedback across skills.

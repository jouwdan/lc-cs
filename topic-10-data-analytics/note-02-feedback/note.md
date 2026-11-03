# 4. Answers: Data

Check your reasoning and repair one gap.

Check your attempt, then retry the step that caused difficulty.

## Practical checkpoints

| Values | Mean | Median | What this checks |
|---|---:|---:|---|
| `4, 6, 6, 12` | 7 | 6 | Even-length middle pair |
| `9, 1, 3, 3` | 4 | 3 | Sort before taking the middle |
| `7` | 7 | 7 | One item |
| Empty list | `None` | `None` | No division or indexing |
| `4, 6, 6, 120` | 34 | 6 | Effect of a large value |

Add the range only where the list is non-empty:

```python
if values:
    print('Range:', max(values) - min(values))
else:
    print('Range: None')
```

The original CSV has **8 accepted rows and 3 rejected rows**. A: count 4, mean 7, median 6. B: count 4, mean 3.75, median 4. Row 9 is blank; row 10 is non-numeric; row 11 is 130, outside the agreed range. The zero on row 12 is valid.

Changing only `unknown` to `5` gives B five readings: `3,5,7,5,0`. Their sum is 20, mean 4, and median 5. Rows 9 and 11 remain rejected. Keep the original source and your experimental copy separately.

Our mode convention returns every highest-frequency value. B's original four distinct values therefore all appear in the mode list; it is not a claim that any one value dominates.

A defensible conclusion: “In this fictional sample, B's median was 4 compared with A's 6, with four accepted observations each. This tiny dataset has no collection times, so it does not establish a general difference.”

## Quiz explanations

| Question | Correct choice | Why |
|---:|---|---|
| 1 | Mean room number is not room size | A room number identifies a category; it is not a physical measurement. |
| 2 | 3 | Sort to `1,3,3,9`; average the middle pair, 3 and 3. |
| 3 | Neither; use a stated missing-data policy | Missing is not a measured zero. |
| 4 | `csv.DictReader` | It handles CSV quoting, including commas inside fields. |
| 5 | `value IS NULL` | SQL uses this condition for missing/unknown values. |
| 6 | Unique for every record | A primary key must identify a row reliably. |
| 7 | An association, not proven causation | A third factor or sampling could explain the relationship. |
| 8 | Handle the empty case explicitly | No middle observation exists; use the stated `None` contract. |
| 9 | Values stay separate from SQL instructions | Parameters protect query structure; domain checks are still needed. |

**Retry:** if Question 2 was wrong, label sorted positions starting at zero. If Questions 3–4 were wrong, inspect the three rejected CSV rows. If database terms were unclear, explain the Area–Reading relationship with two paper tables before coding it.


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-10-data-analytics/note-03-exam-practice">5. Try one exam question</a>. <a href="https://tutors.dev/topic/lc-cs/topic-10-data-analytics">Back to the topic</a>.

---
order: 1
---
# 1. Learn: Data

Clean data and explain what it shows.

Find a useful answer without hiding missing values or claiming more than your sample shows.

**Start here:** read sections 1–5 in your first session. Return to sections 6–8 for databases. You need the lists and functions from Topics 06–07; you do not need to install a database app.

## 1. What does one row mean?

Our fictional readings compare areas A and B. Each row is one observation. The values are **practice scores on a 0–120 scale**, not real sound, health, or pupil measurements.

| Field | Meaning | Allowed values |
|---|---|---|
| `area` | Where the reading was taken | `A` or `B` |
| `value` | Practice reading | A finite number from 0 to 120 |

This small table is a **data dictionary**: it explains the fields and their rules. A real investigation would also record units, time, instrument, and collection method.

**Try:** room number 204, room temperature 21.5, number of chairs 28. Which two values make sense in an average?

**Check:** temperatures and chair counts. Room numbers are labels. A numerical-looking identifier does not become a measurement.

| Term | Plain meaning | Example |
|---|---|---|
| Qualitative | A category or description | Area A |
| Quantitative | A measurement or count | 28 chairs |
| Discrete | Separate countable values | Number of chairs |
| Continuous | A quantity that can vary between recorded values | Temperature |

## 2. Clean data without inventing it

Look at these four records:

```text
A,6
B,
B,unknown
B,0
```

The first and fourth contain valid readings. The blank and the word are missing/invalid measurements. **Do not change them to zero:** zero is already a valid measured value.

A cleaning log says which rows were rejected and why. Keep the original file unchanged so another person can check your decisions. A duplicate might be an accidental repeat or a genuine repeated observation; inspect its source or timestamp before deleting it. A large value might be an outlier rather than an error.

**Validation** checks a rule, such as “between 0 and 120”. **Verification** checks that data was copied as intended. Neither proves a plausible reading is factually correct.

**Try:** `130` fails our range rule. Does `110` prove the sensor worked?

**Check:** no. It passes the rule, but the instrument or collection process could still be wrong.

## 3. Work the statistics by hand

Use `4, 6, 6, 12` before writing code.

| Statistic | Calculation | Result |
|---|---|---:|
| Count | Number of values | 4 |
| Mean | `(4 + 6 + 6 + 12) / 4` | 7 |
| Median | Middle pair of sorted data: `(6 + 6) / 2` | 6 |
| Mode | Most frequent value | 6 |
| Range | `12 - 4` | 8 |

For odd-length data `12, 4, 6, 6, 2`, sort to `2, 4, 6, 6, 12`; the median is the middle item, 6. For even-length data average the middle pair. The mean here is also 6, but that agreement is not guaranteed.

**Try:** find the median of `9, 1, 3, 3`.

**Check:** sorted data are `1, 3, 3, 9`, so the median is 3. The mean is 4.

A **frequency** is a count of occurrences. For `1, 1, 2, 2`, both 1 and 2 tie for highest frequency. Our program returns all tied modes. Some classes use “no mode” when every value occurs equally often; state the convention you use. Frequencies should add up to the number of observations.

Empty data have no mean or median. Our function returns `None` for these and an empty mode list. Sort a **copy** when time order in the original data matters.

## 4. Explain what a statistic can hide

Replace 12 with 120 in `2, 4, 6, 6, 12`. The mean rises from 6 to 27.6; the median stays 6. The median resists this large isolated value. The mean still correctly expresses total divided by count. Choose the statistic that answers your question; do not remove a value simply because it weakens your claim.

A fair collection method matters as much as the formula. Measuring only the busiest hour can bias a sample. A larger biased sample is still biased.

A useful conclusion has four parts:

> In **this sample**, B's median was **4**, below A's **6**. Each area had **four valid observations**. The sample is too small and lacks time information to claim that B is always lower.

Two quantities may rise together: that is **correlation**. It does not prove one causes the other. Another factor could affect both.

## 5. Read a CSV and choose a graph

CSV is text organised into rows and fields. Quoted fields may contain commas, so use `csv.DictReader` rather than splitting every line at each comma. It gives you one row at a time with field names such as `row['value']`. Convert numeric text explicitly with `float`; keep conversion failures in the rejection log.

The practical gives you a working reader. First inspect its output, then change one rule. You are not expected to write a parser from memory.

| Graph | Use it for | Include |
|---|---|---|
| Bar chart | Comparing categories | Category labels and a meaningful baseline |
| Histogram | Numerical values grouped into intervals | Interval boundaries and frequency |
| Line graph | Change across time or another ordered scale | Ordered horizontal axis |
| Scatter plot | Relationship between two numerical variables | Both variables and units |

A title, labelled axes, units, and sample size help the reader interpret a graph. A cut-off bar-chart axis can exaggerate a difference. A table is enough for our small dataset; decoration is not a substitute for an explanation.

## 6. A database is a collection of structured records

A table has **records** (rows) and **fields** (columns). A **primary key** uniquely identifies a record. Two pupils or books may have the same name, so names are often poor keys.

**Higher Level depth: related tables.** Store `Area(area_id, name)` once, and let each `Reading(reading_id, area_id, value)` refer to an area through a **foreign key**. One area can have many readings. This avoids repeatedly typing an area name and creating inconsistent spellings. A **join** matches related keys to bring fields together. Topic 13 lets you run a complete two-table example.

## 7. Read a query one clause at a time

```sql
SELECT area, AVG(value) AS mean_value
FROM reading
WHERE value IS NOT NULL
GROUP BY area
ORDER BY area;
```

1. `FROM` names the table.
2. `WHERE` keeps rows with a measurement.
3. `GROUP BY` puts each area's rows together.
4. `AVG` calculates a mean for each group.
5. `ORDER BY` makes the output order explicit.

`NULL` represents missing/unknown data. Check it with `IS NULL`, not `= NULL`. `COUNT(*)` counts rows; `COUNT(value)` skips null values.

**Try:** with A readings 4, 6, 6, 12 and B readings 3, 5, 7, 0, predict the two means.

**Check:** A is 7; B is 3.75. The optional database script prints these without needing a database installation: Python includes SQLite.

## 8. Keep input separate from SQL instructions

Use a placeholder for a value supplied by a user:

```python
db.execute('SELECT * FROM reading WHERE area = ?', (area,))
```

The `?` receives a value. It does not turn that text into SQL instructions. This helps prevent SQL injection; the program must still check allowed values such as area A or B. Database basics belong in the shared course; relational design and longer query reasoning add Higher Level depth.

**Before practice:** explain why a blank is not zero, calculate an even-length median, and say what a primary key identifies. If one is unclear, retry that worked example first.


---

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-10-data-analytics/book-01-practice">2. Practise</a>. <a href="https://tutors.dev/note/lc-cs/topic-10-data-analytics/note-02-feedback">Open the answers when you have tried it</a>.

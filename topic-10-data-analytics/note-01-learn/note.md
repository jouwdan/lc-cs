# Data, databases and analytics

Concepts, worked examples and practical reasoning for data, databases and analytics.

## What you will be able to do

Classify data; clean a CSV file without hiding errors; calculate and interpret descriptive statistics; design a small database; and justify a conclusion with evidence and limitations. Prerequisites are Python variables, lists, loops, functions and file handling. Work with synthetic classroom data here: no names, health records or identifiable student results are needed.

## Start with a question

A dataset is useful when its fields answer a question. “Which reading area is quieter during lunch?” needs sound measurements, location, time, units and a sampling method. A collection of unexplained numbers cannot answer it reliably. Decide what each row represents before coding. A data dictionary records field name, meaning, units, allowed values, missing-value convention and source. For example, `sound_db` is a real-valued measurement, `area` is a category, and `count` is a discrete integer.

Continuous quantities such as temperature can take values between observations even when a sensor rounds them. Discrete quantities such as the number of books are counted. Qualitative data describes categories; quantitative data measures or counts. A numeric room identifier is still a label: calculating its average usually has no meaning. Data types in a program should reflect how the data will be used, not merely how it looks in a spreadsheet.

## Collection and quality

Use a consistent procedure, sample across relevant times and record conditions. Taking every measurement beside the loudest speaker introduces selection bias. A larger biased sample remains biased. Missing values are not automatically zero. A sensor reading of zero may be genuine; a blank cell means something different. Keep the original file and write cleaned output separately, so decisions can be reviewed.

Validation checks whether a value follows a rule. A temperature between −20 and 60 degrees might be plausible for a classroom sensor project, but passing that range check does not prove the measurement is correct. Verification checks that data was copied or entered as intended. A duplicate row might be an accidental repeat or a valid repeated observation; inspect its timestamp and provenance before deleting it. Report how many rows were excluded and why.

CSV stores text with delimiters and quoting rules. Use Python's `csv.DictReader`, rather than `line.split(',')`, because quoted text may contain commas. Convert numeric fields explicitly. Catch expected conversion errors and record rejected row numbers; do not silently replace every error with zero. Strip incidental surrounding whitespace when the field definition allows it. Preserve units and avoid mixing Celsius and Fahrenheit in one numeric column.

## Statistics with a worked example

Consider the readings `12, 4, 6, 6, 2`. Their sum is 30 and count is 5, so their mean is 6. Sort to obtain `2, 4, 6, 6, 12`: the median is the central value 6, the mode is 6 and the range is 10. With `2, 4, 6, 12`, the median is `(4 + 6) / 2 = 5`; it is not either central value alone. A frequency table counts each distinct value. Frequencies must sum to the number of observations.

There may be several tied modes. State the convention your program uses: returning all values with maximum frequency is explicit and useful. An empty dataset has no mean or median; return `None` or raise a clear error according to the stated contract. Do not divide by zero. Sorting a copy preserves the caller's original order, which may encode time.

An outlier affects summaries differently. Replacing 12 with 120 increases the mean from 6 to 27.6, while the median stays 6. Neither statistic is automatically “best”: the mean describes total divided across observations; the median resists a very large isolated value. Explain which question the statistic answers. Never remove a surprising observation only because it weakens your hypothesis.

## Graphs and conclusions

A bar chart compares categories; a histogram groups numerical values into intervals; a line graph shows a meaningful progression such as time; a scatter plot explores two numerical variables. Give axes labels, units and a title. A truncated vertical axis can exaggerate differences, especially in bar charts where length represents magnitude. Mention sample size and the period represented. An attractive graph does not repair poor sampling.

Correlation means two variables vary together. It does not establish that one causes the other: another factor may affect both, or the relationship may be coincidental. A claim should follow a simple structure: observation, numerical evidence, interpretation, limitation, next measurement. “Area B had a lower median in our ten lunch samples” is defensible; “Area B is always silent” is not. Preserve uncertainty instead of inventing precision.

## Databases: meaning before syntax

A table contains records (rows) and fields (columns). Choose data types and constraints. A primary key uniquely identifies each record; it need not describe the record to a human. A foreign key refers to a key in another table. In a borrowing system, `Book(book_id, title)` and `Loan(loan_id, book_id, returned)` avoid repeating book details in every loan. The relationship is one book to many loan records over time. A spreadsheet can store a table, but a database also provides controlled querying and integrity rules.

**Higher Level extension:** relational design is specifically emphasised in the legacy specification. Explain why storing a title once reduces inconsistent updates, how keys join related records, and why a join may return more rows than one input table. Do not claim that all database knowledge is Higher Level only.

```sql
SELECT area, AVG(sound_db) AS mean_sound
FROM reading
WHERE sound_db IS NOT NULL
GROUP BY area
ORDER BY mean_sound;
```

`WHERE` selects rows before grouping. `AVG` produces one mean per group. `ORDER BY` determines result order; without it, do not rely on insertion order. `NULL` means missing/unknown, so test it with `IS NULL`, not `= NULL`. `COUNT(*)` counts rows; `COUNT(sound_db)` excludes null values. Explain each clause in words before memorising syntax.

When a value comes from user input, use placeholders: `db.execute('SELECT * FROM reading WHERE area = ?', (area,))`. Concatenating user text into SQL mixes data with instructions and may create injection vulnerabilities. Parameters preserve the distinction. Use synthetic data and local databases in practice.

## Transfer to examinations

The 2022 Higher Level practical asks learners to work with dice frequencies and a chart; the 2025 Higher Level practical includes grade statistics and median cases. Use the archived paper's wording and its matching scheme for exact requirements. Our examples use different contexts. In a programming answer, show initial values, update logic and the empty/even/odd decisions clearly. In an explanation, attach each statistical choice to the question being investigated.

## Check your understanding

Explain why a room number should not be averaged, why a blank is not a zero, and why a correct formula can still support a weak conclusion. Calculate the median of `9, 1, 3, 3` and describe a test that would expose a median function that never sorts its input. Then design two related tables for a school equipment library and identify their keys. Success means explaining the decisions, not only producing output.

Source for curriculum alignment: [legacy specification](https://www.curriculumonline.ie/getmedia/cff6eb86-9ff8-4e68-abf9-e42ca637492d/LC-Computer-Science-specification-updated.pdf), outcomes 2.16–2.18 and 3.2–3.7.

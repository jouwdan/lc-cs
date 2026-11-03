# 10 · Data, databases and analytics: quiz feedback

Use these explanations after your first attempt. Correct the reasoning, then retry after a delay.

## Question 1

**Answer: Calculating the mean room number as a measure of room size.** The digits identify a category. Arithmetic does not turn an identifier into a meaningful physical measurement.

## Question 2

**Answer: 3.** Sort to 1, 3, 3, 9. The middle pair is 3 and 3, whose average is 3. The mean is 4.

## Question 3

**Answer: Neither; apply and document a missing-data policy.** Missing is not a measured zero. Preserve the distinction and explain exclusion or justified replacement.

## Question 4

**Answer: Use csv.DictReader.** The csv module understands quoting. A naive split can produce the wrong number of fields.

## Question 5

**Answer: value IS NULL.** NULL represents missing/unknown. SQL provides IS NULL rather than equality for this check.

## Question 6

**Answer: Unique for every record.** Uniqueness identifies a row reliably. Names can repeat and may be inappropriate personal data.

## Question 7

**Answer: A relationship is observed, but causation needs further evidence.** Confounding, coincidence and sampling can produce associations. Explain limits and design further evidence.

## Question 8

**Answer: Handle the empty case according to an explicit contract.** There is no middle observation. A documented None or clear error is safer than an index or division failure.

## Question 9

**Answer: They keep values separate from SQL instructions.** Parameters prevent supplied text being interpreted as SQL syntax; domain validation remains necessary.

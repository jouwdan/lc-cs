---
order: 3
---
# 3. Quiz: Data

Test yourself, then check the answers.

Nine quick questions to find the idea you should practise next.

Try without notes. This is a formative self-check: answers and scores are not recorded. For each mistake, read its explanation, retry the small worked example, then try again.

````quiz
title: 10 · Data, databases and analytics
---
question: A room number is stored as 204. Which operation is usually meaningless?
type: multiple-choice
options:
  - Checking whether it equals a requested room
  - Calculating the mean room number as a measure of room size
  - Using it to look up a room
correct: 1
---
question: What is the median of 9, 1, 3, 3?
type: multiple-choice
options:
  - 3
  - 4
  - 6
correct: 0
---
question: What should a missing sensor reading become automatically?
type: multiple-choice
options:
  - Zero
  - The largest reading
  - Neither; apply and document a missing-data policy
correct: 2
---
question: Which CSV reading approach correctly handles quoted commas?
type: multiple-choice
options:
  - Split every line on a comma
  - Use csv.DictReader
  - Remove all quotation marks first
correct: 1
---
question: Which SQL condition checks for missing values?
type: multiple-choice
options:
  - value = NULL
  - value IS NULL
  - value == missing
correct: 1
---
question: A primary key must be what?
type: multiple-choice
options:
  - Unique for every record
  - A person’s name
  - A decimal measurement
correct: 0
---
question: Two measurements correlate. What follows?
type: multiple-choice
options:
  - One definitely causes the other
  - A relationship is observed, but causation needs further evidence
  - Both measurements are wrong
correct: 1
---
question: For an empty list, what should a median function do?
type: multiple-choice
options:
  - Return the first element
  - Divide its sum by its length
  - Handle the empty case according to an explicit contract
correct: 2
---
question: Why use SQL placeholders for user values?
type: multiple-choice
options:
  - They keep values separate from SQL instructions
  - They make every query run in constant time
  - They remove the need to validate domain values
correct: 0
````


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-10-data-analytics/note-02-feedback">4. Read the answers and explanations</a>. <a href="https://tutors.dev/topic/lc-cs/topic-10-data-analytics">Back to the topic</a>.

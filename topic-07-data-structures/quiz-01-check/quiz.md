# 3. Quiz: Lists & files

Test yourself, then check the answers.

Allow 10 minutes. Answer all 10 questions without notes or running code. Submit, then write down the numbers you want to revisit. Scores are not saved.

Some questions use the extension examples. Read their worked lesson sections first; you do not need to have implemented every extension.

After your attempt, use **4. Answers** to explain each correction, then retry the missed questions.

````quiz
question: What is `"COMPUTER"[1:4]`?
type: multiple-choice
options:
  - COM
  - OMP
  - OMPU
  - MPU
correct: 1
---
question: What does this print?
```python
a = [4, 7]
b = a
b.append(9)
print(a)
```
type: multiple-choice
options:
  - [4, 7]
  - [9]
  - [4, 7, 9]
  - None
correct: 2
---
question: What does list.sort() return?
type: multiple-choice
options:
  - A sorted copy
  - The first element
  - True
  - None
correct: 3
---
question: A function that prints a value automatically returns that same value.
type: true-false
correct: false
---
question: What is the median of [9, 2, 7, 4]?
type: multiple-choice
options:
  - 4
  - 7
  - 5.5
  - 6.5
correct: 2
---
question: Which input must be handled before taking the first element as a minimum?
type: multiple-choice
options:
  - A list with duplicates
  - An empty list
  - A list with four numbers
  - A sorted list
correct: 1
---
question: What is the longest strictly increasing consecutive run in [3, 5, 2, 4, 7, 7, 9]?
type: multiple-choice
options:
  - [3, 5, 7, 9]
  - [2, 4, 7]
  - [2, 3, 4, 5, 7, 9]
  - [7, 7, 9]
correct: 1
---
question: A digit-sum modulo-10 check digit detects every transposition of two digits.
type: true-false
correct: false
---
question: Why use csv.DictReader rather than splitting each line at every comma?
type: multiple-choice
options:
  - It encrypts data
  - It guarantees that all values are valid
  - It handles quoted commas and maps columns by header
  - It makes every field an integer
correct: 2
---
question: If two independent password-scoring conditions can both earn points, an if/elif chain always implements them correctly.
type: true-false
correct: false
````

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-07-data-structures/note-02-feedback">4. Answers: check your reasoning</a>. <a href="https://tutors.dev/note/lc-cs/topic-07-data-structures/note-02-feedback">Open the answers</a>.

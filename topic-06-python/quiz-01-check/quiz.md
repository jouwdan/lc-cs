---
order: 3
---
# 3. Quiz: Python

Test yourself, then check the answers.

Allow 10 minutes. Answer all 10 questions without notes or running code. Submit, then write down the numbers you want to revisit. Scores are not saved.

After your attempt, use **4. Answers** to explain each correction, then retry the missed questions.

````quiz
question: What type does input() return?
type: multiple-choice
options:
  - int
  - float
  - str
  - bool
correct: 2
---
question: What is 17 // 5?
type: multiple-choice
options:
  - 3
  - 3.4
  - 2
  - 4
correct: 0
---
question: What does this print?
```python
total = 0
for n in range(1, 4):
    total += n
print(total)
```
type: multiple-choice
options:
  - 3
  - 4
  - 6
  - 10
correct: 2
---
question: Which expression accepts only percentages between 0 and 100 inclusive?
type: multiple-choice
options:
  - score >= 0 or score <= 100
  - 0 <= score <= 100
  - score > 0 and score < 100
  - score == 0 and score == 100
correct: 1
---
question: An if/elif/else chain executes the first branch whose condition is true.
type: true-false
correct: true
---
question: What is the result of `"3" + "4"`?
type: multiple-choice
options:
  - 7
  - 34 as an integer
  - `"34"` as a string
  - A syntax error
correct: 2
---
question: Which is a logical error?
type: multiple-choice
options:
  - A missing colon
  - Converting `"hello"` with `int()`
  - Using > when the required boundary is inclusive
  - Dividing by zero
correct: 2
---
question: A while loop always executes its body at least once.
type: true-false
correct: false
---
question: What does `f"{2.5:.2f}"` display?
type: multiple-choice
options:
  - 2.5
  - 2.50
  - 3.00
  - 2
correct: 1
---
question: Why must a running total normally be initialised before the loop?
type: multiple-choice
options:
  - So it resets after every item
  - So previous additions are preserved
  - So it becomes a string
  - So the loop runs forever
correct: 1
````

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-06-python/note-02-feedback">4. Answers: check your reasoning</a>. <a href="https://tutors.dev/note/lc-cs/topic-06-python/note-02-feedback">Open the answers</a>.

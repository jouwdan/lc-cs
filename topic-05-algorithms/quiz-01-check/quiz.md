---
order: 3
---
# 3. Quiz: Algorithms

Test yourself, then check the answers.

Allow 10 minutes. Answer all 10 questions without notes or running code. Submit, then write down the numbers you want to revisit. Scores are not saved.

After your attempt, use **4. Answers** to explain each correction, then retry the missed questions.

````quiz
question: Which is the most useful decomposition of a bus-booking task?
type: multiple-choice
options:
  - Read and validate passengers, calculate buses, report result
  - Split the program after every five lines
  - Write all calculations in one unnamed block
  - Remove the passenger count
correct: 0
---
question: Which detail should be retained in an abstraction for bus capacity?
type: multiple-choice
options:
  - Paint colour
  - Available passenger seats
  - Radio station
  - Seat fabric
correct: 1
---
question: For 37 passengers and capacity 12, how many buses are needed?
type: multiple-choice
options:
  - 2
  - 3
  - 4
  - 37
correct: 2
---
question: What is the output?
```text
count ← 0
FOR EACH value IN [50, 49, 80]
    IF value >= 50 THEN
        count ← count + 1
    ENDIF
ENDFOR
OUTPUT count
```
type: multiple-choice
options:
  - 0
  - 1
  - 2
  - 3
correct: 2
---
question: A decision diamond should have labelled exits so the conditions for following each path are clear.
type: true-false
correct: true
---
question: Which tests best target a threshold of 50?
type: multiple-choice
options:
  - 10, 20, 30
  - 49, 50, 51
  - 60, 70, 80
  - 0, 10, 100
correct: 1
---
question: A nearest-next-stop heuristic always produces the shortest complete route.
type: true-false
correct: false
---
question: Which statement describes generalisation?
type: multiple-choice
options:
  - Record only the answer for 29 passengers
  - Use one input-independent answer
  - Express a rule using passenger count and capacity
  - Remove every boundary case
correct: 2
---
question: For a loop that repeats while a condition is true and has no other exit, what must happen?
type: multiple-choice
options:
  - Its condition must eventually become false
  - It must always execute exactly once
  - It must print a value in every iteration
  - Its condition must always be true
correct: 0
---
question: Changing a counter from adding 1 to adding the matching value still counts the number of matching items.
type: true-false
correct: false
````

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-05-algorithms/note-02-feedback">4. Answers: check your reasoning</a>. <a href="https://tutors.dev/note/lc-cs/topic-05-algorithms/note-02-feedback">Open the answers</a>.

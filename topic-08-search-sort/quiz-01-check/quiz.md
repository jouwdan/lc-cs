# 3. Quiz: Search & sort

Test yourself, then check the answers.

Allow 10 minutes. Answer all 10 questions without notes or running code. Submit, then write down the numbers you want to revisit. Scores are not saved.

Some questions use the extension examples. Read their worked lesson sections first; you do not need to have implemented every extension.

After your attempt, use **4. Answers** to explain each correction, then retry the missed questions.

````quiz
question: Which precondition is essential for binary search?
type: multiple-choice
options:
  - All values are positive
  - The list has an even length
  - The list is sorted under the comparison rule
  - The target is definitely present
correct: 2
---
question: In an ascending binary search, target < values[middle]. What update excludes the impossible region?
type: multiple-choice
options:
  - low = middle
  - high = middle - 1
  - high = middle + 1
  - low = high
correct: 1
---
question: After the first full left-to-right bubble-sort pass on [7, 2, 5, 1], what is the list?
type: multiple-choice
options:
  - [1, 2, 5, 7]
  - [2, 7, 5, 1]
  - [2, 5, 1, 7]
  - [7, 5, 2, 1]
correct: 2
---
question: Selection sort must remove a selected minimum from the source in its two-list version.
type: true-false
correct: true
---
question: Which statement best describes insertion sort?
type: multiple-choice
options:
  - Repeatedly halve a search interval
  - Insert the next item into a sorted prefix
  - Choose a random final answer
  - Only compare the first and last elements
correct: 1
---
question: A correct recursive function needs a base case and progress towards that case.
type: true-false
correct: true
---
question: What is gcd(48, 18)?
type: multiple-choice
options:
  - 3
  - 6
  - 12
  - 18
correct: 1
---
question: What is the worst-case time growth of binary search on sorted data?
type: multiple-choice
options:
  - O(1) for every input
  - O(log n)
  - O(n)
  - O(n²)
correct: 1
---
question: Quicksort always takes O(n log n) time, regardless of partition quality.
type: true-false
correct: false
---
question: For the inclusive binary-search version in these notes, how many middle-item probes can an absent target require in 8 items?
type: multiple-choice
options:
  - 1
  - 2
  - 3
  - 4
correct: 3
````

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-08-search-sort/note-02-feedback">4. Answers: check your reasoning</a>. <a href="https://tutors.dev/note/lc-cs/topic-08-search-sort/note-02-feedback">Open the answers</a>.

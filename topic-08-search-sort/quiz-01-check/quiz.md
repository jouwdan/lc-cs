# Search, sort, and recursion check

A formative self-check: answers and scores are not recorded.

Answer without running code first. After submitting, explain each answer in your own words and use the separate feedback note. The answer key is visible in the source; this is practice, not a secure assessment.

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

# Design and testing check

A formative self-check: answers and scores are not recorded.

Answer without running code first. After submitting, explain each answer in your own words and use the separate feedback note. The answer key is visible in the source; this is practice, not a secure assessment.

````quiz
question: Which requirement is most directly testable?
type: multiple-choice
options:
  - Make it good
  - Make it modern
  - Accept quantities 1 to 8 inclusive and reject all other integers
  - Make it attractive
correct: 2
---
question: Which is a boundary test for a discount that begins at 5 tickets?
type: multiple-choice
options:
  - Only quantity 2
  - Quantities 4, 5, and 6
  - Only quantity 7
  - Only a blank screen
correct: 1
---
question: What does regression testing check?
type: multiple-choice
options:
  - That old working behaviour still works after a change
  - Only that a logo is visible
  - That all code is rewritten
  - That no future bug can ever occur
correct: 0
---
question: A calculation function passing unit tests proves the entire interface works correctly.
type: true-false
correct: false
---
question: Which example is primarily non-functional?
type: multiple-choice
options:
  - The total for 5 tickets is 5000 cents
  - Invalid quantities are rejected
  - The result appears within an agreed response-time threshold
  - The function returns an integer
correct: 2
---
question: A test oracle supplies the expected result against which actual behaviour is compared.
type: true-false
correct: true
---
question: What are the final values of x and y in JavaScript?
```javascript
let x = 4;
let y = x++;
```
type: multiple-choice
options:
  - x = 4, y = 5
  - x = 5, y = 4
  - x = 5, y = 5
  - x = 4, y = 4
correct: 1
---
question: What does JavaScript 3 === "3" evaluate to?
type: multiple-choice
options:
  - true
  - false
  - "33"
  - 7
correct: 1
---
question: Which is the best next step after reproducing a bug?
type: multiple-choice
options:
  - Change several unrelated lines
  - Delete the failing test
  - Reduce the failing case and test a specific hypothesis
  - Assume the user made a mistake
correct: 2
---
question: Complete branch coverage guarantees that the software has no faults.
type: true-false
correct: false
````

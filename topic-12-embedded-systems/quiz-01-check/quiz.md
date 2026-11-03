# 3. Quiz: Embedded

Test yourself, then check the answers.

Nine quick questions to find the idea you should practise next.

Try without notes. This is a formative self-check: answers and scores are not recorded. For each mistake, read its explanation, retry the small worked example, then try again.

````quiz
title: 12 · Embedded systems
---
question: Which device is an input?
type: multiple-choice
options:
  - A moisture sensor
  - A warning LED
  - A motor
correct: 0
---
question: Ten bits can represent how many distinct codes?
type: multiple-choice
options:
  - 10
  - 1023
  - 1024
correct: 2
---
question: Dry is 800, wet is 300 and raw is 550. What is the relative level?
type: multiple-choice
options:
  - 50
  - 55
  - Cannot be calculated because wet is lower
correct: 0
---
question: What if dry and wet calibration readings are equal?
type: multiple-choice
options:
  - Assume 50%
  - Reject the calibration and investigate
  - Divide anyway
correct: 1
---
question: A warning is on; the level rises to 35. On below 30, off above 40. What happens?
type: multiple-choice
options:
  - It stays on
  - It turns off
  - It toggles repeatedly
correct: 0
---
question: Does a successful simulator test prove the sensor is calibrated?
type: multiple-choice
options:
  - Yes
  - No
  - Only with many random values
correct: 1
---
question: What does micro:bit write_analog produce?
type: multiple-choice
options:
  - A continuously adjustable analogue voltage
  - PWM with varying duty cycle
  - A CSV file
correct: 1
---
question: Why might a very long blocking delay be unsuitable?
type: multiple-choice
options:
  - It always makes measurement more accurate
  - It may delay response to a stop or enable input
  - It changes every input to analogue
correct: 1
---
question: An embedded system must have an Internet connection.
type: multiple-choice
options:
  - True
  - False
  - Only if it has a processor
correct: 1
````


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-12-embedded-systems/note-02-feedback">4. Read the answers and explanations</a>. <a href="https://tutors.dev/topic/lc-cs/topic-12-embedded-systems">Back to the topic</a>.

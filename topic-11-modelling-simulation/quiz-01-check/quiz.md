# 11 · Modelling and simulation: retrieval check

Attempt without notes, then explain your choices using the feedback note.

````quiz
title: 11 · Modelling and simulation
---
question: What is a simulation?
type: multiple-choice
options:
  - A run of a model’s rules to explore behaviour
  - Any stored dataset
  - A guaranteed prediction
correct: 0
---
question: Which is a state variable in the queue model?
type: multiple-choice
options:
  - Queue length during the run
  - The chosen run duration
  - The fixed seed
correct: 0
---
question: What does random.Random(7) primarily support?
type: multiple-choice
options:
  - Perfect realism
  - Reproducibility of a pseudo-random sequence
  - Elimination of sampling bias
correct: 1
---
question: Which call includes both die endpoints?
type: multiple-choice
options:
  - randrange(1, 6)
  - randint(1, 6)
  - random()
correct: 1
---
question: A program follows its rules but ignores a crucial real factor. Which issue remains?
type: multiple-choice
options:
  - Model validation
  - Only syntax checking
  - None
correct: 0
---
question: Why repeat stochastic runs?
type: multiple-choice
options:
  - Every run must give the same result
  - To examine variability and estimate typical outcomes
  - To guarantee the model’s assumptions are true
correct: 1
---
question: What is emergence?
type: multiple-choice
options:
  - A system-level pattern arising from local interactions
  - An agent knowing the final answer
  - A syntax error appearing late
correct: 0
---
question: With arrivals first, initial queue 0, arrivals 1,1,1 and service 0,1,0, what is the final queue?
type: multiple-choice
options:
  - 1
  - 2
  - 3
correct: 1
---
question: Mean queue length is automatically mean waiting time.
type: multiple-choice
options:
  - Yes, both are averages
  - No, their units and definitions differ
  - Only if a random seed is used
correct: 1
````

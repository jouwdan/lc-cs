# 11 · Modelling and simulation: quiz feedback

Use these explanations after your first attempt. Correct the reasoning, then retry after a delay.

## Question 1

**Answer: A run of a model’s rules to explore behaviour.** A model represents selected aspects of a system; simulation executes its rules. Its outputs remain conditional on assumptions.

## Question 2

**Answer: Queue length during the run.** Queue length changes as events occur. Duration and seed configure the experiment.

## Question 3

**Answer: Reproducibility of a pseudo-random sequence.** A seed lets you repeat a sequence. It does not validate assumptions or make an unrepresentative dataset representative.

## Question 4

**Answer: randint(1, 6).** randint includes 1 and 6. randrange excludes its stop value; random returns a real value from 0 inclusive to 1 exclusive.

## Question 5

**Answer: Model validation.** Verification concerns implementing rules correctly. Validation concerns suitability for the real purpose.

## Question 6

**Answer: To examine variability and estimate typical outcomes.** Repeated runs expose sampling variation. They cannot remove systematic errors in model design.

## Question 7

**Answer: A system-level pattern arising from local interactions.** Individual local rules can generate a collective pattern that is not directly specified as a global instruction.

## Question 8

**Answer: 2.** The states are 1, then 1 after one arrival and one service, then 2 after another arrival without service.

## Question 9

**Answer: No, their units and definitions differ.** Queue length counts people; waiting time measures duration. Track arrival and departure times if waiting is required.

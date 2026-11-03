# Algorithms: feedback and model reasoning

Use these explanations after completing the quiz and lab.

## Quiz explanations

1. **Read/validate, calculate, report.** Each part has a purpose and can be checked separately. Arbitrary line counts do not represent the problem's structure.
2. **Available passenger seats.** Capacity affects the answer; colour does not in this model. An abstraction retains relevant detail.
3. **4 buses.** Three buses hold 36 passengers, leaving one passenger. Integer division gives 3 and the nonzero remainder requires one more.
4. **2.** Both 50 and 80 qualify; 49 does not. The equality boundary matters.
5. **True.** A decision chooses a path. Labels make that choice unambiguous.
6. **49, 50, 51.** These reveal confusion between `<`, `<=`, `>` and `>=` at the stated boundary.
7. **False.** A locally short step can create a costly later step. A heuristic does not automatically guarantee global optimality.
8. **A rule using count and capacity.** It handles a class of inputs rather than one memorised example.
9. **The condition eventually becomes false.** The question excludes explicit exits such as `break` or `return`. For condition-based termination, progress and a suitable condition are required; printing does not provide either.
10. **False.** Adding the value produces an accumulator total. Adding one produces a count.

## Lab model

Inputs are `passengers` and `capacity`. The output is the smallest whole bus count whose combined capacity is at least the passenger count. Valid passengers are integers at least zero; capacity is a positive integer. Do not silently round an invalid passenger value.

| Passengers | Capacity | Quotient | Remainder | Buses |
|---:|---:|---:|---:|---:|
| 0 | 12 | 0 | 0 | 0 |
| 1 | 12 | 0 | 1 | 1 |
| 11 | 12 | 0 | 11 | 1 |
| 12 | 12 | 1 | 0 | 1 |
| 13 | 12 | 1 | 1 | 2 |
| 24 | 12 | 2 | 0 | 2 |
| 25 | 12 | 2 | 1 | 3 |

The model's key calculation is:

```python
buses = passengers // capacity
if passengers % capacity > 0:
    buses += 1
```

The version that always adds one fails at zero and exact multiples. Changing the condition to `>= 0` reproduces that defect because a remainder is never negative for these valid inputs. Your test suite should catch it at 0, 12, and 24.

The complete checked source is [`solutions.py` on GitHub](https://github.com/jouwdan/lc-cs/blob/main/code/topic-05-algorithms/solutions.py). Run `python3 code/topic-05-algorithms/solutions.py` from the repository root. The successful output is `Topic 05 checks passed`.

For the threshold task the trace counts are 0, 1, 2, 2 after the four values. Zero items produce a zero count. For two exact threshold values the result is two.

For the extension, the quotient-and-remainder method uses a fixed small number of arithmetic operations for the input sizes considered here. Repeated subtraction needs one iteration per bus, so it performs more iterations as the passenger count rises. Neither comparison says anything about fairness of allocating seats: that depends on requirements and policy.

## Corrective practice

If the trace was wrong, make a row after every assignment for a two-item example. If abstraction was vague, write “I keep ___ because ___; I omit ___ because ___.” If boundary tests were missing, circle every comparison operator and invent one test on each side of it. Repeat the quiz only after you can explain the corrected reasoning.

## State-space feedback

Moving A first leaves B and C together on the left without the robot. Moving C first similarly leaves A and B together. Moving B first is safe. The valid seven-trip state trace is printed in the concepts note. Returning B on trip four permits C to cross without leaving a forbidden pair unattended.

The checker models each move as an edge in a finite graph, rejects unsafe states, and explores breadth-first. Its returned path has eight states, including the start: eight states represent seven moves. A visited-state set prevents an endless left/right cycle. It finds a shortest path because every edge represents one trip and it explores by trip count.

In the game, three counters give legal successors 2 and 1, both winning for the opponent. Four counters have a move to the opponent's losing position 3. This is adversarial reasoning: a helpful opponent cannot be assumed.

For the two-pile supplement, the winning move from `(1,3)` removes two from the second pile and leaves `(1,1)`. Both possible opponent replies leave one final counter for you. Equal pairs are losing; unequal pairs can be equalised by reducing the larger one. For three equal positive piles, remove an entire pile and leave the equal pair. These claims use the explicit normal-play rule that the last taker wins.

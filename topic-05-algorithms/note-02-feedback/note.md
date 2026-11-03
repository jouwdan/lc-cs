# 4. Answers: Algorithms

Check your reasoning and repair one gap.

Use this after an attempt. Find the question or lab step you missed, explain the correction in one sentence, then rerun that case yourself.

## Quiz explanations

1. **Read/validate, calculate, report.** Each part has a purpose and can be checked separately. Arbitrary line counts do not represent the problem's structure.
2. **Available passenger seats.** Capacity affects the answer; colour does not in this model. An abstraction retains relevant detail.
3. **4 buses.** Three buses hold 36 passengers, leaving one passenger. Integer division gives 3 and the nonzero remainder requires one more.
4. **2.** Both 50 and 80 qualify; 49 does not. The equality boundary matters.
5. **True.** A decision chooses a path. Labels make that choice unambiguous.
6. **49, 50, 51.** These reveal confusion between `<`, `<=`, `>` and `>=` at the stated boundary.
7. **False.** A locally short step can create a costly later step. A heuristic does not automatically guarantee global optimality.
8. **A rule using count and capacity.** It handles a class of inputs rather than one memorised example.
9. **The condition eventually becomes false.** The question has no other exit. For condition-based termination, progress and a suitable condition are required; printing does not provide either.
10. **False.** Adding the value produces an accumulator total. Adding one produces a count.


## Your bus plan

A useful specification says: accept a whole-number passenger count of zero or more; use 12 passenger seats per bus; return the fewest whole buses; report invalid input. Drivers do not use these seats. Keep seat capacity and omit colour because only the former affects this calculation.

| Passengers | Quotient | Remainder | Buses |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 11 | 0 | 11 | 1 |
| 12 | 1 | 0 | 1 |
| 13 | 1 | 1 | 2 |
| 24 | 2 | 0 | 2 |
| 25 | 2 | 1 | 3 |

The missing pseudocode condition is `passengers MOD 12 > 0`; the update is `buses ← buses + 1`. Always adding one fails for 0, 12 and 24. Changing the condition to `>= 0` makes the same mistake because all these valid remainders are non-negative.

A model explanation: “The algorithm finds how many complete groups of 12 fit into the passenger count. If a positive remainder exists, it adds one bus for those passengers. Zero gives quotient and remainder zero, so no bus is added. Tests 11, 12 and 13 check both sides of the capacity boundary.”

For the score counter, the successive counts are 0, 1, 2, 2. Empty input gives 0; `[50,50]` gives 2. Adding the matching scores would give a total, not a count.

## Optional extensions

31 and 32 passengers at capacity 16 both need 2 buses. Repeated subtraction needs one iteration per bus; the quotient-and-remainder method uses a fixed small number of arithmetic operations for the input sizes considered.

In the robot puzzle, only taking B first is safe. Taking A leaves B/C alone; taking C leaves A/B alone; travelling empty leaves both forbidden pairs. Replacing trip 4 with an empty return leaves A/B alone on the right. Eight recorded states include the start, so they represent seven trips.

In the one-pile game, 3 leaves the opponent either 1 or 2, both winning. From 4, leave 3. In the two-pile game, `(1,3) → (1,1)` is winning; whichever remaining counter the opponent takes, you take the last. From three equal positive piles, remove a whole pile to leave an equal pair. These conclusions depend on the last-taker-wins rule.

For the weighing tree, B follows left-heavy then right-heavy; F follows right-heavy then balance; H follows balance then right-heavy. One balance weighing has only three outcomes. Two can distinguish nine possibilities under the known-heavier rule.

## Compare code only if you chose that option

Save [bus_booking.py](https://raw.githubusercontent.com/jouwdan/lc-cs/main/code/topic-05-algorithms/bus_booking.py) and run `python3 bus_booking.py`: the default prints `Buses: 3`. The separate [full checked model](https://github.com/jouwdan/lc-cs/blob/main/code/topic-05-algorithms/solutions.py) uses functions developed in later topics; its self-check prints `Topic 05 checks passed`.

**Repair one gap:** if abstraction was unclear, write “keep ___ because ___; omit ___ because ___”. If a trace failed, use two items and record every update before returning to the full table.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-05-algorithms/note-03-exam-practice">5. Exam practice: apply one skill</a>. <a href="https://tutors.dev/note/lc-cs/topic-05-algorithms/note-02-feedback">Open the answers</a>.

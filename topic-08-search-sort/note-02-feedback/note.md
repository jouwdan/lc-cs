# 4. Answers: Search & sort

Check your reasoning and repair one gap.

Use this after an attempt. Find the question or lab step you missed, explain the correction in one sentence, then rerun that case yourself.

## Quiz explanations

1. **Sorted data.** Only ordering justifies discarding half the interval. Positivity and even length are irrelevant.
2. **`high = middle - 1`.** The middle value is too large and cannot be the target, so exclude it and the region above it.
3. **`[2, 5, 1, 7]`.** Swaps move 7 to the final position during the first pass; the remaining prefix is not yet sorted.
4. **True.** Copying without removing leaves the same minimum available again, so the source never shrinks.
5. **Insert into a sorted prefix.** Larger prefix values shift right to make room for the next item.
6. **True.** A base case alone is insufficient if the calls never approach it.
7. **6.** Euclid's state pairs are `(48,18)`, `(18,12)`, `(12,6)`, `(6,0)`.
8. **`O(log n)`.** Each unsuccessful probe approximately halves the eligible interval. A middle-item match can still be a best-case `O(1)` event.
9. **False.** Repeated extreme partitions can produce quadratic time. The implementation and input arrangement matter.
10. **4.** For example, searching above the maximum of an eight-item list probes four middle positions with this inclusive algorithm.


## Search answers

Linear search on `[6,3,8,2]` returns 2 for target 8 after three probes. It returns -1 for target 5 after four probes. The return for absence belongs outside the loop.

The missing binary interval update is:

```python
if target < values[middle]:
    high = middle - 1
else:
    low = middle + 1
```

For both 23 and 24, the trace starts `(low,high,middle)` = `(0,6,3)`, `(4,6,5)`, `(4,4,4)`. Target 23 returns index 4; target 24 moves low to 5, beyond high 4, and returns -1.

For `[3,7,7,11]`, this version returns index 1 for target 7; accepting index 2 is also consistent with the any-match contract. The unsorted `[8,1,6]` example discards its answer after seeing middle value 1, showing why the precondition matters.

## Sort answers

| Algorithm and input | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| Bubble `[7,2,5,1]` | `[2,5,1,7]` | `[2,1,5,7]` | `[1,2,5,7]` |
| Insertion `[7,2,5,1]` | `[2,7,5,1]` | `[2,5,7,1]` | `[1,2,5,7]` |
| Selection `[6,3,8,2]` | `[2,3,8,6]` | `[2,3,8,6]` | `[2,3,6,8]` |

The unchanged second selection pass still compares values. Bubble grows a sorted suffix; insertion and selection grow a sorted prefix using different methods.

Quicksort's groups around 5 are `[2,1]`, `[5,5]`, `[7]`. Keep both copies of 5. For all equal values, all items go into the equal group and the recursive sides are empty. Our model builds extra lists rather than sorting in place.

## GCD and cost answers

A completed recursive version for the exercise's integer arguments is:

```python
def gcd_recursive(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
```

The requested GCD results are 7, 7, 6, 6, 6, 0. The last is the stated `(0,0)` convention. The base case is `b == 0`; otherwise the next nonzero second argument is smaller.

For missing targets above the maximum, `cost_lab.py` prints:

```text
8 8 4
16 16 5
32 32 6
```

Input size is the number of items. We counted inspected items. Binary search requires ascending input. Doubling size doubles linear probes and adds about one binary probe here. This supports a growth comparison, not a universal stopwatch result.

## Recurrence reminders

The last-taker-wins game has losing multiples of 3. The simple recursive evaluator repeats subproblems, so use small teaching inputs; the derived strategy is much cheaper for large counts.

The Fibonacci sequence with starting pair 1,1 reaches 21 after eight terms. Generation 8 in the A/B model has A = 8, B = 13, total 21. State your index convention and base values.

[Completed guided files and full models](https://github.com/jouwdan/lc-cs/tree/main/code/topic-08-search-sort) include all sorts, both GCD versions, game positions and Fibonacci checks. Running `solutions.py` prints `Topic 08 checks passed`.

**Repair one gap:** for binary search, circle the excluded middle and write the new bounds. For a sort, distinguish one comparison, one swap and one full pass before retrying.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-08-search-sort/note-03-exam-practice">5. Exam practice: apply one skill</a>. <a href="https://tutors.dev/note/lc-cs/topic-08-search-sort/note-02-feedback">Open the answers</a>.

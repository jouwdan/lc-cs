---
order: 1
---
# 1. Learn: Search & sort

Find, order and trace values.

A search finds an item. A sort puts items in order. Work through sections 1–5 with a pencil before coding; use the recursion and cost sections in a later session.

## 1. State what a search returns

Our search functions return a matching **zero-based index**, or **-1 if absent**. If -1 is returned, do not use it to index the list: Python interprets `values[-1]` as the final item.

**Linear search** examines items in order. It works even when the list is unsorted.

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

print(linear_search([6, 3, 8, 2], 8))
```

This prints 2. The function inspects indices 0, 1 and 2. One inspected item is one **probe** in our comparisons.

**Try:** search for 5 and count the probes.

**Check:** return -1 after four probes. The final `return -1` belongs **after** the loop; the first non-match does not prove absence. Empty input returns -1 with no probes. With duplicates, this version returns the first match.

## 2. Binary search halves the possible region

A **precondition** is something that must already be true before an algorithm starts. Binary search requires a list sorted under the same comparison rule, here ascending numbers.

Use inclusive bounds: `low = 0`, `high = len(values) - 1`. While `low <= high`:

1. Calculate `middle = (low + high) // 2`.
2. If the target equals the middle value, return the index.
3. If smaller, set `high = middle - 1`.
4. If larger, set `low = middle + 1`.

The discarded region cannot contain the target **because the list is sorted**. Excluding the middle guarantees progress. Keeping it can repeat the same probe forever.

For target 23 in `[3, 7, 11, 18, 23, 31, 42]`:

| low | high | middle | Value | Next action |
|---:|---:|---:|---:|---|
| 0 | 6 | 3 | 18 | Target larger: low = 4 |
| 4 | 6 | 5 | 31 | Target smaller: high = 4 |
| 4 | 4 | 4 | 23 | Return 4 |

**Try:** repeat for target 24.

**Check:** the same three middle positions are probed, then low becomes 5 while high stays 4. The interval is empty; return -1.

On `[8, 1, 6]`, searching for 8 would discard the left side containing it. This violates the precondition. Sorting inside the function would change index meanings and add work; our function expects already-sorted input. With duplicates, it may return **any** matching index.

## 3. Bubble sort: compare neighbours

A **pass** is a complete scan of the current region, not a single swap. Scanning left to right, compare neighbouring items and swap if the left is larger.

Worked first pass on `[7, 2, 5, 1]`:

```text
7 and 2: swap → [2, 7, 5, 1]
7 and 5: swap → [2, 5, 7, 1]
7 and 1: swap → [2, 5, 1, 7]
```

The largest remaining value is now at the right. After the next two passes: `[2,1,5,7]`, then `[1,2,5,7]`.

The **invariant** is a property that stays true after each pass: the sorted **suffix** (end portion) grows. Later passes can ignore that suffix.

**Try:** do one pass on `[3, 1, 2]`.

**Check:** `[1, 2, 3]`. An early-stop flag can finish after a pass with no swaps. Without that flag, already-sorted input still performs its scheduled comparisons.

## 4. Selection sort: find the next smallest

Find the smallest value in the unsorted region and swap it into that region's first position.

| Full pass on `[6,3,8,2]` | List afterwards |
|---|---|
| Find 2; swap with 6 | `[2,3,8,6]` |
| Find 3; already in place | `[2,3,8,6]` |
| Find 6; swap with 8 | `[2,3,6,8]` |

The sorted **prefix** (beginning portion) grows. A pass can make no change and still have performed comparisons.

A two-list version repeatedly removes the minimum from a source list and appends it to a result list. **Try:** what happens if it copies the minimum but never removes it?

**Check:** the source never shrinks; the same minimum can be selected repeatedly. A swapping version works in place within its list. Our models first make a copy to preserve the caller's original.

## 5. Insertion sort: make room in a sorted prefix

Take the next item, store it temporarily, shift larger values right, then put it in the gap.

| Insert into the growing prefix | List afterwards |
|---|---|
| Insert 2 before 7 | `[2,7,5,1]` |
| Insert 5 between 2 and 7 | `[2,5,7,1]` |
| Insert 1 at the start | `[1,2,5,7]` |

Store the item before shifting so it is not overwritten. Already-sorted input needs few shifts; reverse order needs many.

**Try:** start with `[2,4,3]`. Insert its final item into the sorted prefix `[2,4]`.

**Check:** store 3; shift 4 right; place 3 in the gap → `[2,3,4]`.

## 6. Recursion: solve a smaller version

A **recursive function** calls itself. It needs:

- a **base case** that returns without another call;
- a change that moves towards that case;
- the required returned result.

Factorial multiplies all positive integers up to `n`. Define `factorial(0) = 1` and `factorial(n) = n * factorial(n-1)` for non-negative integers.

```text
factorial(3)
= 3 × factorial(2)
= 3 × 2 × factorial(1)
= 3 × 2 × 1 × factorial(0)
= 6
```

The **call stack** holds unfinished calls and their local information. These calls wait for the smaller answer, then return upwards. Negative values must be rejected for this rule; subtracting one would move farther from zero. Python also limits recursion depth.

### Worked example: greatest common divisor

The **GCD** is the largest positive integer dividing two nonzero integers exactly. Euclid's algorithm replaces `(a,b)` with `(b,a % b)` until `b` is 0, then returns `a`.

```text
(48,18) → (18,12) → (12,6) → (6,0) → return 6
```

It can use a loop or recursion. The nonzero second argument shrinks, explaining termination. Our program accepts integers, uses `abs` to make them non-negative, and explicitly returns 0 for `(0,0)` as its programming convention.

**Try:** `(7,0)` and `(0,7)`.

**Check:** both return 7. The first is already at the base case; the second takes one update.

Iteration can avoid the stack space of recursive calls. Recursion can express a problem clearly. Compare the actual task rather than claiming either is always better.

## 7. Quicksort: partition, then recurse

A **pivot** is a value used to split the list. A **partition** groups values by how they compare with the pivot; it does not necessarily sort those groups.

For `[7,2,5,1,5]`, pivot 5 gives:

| Less | Equal | Greater |
|---|---|---|
| `[2,1]` | `[5,5]` | `[7]` |

Sort the less and greater groups recursively, then join them with the equal group: `[1,2] + [5,5] + [7]`. Result: `[1,2,5,5,7]`. Lists of length 0 or 1 are already sorted and form the base case.

**Try:** partition `[4,4,4]` around 4.

**Check:** less and greater are empty; equal contains all three copies. This three-way version preserves duplicates and stops. It builds extra lists, so it is not in-place.

Follow any pivot and partition procedure printed in an exam. First, last, middle-position, random and median-of-three are possible pivot choices. The middle **position** is not necessarily the middle **value**. Median-of-three compares the first, middle and last values. Random choice reduces dependence on a pattern but cannot guarantee balanced partitions.

## 8. Explain growth using a defined operation

Let `n` mean the number of items. **Big-O notation** describes how a cost grows as `n` increases; it is not a duration in seconds.

| Growth | Plain meaning | Example |
|---|---|---|
| `O(1)` | Bounded number of steps, independent of list length | Match at the first inspected item |
| `O(log n)` | Repeatedly shrink by a fixed factor | Binary search halves its region |
| `O(n)` | Work grows roughly in proportion to item count | Scan a whole list |
| `O(n²)` | Work can grow roughly like length squared | Repeated scans across a shrinking unsorted region |

For a missing target above all values:

| List size | Linear probes | Binary probes, inclusive version |
|---:|---:|---:|
| 8 | 8 | 4 |
| 16 | 16 | 5 |
| 32 | 32 | 6 |

Doubling the list doubles linear probes but adds about one binary probe. One probe means one inspected list item, not every Boolean operation in the code.

| Algorithm/version | Best time | Worst time |
|---|---|---|
| Linear search | `O(1)` | `O(n)` |
| Binary search on sorted data | `O(1)` | `O(log n)` |
| Bubble with early-stop flag | `O(n)` | `O(n²)` |
| Selection sort | `O(n²)` | `O(n²)` |
| Insertion sort | `O(n)` | `O(n²)` |
| Quicksort on distinct keys | Balanced: `O(n log n)` | Extreme repeated splits: `O(n²)` |

Binary search's inclusive implementation takes at most `floor(log2(n)) + 1` probes for non-empty input: 8 items can require 4, not always 3. Sorting before a single search has a preparation cost; repeated searches can make that preparation worthwhile.

Balanced quicksort has logarithmically many levels with linear partition work per level. Extreme pivots can leave sizes 0 and `n-1` repeatedly. Our three-way version takes `O(n)` on all-equal input because its recursive sides are empty; distinguish that special case from the distinct-key table.

**Try:** if a faster computer halves the elapsed time, does a full linear scan become logarithmic?

**Check:** no. Hardware speed changes duration, not the algorithm's growth pattern.

## 9. Extension: recurrences and games

A **recurrence** defines an answer using smaller or earlier answers. In the one-pile game, remove 1 or 2 and take the last to win. Zero is losing for the player to move. A position is winning if some legal move leaves the opponent losing.

| Counters | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Status for player to move | Lose | Win | Win | Lose | Win | Win | Lose |

**Try:** what should you leave from 8?

**Check:** 6, by removing 2. Multiples of 3 are losing under these rules. If taking the last loses instead, recheck the base cases; do not reuse the rule blindly.

## 10. Extension: Fibonacci generations

Define `T1 = 1`, `T2 = 1`, then `Tn = T(n-1) + T(n-2)`. The terms are `1,1,2,3,5,8,13,21`. The common alternative `F0 = 0, F1 = 1` uses different index labels; always state the starting values.

For a generation tree, suppose type A has one B parent and type B has one A plus one B parent. Start with one A node. Count the next generation using `next_A = B` and `next_B = A + B`.

| Generation | A | B | Total |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |
| 6 | 3 | 5 | 8 |
| 7 | 5 | 8 | 13 |

**Try:** calculate generation 8 before looking at the answer.

**Check:** A = 8, B = 13, total 21. Count each generation at the same level of the diagram.

An iterative sequence generator stores two previous terms, emits the earlier one, then updates them simultaneously: `previous, current = current, previous + current`. A simple recursive version recalculates many smaller terms. The recurrence describes the mathematics; it does not force an inefficient implementation. Iteration takes linear time in the number of output terms, with constant working state apart from the output list.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-08-search-sort/book-01-practice">2. Practise: trace and test algorithms</a>. <a href="https://tutors.dev/note/lc-cs/topic-08-search-sort/note-02-feedback">Open the answers</a>.

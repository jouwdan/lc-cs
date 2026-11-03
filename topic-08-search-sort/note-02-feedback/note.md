# Algorithms: traces, answers, and explanations

A correct final list is only part of the evidence; intermediate states explain how it was reached.

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

## Search traces

Linear search of `[6, 3, 8, 2]` for 8 probes indices 0, 1, 2 and returns 2. Searching for 5 probes all four indices and returns -1.

Binary search for 23 uses `(low, high, middle)` states `(0,6,3)`, `(4,6,5)`, `(4,4,4)` and returns 4. Searching for 24 follows the same middle positions but then sets `low = 5`, beyond `high = 4`, and returns -1.

On the invalid unsorted example `[8,1,6]`, searching for 8 first sees 1 and discards the left portion containing the answer. This demonstrates a violated precondition; it is not evidence that binary search is incorrect when its precondition holds.

## Sorting traces

| Algorithm | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| Bubble on `[7,2,5,1]` | `[2,5,1,7]` | `[2,1,5,7]` | `[1,2,5,7]` |
| Insertion on `[7,2,5,1]` | `[2,7,5,1]` | `[2,5,7,1]` | `[1,2,5,7]` |
| Selection on `[6,3,8,2]` | `[2,3,8,6]` | `[2,3,8,6]` | `[2,3,6,8]` |

A selection pass can leave the list unchanged when the smallest remaining item is already in place. That pass still performed comparisons.

Quicksort around pivot 5 produces less `[2,1]`, equal `[5,5]`, greater `[7]`. Recursing on the unequal parts gives `[1,2,5,5,7]`. An all-equal list puts every value in the equal partition, leaving empty recursive sides, which terminate immediately.

## GCD and growth

The GCD values for `(7,0)`, `(0,7)`, and `(18,48)` are 7, 7, and 6. Equal nonzero arguments return their absolute value. The model's explicit contract accepts integer arguments, normalises signs, and returns zero for `(0,0)`.

For a missing target above all values, linear-search item probes for sizes 8, 16, 32 are 8, 16, 32. Binary-search probes are 4, 5, 6. Doubling the input adds roughly one binary probe while doubling the linear probes. This supports a growth comparison; it does not give a universal wall-clock time.

The [`checked source`](https://github.com/jouwdan/lc-cs/blob/main/code/topic-08-search-sort/solutions.py) contains all algorithms and seeded repeatable checks against Python's sorted output and `math.gcd`. Run `python3 code/topic-08-search-sort/solutions.py`; expect `Topic 08 checks passed`.

The recursive counter-game model is deliberately for small learning examples: it repeats subproblems and grows expensive. For larger input, use the derived modulo-3 strategy or store previously computed positions. This illustrates why an elegant recurrence is not automatically an efficient implementation.

Pivot choices include first, last, middle position, random, and median-of-three. Median-of-three compares values at three chosen positions; it is not simply choosing the middle position. The supplied three-way quicksort handles an all-equal input in linear time because it creates one equal partition and two empty sides. The notes' balanced `O(n log n)` comparison refers to distinct-key input; that qualification avoids a misleading universal best-case claim.

For the Fibonacci supplement, generation totals are 1, 1, 2, 3, 5, 8, 13. Generations six and seven therefore contain 8 and 13 nodes, with type counts `(3,5)` and `(5,8)`. The eight-term sequence ends with 21. Starting conditions and index labels are essential; a zero-indexed definition may include an initial zero without contradicting this one-indexed sequence. The checked `fibonacci_terms` function uses the explicitly stated `1,1` starting pair.

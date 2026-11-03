# Choosing and tracing algorithms

Correct algorithms need clear preconditions, and efficient algorithms need a stated measure of work.

## Search means finding a specified target

A search function usually answers whether a target exists or returns its position. Define the contract first. In this topic, a search returns a matching zero-based index, or -1 when absent. A returned -1 is a sentinel, not permission to access `values[-1]`: Python would interpret that as the final item. If duplicates exist, our linear search returns the first match; the binary-search model may return any matching position.

Linear search examines items in order. For `[6, 3, 8, 2]` and target 8, it checks 6, then 3, then 8 and returns index 2. It works on unsorted data. If the target is absent, every item may need examination. An empty list needs no comparisons and returns -1. A common error is returning -1 inside the loop after the first non-match; absence can be concluded only after all eligible items have been checked.

## Binary search halves an ordered interval

Binary search requires data sorted according to the comparison rule used by the search. With an ascending numeric list, compare the target with the middle item. If the target is smaller, discard the middle item and everything to its right; if larger, discard the middle and everything to its left. This is safe because ordering tells us where a possible match can remain.

Use inclusive indices `low = 0`, `high = len(values) - 1`, and continue while `low <= high`. Set `middle = (low + high) // 2`. Updating to `middle - 1` or `middle + 1` guarantees progress; keeping `middle` in the interval can repeat the same comparison indefinitely.

Search for 23 in `[3, 7, 11, 18, 23, 31, 42]`:

| Step | low | high | middle | Middle value | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 18 | Target larger: low becomes 4 |
| 2 | 4 | 6 | 5 | 31 | Target smaller: high becomes 4 |
| 3 | 4 | 4 | 4 | 23 | Return index 4 |

For target 24, the third comparison moves `low` to 5, leaving `low > high`; return -1. There is no requirement to compare with every item. Sorting immediately before a single search has a cost, so binary search is especially useful when sorted data are already available or many searches justify the preparation.

## Bubble sort: neighbouring exchanges

Bubble sort compares neighbouring items and swaps those out of order. In an ascending version scanning left to right, the largest remaining item reaches the right end after each full pass. For `[7, 2, 5, 1]`, the states after full passes are `[2, 5, 1, 7]`, `[2, 1, 5, 7]`, and `[1, 2, 5, 7]`.

A pass is not a single swap. If asked to show the array after each pass, do not jump directly to the final sorted order. An optimised version records whether a swap occurred and stops after a pass with no swaps. Without that flag, an already sorted list can still perform all the planned comparisons. When discussing best-case performance, say which version you mean.

## Selection sort: select the next smallest

Selection sort repeatedly finds the smallest item in the unsorted region and places it at the beginning of that region. For `[6, 3, 8, 2]`, pass one selects 2 and swaps it with 6, giving `[2, 3, 8, 6]`. Pass two leaves 3 in place. Pass three swaps 6 and 8, giving `[2, 3, 6, 8]`.

A two-list teaching version can remove the minimum from an unsorted list and append it to a result list. The removal matters: copying without removing can select the same minimum forever. An in-place version tracks the minimum's index and swaps into the next position. Standard selection sort still scans the unsorted region when the input is already sorted; its comparison count remains quadratic.

## Insertion sort: extend a sorted prefix

Insertion sort grows a sorted prefix one item at a time. Take the next item, shift larger prefix values to the right, then insert the item into the resulting gap. With `[7, 2, 5, 1]`, the states after inserting each next item are `[2, 7, 5, 1]`, `[2, 5, 7, 1]`, and `[1, 2, 5, 7]`.

Keep the item being inserted in a temporary variable so shifting does not overwrite it. If the list is already sorted, each next item belongs at the end of the prefix, so little work is needed. Reverse order forces repeated shifts. This makes insertion sort a useful example of why an algorithm's cost depends on the input arrangement as well as its length.

## Higher Level extension: quicksort

Quicksort chooses a pivot and partitions the data around it, then sorts the smaller subproblems. In our clear three-way teaching version, `[7, 2, 5, 1, 5]` with pivot 5 partitions into less `[2, 1]`, equal `[5, 5]`, and greater `[7]`. Recursively sorting the less and greater parts and concatenating them with the equal part gives `[1, 2, 5, 5, 7]`. Keeping an equal partition preserves duplicates and ensures progress.

The exact intermediate layout depends on the partitioning method. If an exam supplies a pivot rule, in-place procedure, or ordering assumption, follow it rather than imposing this version's layout. A partition does not necessarily sort every item on either side. It establishes their relationship to the pivot; later work sorts those regions.

Balanced partitions produce roughly logarithmically many levels with linear partitioning work per level: typical/balanced time is `O(n log n)`. Repeatedly choosing an extreme pivot with distinct values can leave subproblems of sizes 0 and `n-1`, producing `O(n²)` worst-case time. Quicksort is not automatically `O(log n)` merely because it uses divide and conquer. Our list-building implementation also uses extra memory; do not describe it as in-place. Its three-way equal partition gives `O(n)` time on an all-equal input, since the recursive sides are empty. The conventional balanced `O(n log n)` statement assumes distinct keys or a standard partition treatment; distinguish that model from this special case.

Common pivot strategies choose the first item, last item, middle-position item, a random item, or the median of the first/middle/last items. A middle **position** is not necessarily the median **value**. First/last pivots can be poor for already ordered distinct data. Randomisation reduces dependence on an input pattern but does not remove the theoretical quadratic worst case. Median-of-three often improves partition balance, but it too is not a guarantee.

## Recursion needs progress and a stopping case

A recursive function calls itself on a smaller or simpler instance. It needs a base case and progress towards that case. Factorial can use `factorial(0) = 1` and `factorial(n) = n * factorial(n-1)` for non-negative integers. For 4, calls descend through 3, 2, 1, 0; results return as 1, 1, 2, 6, 24. A negative input would move away from zero under this rule, so validate the domain first.

The call stack keeps unfinished calls and their local state. Recursion can express a naturally recursive structure clearly, but each call uses stack space and Python limits recursion depth. Iteration can avoid that overhead. Neither technique is universally clearer or faster; compare the actual algorithms and their constraints.

Euclid's greatest-common-divisor algorithm uses `gcd(a, b) = gcd(b, a % b)` until `b == 0`, then returns `a`. Starting at `(48, 18)`, the states are `(18, 12)`, `(12, 6)`, `(6, 0)` and the answer is 6. An iterative version updates the pair in a loop; a recursive version calls itself on the new pair. The remainder reduces the nonzero second argument, explaining termination. Our code normalises negative arguments with `abs` and defines `gcd(0, 0)` as 0, following its stated programming contract.

## Compare growth, not one stopwatch result

Let `n` be the number of items. A useful operation count might be target comparisons for search or element comparisons for sorting. State what you count. A faster machine can reduce elapsed time, but it does not turn linear growth into logarithmic growth.

| Algorithm/version | Best time | Worst time | Key condition |
|---|---|---|---|
| Linear search | `O(1)` | `O(n)` | First item may match |
| Binary search | `O(1)` | `O(log n)` | Sorted data; interval halves |
| Bubble with early-stop flag | `O(n)` | `O(n²)` | Sorted input stops after one pass |
| Selection sort | `O(n²)` | `O(n²)` | Still scans for each minimum |
| Insertion sort | `O(n)` | `O(n²)` | Sorted prefix needs few shifts |
| Quicksort on distinct keys, balanced versus extreme splits | `O(n log n)` | `O(n²)` | Partition quality matters |

These are time-growth summaries for conventional versions and valid inputs. They do not mean an operation takes exactly `n²` seconds. For non-empty input, the inclusive binary-search version needs at most `floor(log2(n)) + 1` middle-item probes; a list of 8 items can therefore require 4, not always 3. Check the exact supplied algorithm before claiming a comparison count.

## Extension: reason backwards about a game

Suppose players remove one or two counters, and the player taking the last counter wins. With zero counters on your turn, you have already lost. Positions 1 and 2 are winning; position 3 is losing because every move gives the opponent a winning position. Working backwards reveals that multiples of 3 are losing under these rules. A winning player leaves a multiple of 3 after each move where possible.

This is pattern recognition supported by a recurrence: a position is winning if at least one legal move reaches a losing position. A different rule about taking the final counter changes the base cases and may change the strategy. Do not reuse a memorised pattern without checking the rules.

## Exam transfer

The 2022 Higher Level A&B paper examines selection and insertion sorting; 2023 examines binary search, recursive calls, and quicksort partitioning; 2025 examines GCD and quicksort cases. The original worked examples here prepare those methods without replacing the archived questions. Use [the source year index](https://www.betterexams.ie/leaving-cert/computer-science), attempt a question under its own assumptions, and compare the reasoning with its matching scheme.

## Transfer: Fibonacci patterns and a recurrence

A recurrence defines a later result using earlier results. For the sequence starting with `T1 = 1` and `T2 = 1`, let `Tn = T(n-1) + T(n-2)` for `n >= 3`. The first eight terms are `1, 1, 2, 3, 5, 8, 13, 21`. The two starting values are part of the definition: the common zero-indexed convention instead begins `F0 = 0, F1 = 1`. Label indices so these conventions are not confused.

A branching model can explain the rule instead of merely guessing from numbers. Suppose a type-A node has one type-B parent, and a type-B node has one type-A plus one type-B parent. Start with one type-A node. If generation `g` contains `A_g` and `B_g` nodes, then `A_(g+1) = B_g` and `B_(g+1) = A_g + B_g`.

| Generation | Type A | Type B | Total |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |
| 6 | 3 | 5 | 8 |
| 7 | 5 | 8 | 13 |

This is the transferable counting structure needed for a generation-tree question such as 2022 Higher Level A&B Question 11. Apply the rules supplied with the actual diagram and count each generation at the same level. The totals follow Fibonacci because each new total combines the previous two totals; drawing the two next levels gives 8 and 13 after a five-generation total of 5.

For an iterative implementation, store `previous = 1` and `current = 1`. Append `previous`, then update the pair simultaneously to `(current, previous + current)`. For eight iterations, the returned list is the eight terms above. A simple recursive implementation has two base cases, but recalculates the same smaller terms repeatedly; iteration builds the sequence in linear time with constant working state apart from the output list. This distinguishes the mathematical recurrence from an unnecessarily expensive implementation.

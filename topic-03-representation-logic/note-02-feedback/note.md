# 4. Answers: Binary & logic

Check your reasoning and repair one gap.

Check the questions you missed or guessed. Explain one correction, then try a fresh example. A score alone does not tell you what to study next.

## Question 1

**Answer: 45.** The set positions are 32, 8, 4 and 1; their sum is 45.

## Question 2

**Answer: 3A.** 58 = 3×16+10; hexadecimal digit A represents ten.

## Question 3

**Answer: 255.** Eight bits encode 256 distinct values, from zero through 255.

## Question 4

**Answer: 1001.** 6+3=9, represented as 1001. Carries must be included.

## Question 5

**Answer: 12,000.** Divide by eight bits per byte.

## Question 6

**Answer: ASCII-range characters use one byte with matching codes.** UTF-8 encodes Unicode with variable-length sequences and preserves ASCII byte values.

## Question 7

**Answer: Exactly one is true.** XOR differs from inclusive OR when both inputs are true.

## Question 8

**Answer: 8.** There are 2³ possible combinations.

## Question 9

**Answer: 0.** B OR S is one, but AND with zero gives zero.

## Question 10

**Answer: Lossless compression.** Lossless encoding preserves all information needed to reconstruct the original.

## Check the lab

58 = **00111010₂ = 3A₁₆**; B3₁₆ = **179**; `0101 + 0111 = 1100`. The image needs **12,000 bytes** before compression or headers.

For the two-input AND rule, outputs in row order 00, 01, 10, 11 are **0, 0, 0, 1**. OR gives **0, 1, 1, 1**.

For the Higher Level rule `C AND (B OR S)`, outputs in row order 000 to 111 are **0, 0, 0, 0, 0, 1, 1, 1**. The alternative `(C AND B) OR S` differs at 001 and 011.

If a conversion was wrong, write the place values before trying **26**. Check: **00011010₂ = 1A₁₆**. If a truth table was wrong, work out the bracketed expression in its own column first.

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-03-representation-logic/note-03-exam-practice">5. Exam practice</a>. Choose one question; you do not need to complete the whole list.

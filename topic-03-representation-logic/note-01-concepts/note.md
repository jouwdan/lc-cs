# Representing data and reasoning with logic

Convert between number bases, explain encodings and derive Boolean outputs systematically.

## Outcomes

Use binary, decimal and hexadecimal place value; perform binary addition; calculate simple storage requirements; distinguish character, image and sound representations; construct truth tables; and reason about logical conditions. Higher Level extensions combine gates and use a half-adder to connect arithmetic with logic.

## Place value before shortcuts

Decimal uses ten symbols with place values 1, 10, 100 and so on. Binary uses two symbols with place values 1, 2, 4, 8, 16, 32, 64 and 128. The rightmost place has value 1. In an unsigned eight-bit number, the range is 0–255 because all eight places sum to 255. Leading zeroes preserve the value while showing a required width.

For `00101101₂`, add 32 + 8 + 4 + 1 = 45. To encode decimal 73 in eight bits, choose 64, then 8, then 1: `01001001`. Check by summing the selected places. An alternative is repeated division by 2, recording remainders and reading them from last to first. These methods agree; showing either correctly makes your reasoning visible.

A byte is eight bits. A lowercase b commonly means bit and uppercase B byte; use words if ambiguity is possible. State whether a question uses decimal kilo (1000) or binary kibi (1024). Do not silently swap units. If a transfer rate is 8 megabits per second, its ideal byte rate is 1 megabyte per second before protocol overhead, using decimal units in both cases.

## Hexadecimal

Hexadecimal has sixteen digit values: 0–9 and A–F, where A is 10 and F is 15. Each digit corresponds to four binary bits. Decimal 45 is hex `2D`, because 2×16 + 13 = 45. Binary `1010 0110` is `A6` because the two groups have values 10 and 6. Group from the right and add leading zeroes when needed.

An RGB colour written `#1240C8` has red 0x12 = 18, green 0x40 = 64 and blue 0xC8 = 200. Each component uses one byte, with 256 possible values. Three components give 24 bits per pixel in an uncompressed RGB model. Hex is a compact human-readable representation of values; the computer does not gain an extra kind of fundamental storage state by displaying them in base sixteen.

## Binary arithmetic and limits

Binary addition rules are 0+0=0, 0+1=1, and 1+1=10: write 0 and carry 1. Adding `0110` and `0011` gives `1001`, which checks as 6+3=9. With a fixed unsigned eight-bit result, 255+1 needs a ninth bit. Overflow means the mathematical result cannot be represented in the allocated format. Python integers do not generally overflow at eight bits; the eight-bit limit belongs to the representation in the problem.

**Extension:** in eight-bit two's complement, negative 5 is obtained by inverting `00000101` to `11111010` and adding one: `11111011`. The range is −128 to 127. This representation is an enrichment task unless your teacher or a question explicitly requires it; do not confuse unsigned and signed interpretations of the same pattern.

## Text is encoded, not intrinsically binary letters

ASCII assigns codes to a small character set; standard ASCII has 128 codes and fits in seven bits. Unicode assigns code points for a much larger set of characters and symbols. UTF-8 is an encoding of those code points into one to four bytes. ASCII-range characters use the same single-byte values in UTF-8, which supports compatibility. Do not claim that all Unicode characters always take two bytes, or that Unicode and UTF-8 are synonyms.

A character, a code point and a visible symbol need not be one-to-one: a visible accented letter can sometimes be expressed using a base letter plus a combining mark. For introductory calculations, follow the encoding assumptions stated in the question. For Higher Level, explain why multilingual text requires more than the ASCII repertoire and why memory requirements depend on the encoding and text.

## Images, sound and compression

A bitmap is a grid of pixels. More pixels can capture more spatial detail; greater colour depth permits more distinct values per pixel. Ignoring headers and compression, a 40×30 image with 24 bits per pixel requires 40×30×24 = 28,800 bits = 3,600 bytes. Resolution and colour depth are different parameters. A black-and-white one-bit image needs only two possible values per pixel.

Digital sound samples a changing signal at regular intervals and represents each sample using a fixed number of bits. Increasing sample rate captures more samples per second; increasing bit depth provides more amplitude levels. In an uncompressed mono example, 8,000 samples/second × 8 bits/sample × 10 seconds = 640,000 bits = 80,000 bytes. Stereo adds another channel. These are simplified storage models, not guarantees about the size of a compressed audio file.

Lossless compression permits exact reconstruction. Run-length encoding might represent `AAAAABB` as runs `(A,5),(B,2)`, but alternating symbols give little benefit and may expand data because counts add overhead. Lossy compression discards selected detail to reduce size; use it only when exact recovery is unnecessary. Compression is not encryption: a smaller file is not thereby confidential.

## Boolean logic

A Boolean value is true or false, often modelled as 1 or 0. NOT reverses the input. AND is true only when both inputs are true. Inclusive OR is true when at least one input is true. XOR is true when exactly one input is true. NAND and NOR negate AND and OR respectively.

| A | B | AND | OR | XOR | NAND | NOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

For n independent binary inputs, a complete truth table has 2ⁿ rows. Enumerate them systematically to avoid omissions. When evaluating a combined circuit, create a column for every intermediate wire. The visible shapes in a diagram matter; use the supplied gate reference where the paper permits it.

## Worked combined condition — Higher Level extension

A library door opens if a valid card is present and either a member has booked or a staff override is active. Let C mean valid card, B booked and S staff override. Then `open = C AND (B OR S)`. For C=0, B=1, S=1 the output is 0 because no valid card exists. For C=1, B=0, S=1 it is 1. A common wrong expression, `(C AND B) OR S`, lets an override bypass the card requirement. Test a counterexample to reveal the difference.

A half-adder adds two one-bit inputs. The sum bit is A XOR B; the carry bit is A AND B. Inputs 1 and 1 produce sum 0 and carry 1, representing binary 10. This connects truth tables to arithmetic. A full-adder also handles carry-in, but you should not substitute it when asked for a half-adder.

## Logical conditions in programs

Python `and`, `or` and `not` express logical combinations. Comparisons such as `temperature > 20` produce Booleans. Use parentheses to make intended grouping clear. To accept a score between 0 and 100 inclusive, require `score >= 0 and score <= 100`. Using OR would accept almost any number because one side remains true. A boundary test of −1 immediately exposes the error.

Practise without a calculator when the selected paper requires that. Write base labels, units, carries and intermediate truth-table columns; these make a correct method assessable and make your own errors easier to find.

## Proving equivalence with a truth table — Higher Level extension

Two Boolean expressions are equivalent if their outputs match for every possible input combination. Testing one row proves very little. De Morgan's laws express `NOT(A AND B) = (NOT A) OR (NOT B)` and `NOT(A OR B) = (NOT A) AND (NOT B)`.

| A | B | NOT(A AND B) | (NOT A) OR (NOT B) |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

The final two columns match in all four rows, proving equivalence for two Boolean inputs. In words, “not both” means “at least one is not true”; it does not mean “neither”.

Practice: build the same table for the second law. The matching output sequence is 1,0,0,0. Then test the deliberately incorrect claim `NOT(A AND B) = (NOT A) AND (NOT B)`: A=0, B=1 is a counterexample. This is a systematic way to compare an unfamiliar circuit with another expression.

## Capacity and a binary-coded clock

With n independent bits there are **2^n distinct patterns**: every extra bit doubles the possibilities. Five bits can distinguish 32 items, so 33 distinct items require at least six bits. Distinguish the number of patterns from the largest unsigned value: six bits give 64 patterns numbered 0–63.

Some clocks encode each decimal digit separately in binary-coded decimal. For the four groups `0010 0001 : 0011 0101`, decode each group as a digit: 2, 1, 3, 5. The displayed time is **21:35**. Treating the first eight bits as one ordinary binary number would give 33, which is not the intended encoding. The representation rule matters as much as the bits. Practice: `0001 1000 : 0100 1001` displays 18:49. Four bits allow 16 patterns, but a decimal digit uses only ten of them; clock positions impose further restrictions.

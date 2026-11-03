---
order: 1
---
# 1. Learn: Binary & logic

Represent data and work with truth tables.

Learn how bits represent numbers, text, images and sound. Then use true/false rules to make decisions.

**Take this in three sessions:** sections 1–4 for numbers; 5–7 for files; 8–10 for logic. You can do all the core work on paper.

## 1. Binary place value

A **bit** is a binary digit: 0 or 1. A **byte** contains eight bits.

Decimal place values are 1, 10, 100… Binary place values are 1, 2, 4, 8… Start at the right and double each time.

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Example bits | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

Only add columns containing **1**: `32 + 8 + 4 + 1 = 45`. So `00101101₂ = 45₁₀`. The small base label tells you which number system is being used.

### Convert decimal 73 to eight-bit binary

1. Take the largest place value that fits: 64. Remainder: 9.
2. Take 8. Remainder: 1.
3. Take 1. Remainder: 0.
4. Put 1 in the 64, 8 and 1 columns: **01001001**.
5. Check: `64 + 8 + 1 = 73`.

You can also divide repeatedly by 2 and read the remainders from last to first. Both methods work. Leading zeroes show the required width without changing the value.

**Try:** convert 13 to eight-bit binary.

**Check:** `00001101`, because `8 + 4 + 1 = 13`.

## 2. How many values can bits hold?

Each extra bit doubles the number of patterns. **n bits give 2ⁿ patterns.**

| Bits | Patterns | Unsigned whole-number range |
|---|---:|---|
| 3 | 8 | 0–7 |
| 5 | 32 | 0–31 |
| 8 | 256 | 0–255 |

There are 256 eight-bit values, but the largest is **255**, because counting starts at zero. “Unsigned” means there is no sign bit for negative values.

**Try:** 33 different items need unique codes. Are five bits enough?

**Check:** no: five bits give only 32 codes. Six bits give 64.

### A binary-coded clock

Some clocks encode **each decimal digit separately**. Read `0010 0001 : 0011 0101` as 2, 1, 3, 5 → **21:35**. Do not read the first eight bits as one binary number.

**Try:** decode `0001 1000 : 0100 1001`.

**Check:** **18:49**. A decimal digit uses only ten of the sixteen possible four-bit patterns; clock positions impose further restrictions.

## 3. Hexadecimal is a shorter way to write bits

Hexadecimal (hex) uses sixteen digits: **0–9, A, B, C, D, E, F**. A means 10; F means 15. Each hex digit represents four bits.

**Example:** binary `1010 0110` becomes hex **A6**. The groups are 10 and 6. Group from the right; add leading zeroes if needed.

To convert hex **2D** to decimal: `2 × 16 + 13 = 45`.

**Try:** convert hex **B3** to decimal.

**Check:** `11 × 16 + 3 = 179`.

An RGB colour has red, green and blue values. In **#1240C8**, the pairs are 12, 40, C8 in hex: **18, 64, 200** in decimal. Each component uses one byte, giving 24 bits per pixel in this RGB model.

## 4. Binary addition

Use the usual column method, but carry when a column reaches two:

- `0 + 0 = 0`
- `0 + 1 = 1`
- `1 + 1 = 10`: write 0, carry 1.
- `1 + 1 + 1 = 11`: write 1, carry 1.

```text
  0110   (6)
+ 0011   (3)
------
  1001   (9)
```

**Try:** add `0101 + 0111`. Check using decimal.

**Check:** `1100`; `5 + 7 = 12`.

**Overflow** means a result will not fit in the available bits. Eight unsigned bits cannot hold 256, so `255 + 1` needs a ninth bit. Ordinary Python integers are not restricted to eight bits.

### Optional enrichment: negative numbers

Eight-bit **two's complement** represents −128 to 127. To represent −5, invert `00000101` to `11111010`, then add one: `11111011`. The same bits have different meanings under signed and unsigned rules. Use this only when your teacher or question requires it.

## 5. Storage calculations: keep the units

Divide **bits by 8** to get bytes. Lowercase **b** commonly means bit; uppercase **B** means byte. Write the full word if unsure.

A question may use decimal kilo (1000) or binary kibi (1024). Follow its stated convention. An ideal **8 megabits/s** transfer rate equals **1 megabyte/s**, using decimal units, before overhead.

### Worked image size

A bitmap is a grid of **pixels**. **Resolution** describes the number of pixels. **Colour depth** is the bits used for each pixel.

For a 40 × 30 image with 24 bits per pixel:

1. Pixels: `40 × 30 = 1,200`.
2. Bits: `1,200 × 24 = 28,800 bits`.
3. Bytes: `28,800 ÷ 8 = 3,600 bytes`.

This ignores headers and compression. A one-bit pixel has only two possible values, suitable for a simple black/white image.

**Try:** an 80 × 50 image uses 24 bits per pixel. Find its size in bytes.

**Check:** `80 × 50 × 24 ÷ 8 = 12,000 bytes`.

### Worked sound size

A **sample** is one measurement of a sound signal. **Sample rate** is measurements per second. **Bit depth** is bits per sample; more bits allow more amplitude levels.

Uncompressed size = **sample rate × bit depth × seconds × channels**.

For 10 seconds of mono sound at 8,000 samples/s and 8 bits/sample:

`8,000 × 8 × 10 × 1 = 640,000 bits = 80,000 bytes`.

Stereo has two channels, doubling this size. More samples per second and more bits per sample change different aspects of the recording.

## 6. How text becomes bytes

**ASCII** assigns codes to 128 characters and fits in seven bits. **Unicode** assigns code points to a much larger set of characters. **UTF-8** stores those code points using one to four bytes each.

ASCII-range characters use the same one-byte values in UTF-8. Accented letters and other scripts may need more bytes. A visible symbol can sometimes use several code points, such as a letter plus a combining accent.

For a storage question, use the encoding it specifies. Do not assume “one visible symbol = one byte” or “all Unicode takes two bytes”.

## 7. Compression

**Lossless** compression allows exact recovery. **Lossy** compression discards some detail to reduce size.

**Run-length encoding (RLE)** records repeated runs: `AAAAABB` becomes `(A,5), (B,2)`. It works well with long repeats. With `ABABAB`, storing six short runs plus counts may make the representation larger.

Use lossless when exact data matters, such as program files. Lossy may suit a photo when some detail can be sacrificed. Compression is not encryption: making a file smaller does not make it secret.

## 8. Boolean logic

A **Boolean** value is true or false, often written 1 or 0.

| Rule | Output is 1 when… |
|---|---|
| NOT A | A is 0. |
| A AND B | Both inputs are 1. |
| A OR B | At least one input is 1, including both. |
| A XOR B | Exactly one input is 1. |
| A NAND B | A AND B is 0. |
| A NOR B | A OR B is 0. |

A **truth table** checks every input combination. Two inputs need four rows; three inputs need eight. In general, use **2ⁿ rows** for n binary inputs.

| A | B | AND | OR | XOR | NAND | NOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**Try:** when A and B are both 1, how do OR and XOR differ?

**Check:** OR gives 1; XOR gives 0.

## 9. Combining rules — Higher Level

A door opens only if a valid card is present **and** either a booking or staff override exists.

Let C = valid card, B = booking, S = staff override:

**open = C AND (B OR S)**

For C=0, B=1, S=1:

1. Work inside the brackets: `B OR S = 1`.
2. Then `C AND 1 = 0`.
3. The door stays closed: no valid card.

The wrong rule `(C AND B) OR S` would open the door with S=1 even without a valid card. One example showing a rule fails is a **counterexample**.

For a circuit, label inputs and make a column for each intermediate gate output. Use gate symbols from the reference supplied with your question.

### A half-adder

A half-adder adds two one-bit inputs. **Sum = A XOR B** and **carry = A AND B**. Inputs 1 and 1 give sum 0, carry 1: binary **10**. A full-adder also handles a carry-in; it is a different circuit.

### Equivalent rules

Two expressions are equivalent only if every row gives the same output. De Morgan's laws are:

- `NOT(A AND B) = (NOT A) OR (NOT B)`
- `NOT(A OR B) = (NOT A) AND (NOT B)`

| A | B | NOT(A AND B) | (NOT A) OR (NOT B) |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

The final columns match. “Not both” means at least one is false; it does not mean both are false.

**Try:** check the second law in the same row order.

**Check:** both output columns are **1, 0, 0, 0**.

## 10. A programming connection

To accept a percentage from 0 to 100, both limits must hold:

`score >= 0 and score <= 100`

Using `or` is wrong: −1 would pass the “at most 100” test. You will write these conditions in Topic 06; no Python is needed for this topic's core lab.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-03-representation-logic/book-01-practice">2. Practise: Numbers and logic →</a>

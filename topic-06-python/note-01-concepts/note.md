---
order: 1
---
# 1. Learn: Python

Learn Python through small working programs.

Use Python 3 in your school editor. Read sections 1–4, then pause; practise sections 5–8 in a second session. The lab builds a ticket calculator in small working versions.

## 1. Save, predict, run

Create `first_steps.py`. Copy and save:

```python
name = "Ava"
tickets = 2
print(name, "needs", tickets, "tickets")
```

Run the saved file using your editor's Run button. A terminal alternative is `python3 first_steps.py` from its folder. Expect:

```text
Ava needs 2 tickets
```

`print()` displays values. A line beginning with `#` is a comment; Python does not run it. Change `tickets` to 3, predict the output and run again. Keep one working version before making a bigger change.

## 2. A variable stores a value

In `tickets = 2`, `tickets` is a **variable name** and `=` is assignment. The right side is worked out before the name is assigned.

```python
score = 10
score = score + 1
print(score)
```

This prints 11. It means “read 10, add one, store 11”, not the algebraic claim that 10 equals 11. `score += 1` is a shorter way to do this update.

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `12` |
| `float` | Number that can represent fractional values | `18.5`, `2.0` |
| `str` | Text | `"CS06"` |
| `bool` | True/false value | `True` |

**Try:** choose a type for the identifier `"00127"` and for the number of pupils.

**Check:** keep the identifier as a string so leading zeroes survive. Use an integer for the count.

## 3. Calculate and display

| Expression | Result | Reason |
|---|---|---|
| `17 / 5` | `3.4` | Division |
| `17 // 5` | `3` | Floor division |
| `17 % 5` | `2` | Remainder |
| `3 + 4 * 2` | `11` | Multiply before adding |
| `(3 + 4) * 2` | `14` | Parentheses first |
| `2 ** 3` | `8` | Exponentiation: 2 cubed |

`//` rounds down: `-17 // 5` is -4, so “remove the decimal part” is not a safe rule for negatives. `-3 ** 2` is -9; `(-3) ** 2` is 9. Parentheses show which quantity is squared.

Text behaves differently: `"3" + "4"` joins the strings into `"34"`; `3 + 4` adds numbers to give 7. `"Age: " + 17` raises a type error. Use `print("Age:", 17)` instead.

An **f-string** inserts values into text. Save and run:

```python
price_cents = 800
print(f"Price: EUR {price_cents / 100:.2f}")
```

Expect `Price: EUR 8.00`. The `f` enables the braces; `:.2f` requests two decimal places. Store money in integer cents here and format it only for display. `round(2.5, 2)` does not force two visible decimal places.

**Try:** predict the display for 1250 cents.

**Check:** `Price: EUR 12.50`.

## 4. Choose a path with a condition

A **condition** is an expression used to choose what happens. Comparisons include `==` (equal), `!=` (not equal), `<`, `<=`, `>` and `>=`. Remember: `=` stores; `==` compares.

```python
age = 16
if age < 16:
    price_cents = 800
elif age < 65:
    price_cents = 1200
else:
    price_cents = 900
print(price_cents)
```

This fictional ticket rule prints 1200. `if` tests first; `elif` means “otherwise, if”; `else` handles what remains. Only the first matching branch runs. A colon starts the block; indent its lines by four spaces. The unindented print happens after the choice.

**Try:** trace ages 15, 64 and 65.

**Check:** 800, 1200 and 900 cents. Ages 15/16 and 64/65 cross boundaries. A single age such as 30 cannot check either boundary fully.

### Combine conditions

- `and`: both conditions must hold.
- `or`: at least one must hold.
- `not`: reverse a true/false result.

A valid score can use `score >= 0 and score <= 100`, or Python's shorter `0 <= score <= 100`. With `or`, -1 passes the upper-limit test and 101 passes the lower-limit test, so that expression is wrong.

Branch order matters. For a practice grade, check `score >= 75` before `score >= 50`; otherwise 80 matches the lower band first. These are practice bands, not official Leaving Certificate grades.

## 5. Give a calculation a name

A **function** is a named block that can be called again. Learn this syntax before the lab asks you to make a ticket function:

```python
def double(number):
    answer = number * 2
    return answer

result = double(6)
print(result)
```

Expect 12.

1. `def` defines the function; defining it does not yet run the body.
2. `number` is a **parameter**, a name for an incoming value.
3. `double(6)` calls the function; 6 is the **argument** supplied.
4. `return` sends the answer back and ends this call.
5. `print(result)` displays the returned value.

`return` and `print` have different jobs. A function with no explicit `return` gives back `None`, even if it prints something. A name created inside a function is normally **local** to that call.

**Try:** change the call to `double(9)`.

**Check:** 18. You changed the argument, not the rule.

An **assertion** checks a result in code:

```python
assert double(6) == 12
print("Check passed")
```

A true assertion is silent. A false assertion stops with `AssertionError`. Write your expected answer independently before running it.

## 6. Repeat for a known collection

A **list** holds items in order, using square brackets. `ages = [12, 16, 70]` holds three ages. A `for` loop visits each item:

```python
total = 0
for number in [2, 3, 4]:
    total = total + number
print(total)
```

| Number | Total after addition |
|---:|---:|
| 2 | 2 |
| 3 | 5 |
| 4 | 9 |

The output is 9. An **accumulator** keeps a running total. It starts **before** the loop; moving `total = 0` inside loses earlier additions. Empty input leaves the initial total at 0.

`range()` supplies a sequence of integers; its stop is excluded:

| Expression | Values |
|---|---|
| `range(4)` | 0, 1, 2, 3 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(6, 0, -2)` | 6, 4, 2 |

**Try:** replace the list with `range(1, 4)`. Predict the total.

**Check:** 6, because 1 + 2 + 3 = 6. The number 4 is excluded.

## 7. Convert and validate input

`input()` returns text, even when the person types digits. `int("16")` produces integer 16. `int("16.5")` and `int("sixteen")` raise `ValueError`. `int(16.5)` instead truncates a numeric value; do not use that to accept a fractional ticket count.

**Validation** checks a rule, such as “whole number from 0 to 120”. It cannot prove a plausible age is truthful. **Verification** checks a copy or result against its original or expected version.

```python
try:
    age = int(input("Age (0-120): "))
except ValueError:
    print("Enter a whole number.")
else:
    if 0 <= age <= 120:
        print("Accepted age:", age)
    else:
        print("Enter an age from 0 to 120.")
```

`try` attempts conversion. `except ValueError` handles that expected conversion failure. `else` runs when conversion succeeds. Range checking is separate: `int("-1")` succeeds, but -1 fails the age rule.

A function can signal an invalid value with `raise ValueError("message")`. The lab supplies that validation line before asking you to complete the price branches. Avoid catching every error with a bare `except`, which can hide unrelated faults.

## 8. Repeat while a condition holds

```python
count = 3
while count > 0:
    print(count)
    count = count - 1
```

This prints 3, 2 and 1 on separate lines. A `while` loop checks before each repetition, so starting at 0 prints nothing. Omitting the subtraction would keep the condition true forever.

A **sentinel** is a special value meaning “stop”. For scores 0–100, -1 can stop entry. Test it **before** adding it. `break` exits the nearest loop; `continue` skips the remaining body and starts the next check. The lab supplies a small sentinel example to adapt.

Use `for` when visiting a known collection; use `while` when repetition depends on a changing condition, such as entering a valid age.

## 9. Recognise three kinds of error

| Kind | Example | Useful first action |
|---|---|---|
| Syntax | Missing colon after `if` | Read the reported line and nearby punctuation |
| Runtime | `int("hello")`, division by zero | Read the error type and values at the failing operation |
| Logical | Using `> 65` when 65 belongs in the senior band | Compare expected and actual boundary results |

A **traceback** reports the sequence of calls leading to an error. Start with its error type and final relevant source line. A program can run without errors and still calculate the wrong result.

For Section C practice, keep the required filenames, run supplied code before editing, make one requested change, and rerun earlier tests. The next activity follows that same routine.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-06-python/book-01-practice">2. Practise: build a ticket calculator</a>. <a href="https://tutors.dev/note/lc-cs/topic-06-python/note-02-feedback">Open the answers</a>.

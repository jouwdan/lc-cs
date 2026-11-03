# Python: state, decisions, and repetition

Learn to predict what a program does, then make the smallest change that produces the required behaviour.

## A dependable programming routine

A Python file is plain text containing instructions. Run the file you actually saved, and check the filename before making changes. Keep a working copy of supplied material when a task asks you to modify it. Read the program from top to bottom, identify its inputs and outputs, predict one result, and run it before editing. If the starting version already fails, record that separately from any fault introduced by your change.

Use meaningful names such as `ticket_count` and `total_cost`, consistent indentation, and short comments explaining intent. A comment begins with `#` and is not executed. A useful comment states why a boundary or conversion is required; repeating “add one” beside `count += 1` adds little. Save and run after each small change. Several untested changes make the source of a failure harder to isolate.

## Values, variables, and types

A variable name refers to a value. Assignment evaluates the expression on the right before binding the name on the left. In `score = score + 1`, Python reads the current value, adds one, and replaces the binding. It is not an algebraic equation. A variable must have a value before an expression can use it.

| Type | Example | Appropriate use |
|---|---|---|
| `int` | `12` | Number of pupils or loop count |
| `float` | `18.5` | Measurements with fractional parts |
| `str` | `"CS06"` | Names, labels, and text identifiers |
| `bool` | `True` | Whether a condition holds |

A student identifier such as `"00127"` is text even though its characters are digits. Converting it to an integer loses leading zeroes and suggests arithmetic that has no useful meaning. Choose a representation according to the information, not its visual appearance.

`input()` returns a string. `int(input("How many? "))` converts a valid integer string, while `float(...)` permits a decimal. `int("3.5")` raises `ValueError`; it does not round. `int(3.5)` truncates the already numeric value towards zero. Do not use truncation as a substitute for checking whether a user entered a whole-number quantity.

## Expressions and output

Python supports `+`, `-`, `*`, `/`, `//`, `%`, and `**`. `/` performs division and returns a floating-point result. `//` is floor division, and `%` returns the remainder. For positive integers, `17 // 5` is 3 and `17 % 5` is 2. With negative values floor division rounds down, so do not describe it as universally chopping off the decimal part.

Multiplication and division take precedence over addition and subtraction. Parentheses make an intended grouping explicit: `(price + fee) * quantity` differs from `price + fee * quantity`. Exponentiation has its own precedence, and `-3 ** 2` evaluates to -9 whereas `(-3) ** 2` evaluates to 9. When unsure, add meaningful parentheses and test an example.

Strings use `+` for concatenation: `"3" + "4"` is `"34"`. Attempting `"Age: " + 17` raises `TypeError`; use `print("Age:", 17)` or `f"Age: {17}"`. An f-string can control display: `f"{2.5:.2f}"` displays `2.50`. `round(value, 2)` changes a numeric result but does not guarantee two visible decimal places. Display rounding should normally happen at the output boundary rather than repeatedly inside a calculation.

## Selection and Boolean logic

Comparison operators include `==`, `!=`, `<`, `<=`, `>`, and `>=`. `=` assigns; `==` compares. `and` requires both conditions, `or` requires at least one, and `not` negates a condition. For a valid percentage, `0 <= score <= 100` is clear. The expression `score >= 0 or score <= 100` accepts every ordinary number because at least one side is true.

An `if`/`elif`/`else` chain selects the first true branch. Consider a fictional practice grading rule:

```python
if score >= 75:
    band = "Advanced"
elif score >= 50:
    band = "Secure"
else:
    band = "Developing"
```

A score of 80 gets `Advanced`, 75 also gets `Advanced`, 50 gets `Secure`, and 49 gets `Developing`. This is a classroom example, not an official Leaving Certificate grade scale. Reversing the first two tests makes 80 match `>= 50` too early. Separate `if` statements behave differently because more than one block can run.

Indentation defines a block. The line after a condition ends in a colon, and its body is indented consistently, conventionally four spaces. A line back at the original indentation is outside the block. When tracing code, indentation is part of its meaning, not a visual preference.

## Counted loops

A `for` loop visits items from an iterable. `range(4)` supplies 0, 1, 2, 3; its stop value is excluded. `range(1, 5)` supplies 1, 2, 3, 4. `range(6, 0, -2)` supplies 6, 4, 2. Choose a start, stop, and step that move in the intended direction.

```python
total = 0
for number in range(1, 5):
    total += number
print(total)
```

| number | total after addition |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 10 |

The output is `10`. Initialise the accumulator before the loop. If `total = 0` sits inside the loop it resets on each iteration, so the final output becomes 4. A loop over an empty range does not execute its body. This is useful when zero repetitions are valid, but can expose an uninitialised variable if one was created only inside the loop.

## Conditional loops and sentinels

A `while` loop checks its condition before each iteration, so it may run zero times. For `count = 3`, repeatedly printing `count` and subtracting one while `count > 0` prints 3, 2, 1. Omitting the subtraction prevents progress and creates an infinite loop. Check which variable controls the condition and where it changes.

A sentinel is a special input indicating that entry should stop. For a stream of non-negative scores, -1 can be a sentinel. Check for it before adding it to the total. If -1 were a valid measurement, it would be a poor sentinel. A condition-driven loop is often clearer than guessing how many inputs a person will supply.

`break` exits the nearest loop immediately; `continue` skips the remainder of the current iteration and goes to the next check. Overusing them can obscure the path, so prefer the simplest clear condition. A sentinel loop has a legitimate reason to break after recognising the stop value.

## Validation and errors

Validation checks whether data conforms to requirements. It does not prove that a plausible entered age is factually correct. Verification checks that data or a result matches an original or expected version. Distinguish the two when explaining an input workflow.

A **syntax error** breaks the language rules, such as a missing colon. A **runtime error** occurs during execution, such as division by zero or converting `"hello"` to an integer. A **logical error** lets a program run but gives the wrong answer, such as excluding an inclusive boundary. Tests must check outcomes because logical errors may produce no traceback.

Handle expected bad user input narrowly:

```python
try:
    count = int(input("Number of tickets: "))
except ValueError:
    print("Enter a whole number.")
else:
    if count < 0:
        print("Ticket count cannot be negative.")
    else:
        print("You requested", count, "tickets.")
```

The conversion and range check address different problems. Catching every exception and pretending the result is zero can conceal a programming fault. Read a traceback's error type and final relevant line, then inspect that operation and its inputs.

## Transfer to a programming examination

Section C commonly asks for changes to a supplied program and a separate constructed solution. The archived 2024 Ordinary Level Section C practices input, selection, and arithmetic; the 2025 Higher Level Section C develops list processing and function calls. Use those tasks after the fundamentals here. The [Better Exams year index](https://www.betterexams.ie/leaving-cert/computer-science) links the papers and their matching schemes.

Follow the filename and saving instructions printed on the particular paper. Treat each requested modification as a testable requirement: write the expected effect, change the relevant line or block, and rerun earlier examples. If one extension is unfinished, preserve the working parts and clearly identify incomplete work. A neat output does not compensate for an incorrect calculation or missing required branch.

Before moving on, explain why the stop value of `range` is excluded, why a percentage check needs `and`, and why the accumulator starts outside the loop. These three explanations prevent many avoidable programming mistakes.

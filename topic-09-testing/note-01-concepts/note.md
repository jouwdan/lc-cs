# Design a solution and demonstrate that it works

Testing supplies evidence against requirements; debugging explains and repairs the cause of a failure.

## Start with an observable requirement

“Make a good booking system” is too vague to test. “Accept an integer party size from 1 to 8, inclusive, and show the total price before confirming” is observable. Identify the user, the task, the accepted inputs, the output, and any constraints. A requirement can be functional, describing behaviour, or non-functional, describing a quality such as response time, accessibility, or reliability.

For a fictional club booking function, specify the price rule exactly: one to four tickets cost 1200 cents each; five to eight tickets cost 1000 cents each. Quantities outside 1–8 are invalid. The function returns total cents and does not alter any external booking record. Those details tell a tester what to expect at 4 and 5 and prevent ambiguity about whether the cheaper rate applies to every ticket or only tickets after the fourth.

An acceptance criterion might be “given quantity 5, the displayed total is €50.00”. A design then chooses a calculation function and a separate user interface. The separation supports direct tests of the calculation without requiring keyboard input or a live payment system. The test still has to check the displayed value separately: a correct function can be connected to the wrong input field.

## A development process is a feedback cycle

A useful process includes analysis, design, implementation, testing, evaluation, and maintenance. Real projects revisit earlier decisions when evidence shows a problem. Analysis clarifies what is needed; design plans structure, algorithms, data, and interfaces; implementation constructs the program; testing compares behaviour with expectations; evaluation considers how well the complete solution meets user needs.

A sequential or waterfall-style process moves through defined phases and can suit stable requirements. An iterative approach builds and reviews smaller increments, making it easier to incorporate feedback and changing requirements. Neither label guarantees quality. Explain why an approach fits a scenario: a prototype can reveal an inaccessible interaction early, while a fixed-interface project may require particularly explicit documentation.

A prototype is a model used to investigate a question. A paper interface can test whether labels make sense before calculations exist. A working calculation prototype can test a formula without representing the final interface. State its limits; a demonstration using fake data is not evidence that production data import, security, or capacity have been tested.

## Design for people as well as calculations

A usable interface has clear labels, feedback, predictable controls, and understandable errors. An accessible interface must support relevant needs such as keyboard use, sufficient contrast, readable text, and alternatives to visual-only cues. “The error is red” is insufficient if colour is the only signal. Name the problem and how to correct it: “Enter a whole number from 1 to 8” is more useful than “Invalid”.

Collect only data needed for the task. A ticket-quantity calculator does not need a person's date of birth or home address. Use invented data in tests, and avoid exposing private records in screenshots. Check how the system handles failure before it writes or replaces data. A failed input validation should not leave a partial booking or erase a previously valid record.

## Test levels answer different questions

**Unit testing** checks a small isolated component, such as a price function. **Integration testing** checks how components work together, such as input parsing passing a quantity to that function. **System testing** checks the assembled system against its requirements. **Acceptance testing** checks whether the result meets the agreed needs of its users or customer.

Alpha testing commonly refers to testing in a controlled environment associated with the developer. Beta testing gives selected external users an opportunity to try a pre-release system in more realistic use. They can reveal usability and environment problems that the development team missed. They do not replace deliberate boundary or security tests.

**Regression testing** reruns relevant checks after a change to find unintended breakage in previously working behaviour. Fixing the five-ticket discount should not change the one-ticket price. A test that reproduces the original bug becomes a useful permanent regression check.

## Functional and non-functional testing

Functional testing checks what the system does: correct totals, required messages, correct file import, permitted actions, and rejected inputs. Non-functional testing checks qualities such as performance, usability, accessibility, reliability, and security characteristics. The categories describe purpose rather than a strict set of tools; a security check may also verify a functional access-control requirement.

Make a non-functional requirement measurable. “Fast” is vague; “under the agreed test conditions, show a result within one second for 95% of requests” states a threshold and population. A load test uses expected or increased demand; a stress test deliberately goes beyond normal capacity to observe failure and recovery. Report the machine, dataset, and workload rather than presenting one quick run as a universal performance guarantee.

## Choose data that can expose a fault

Normal data are ordinary valid examples. Boundary data are at or close to a limit. Invalid data violate a type, format, or range requirement. Testing every integer from 1 to 8 is feasible for our small booking function, but many real input spaces are too large. Equivalence partitioning groups inputs expected to follow the same rule, such as 1–4 and 5–8, then selects examples from each group and its edges.

| Input | Category | Expected result |
|---|---|---|
| 2 | Normal valid | 2400 cents |
| 1 | Minimum valid boundary | 1200 cents |
| 4 | Last full-price boundary | 4800 cents |
| 5 | First discount boundary | 5000 cents |
| 8 | Maximum valid boundary | 8000 cents |
| 0, 9 | Just outside allowed range | Validation error |
| `"five"`, `2.5` | Invalid type for the function | Validation error |

State the expected result before running the program. Otherwise it is easy to accept whatever output appears. Record actual output, pass/fail, and evidence. If the function accepts only integers, numeric text may be valid for the interface but invalid for the function until conversion occurs. Test each boundary at the layer that owns it.

## Test oracles and coverage

A test oracle is the source of the expected result: a hand calculation, a clear specification, or a trusted reference implementation. Copying the same faulty expression into the test can reproduce the bug and falsely appear to confirm correctness. For a discount threshold, calculate a few totals manually rather than deriving every expected result with the function's own branch logic.

Coverage measures which code or behaviours tests exercise. Statement coverage can show that every line ran; branch coverage checks whether decision outcomes were taken. Neither proves the requirements are correct or that all combinations are covered. Tests can execute a wrong line without asserting its result. A short suite with carefully chosen expectations can provide more useful evidence than many unchecked runs.

## Debug systematically

First reproduce the failure reliably. Reduce it to the smallest input that still fails. Read any traceback, inspect the relevant variables, and form a hypothesis. Use a trace table, a temporary print, or a debugger breakpoint to test that hypothesis. Change the cause, rerun the failing example, then rerun earlier valid examples. Record why the repair works.

Consider this faulty rule:

```python
if quantity > 5:
    price = 1000
else:
    price = 1200
```

Quantity 5 incorrectly costs 6000 instead of 5000. The boundary test identifies a logical error. The root cause is the exclusive comparison; `>= 5` matches the requirement. Changing the expected answer to 6000 would conceal the fault. Changing an unrelated output string would not repair it.

Syntax errors, runtime errors, and logical errors require different evidence. A missing colon prevents parsing; an invalid list index raises an exception during execution; an off-by-one comparison can quietly produce a wrong classification. Do not assume the absence of an error message means correctness.

## Read the language that is actually present

Some archived questions use JavaScript or pseudocode rather than Python. Operator symbols can have different meanings across languages. Python has no `++` increment operator: `x += 1` updates a variable. In JavaScript, prefix `++x` increments and evaluates to the new value, while postfix `x++` evaluates to the old value and then increments.

```javascript
let x = 4;
let before = x++;
let after = ++x;
console.log(x, before, after);
```

The output values are `6 4 6`. After the second line, `before` is 4 and `x` is 5. The third line first changes `x` to 6 and assigns 6 to `after`. Trace each statement; do not apply Python rules to JavaScript syntax.

JavaScript `===` compares without coercing types, so `3 === "3"` is false; loose `3 == "3"` is true. `"3" + 4` produces the string `"34"`. In Python, `3 == "3"` is false and `"3" + 4` raises `TypeError`. These examples show why type assumptions matter. In Python, `True and False` uses words; JavaScript commonly uses `true && false`.

## Evaluate and maintain the result

Evaluation links evidence to requirements. State what worked, what failed, and what remains untested. “All tests passed” means those specific checks passed, not that no bugs exist. A user trial can reveal confusing labels even when every arithmetic test passes. Feedback should lead to a specific change and another relevant check.

For a programming exam, make requested edits incrementally and retain the working parts. The archived 2021 Higher Level A&B paper distinguishes unit, system, and regression testing; the 2023 papers examine test purposes and real-user testing; the 2020 Higher Level paper includes language/operator reasoning. Use the [year index](https://www.betterexams.ie/leaving-cert/computer-science) for the exact wording and matching schemes. Support every claim with a trace, test, or requirement, not a vague assertion that the solution is good.

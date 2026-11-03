# 1. Learn: Testing

Find a fault, repair it and retest.

**Testing** compares actual behaviour with an expected result. **Debugging** finds and repairs the cause of a failure. This lesson uses one small ticket calculator so the evidence is easy to check by hand.

## 1. Make the requirement observable

“Make a good booking system” is too vague. A **requirement** says what users need or what the system must do. Our function has this precise contract:

| Quantity | Rule |
|---|---|
| 1–4 whole tickets | 1200 cents per ticket |
| 5–8 whole tickets | 1000 cents per ticket, for **every** ticket |
| Anything else | Reject with a useful error |
| Result | Return total cents; do not create a booking |

An **acceptance criterion** is a concrete condition for judging whether a requirement is met: “For quantity 5, return 5000 cents.” The display layer should show `Total: EUR 50.00`.

**Try:** calculate the total for 4, then 5 tickets.

**Check:** 4800 and 5000 cents. At 5, the lower price applies to all tickets, not only the fifth.

## 2. Develop in a feedback cycle

| Stage | What you do | Ticket example |
|---|---|---|
| Analysis | Clarify the need and constraints | Ask who receives the discount |
| Design | Plan data, algorithms and interface | Separate calculation from input/display |
| Implementation | Build the program | Write the function |
| Testing | Compare actual and expected behaviour | Check quantity 5 returns 5000 |
| Evaluation | Judge how well needs are met | Check errors are understandable |
| Maintenance | Correct or adapt an existing system | Update a changed price rule and rerun tests |

A **waterfall-style** process uses defined phases and can suit stable requirements. An **iterative** process builds and reviews smaller increments, helping incorporate feedback and changes. Real work can revisit earlier stages.

A **prototype** is a model used to answer a question. A paper screen can test whether labels make sense before the calculations exist. A calculator prototype can test prices without being a complete booking service.

**Try:** users misunderstand the quantity field. Which prototype could help first?

**Check:** a paper or simple interactive screen lets users try the wording. A correct formula alone will not reveal that problem.

## 3. Make the interface usable and accessible

**Usability** means people can carry out their task effectively. **Accessibility** means people with different needs can use it. Use clear labels, readable text, keyboard operation and errors that explain a repair.

Compare “Invalid” with “Enter a whole number from 1 to 8”. The second names the accepted input. Do not rely on red colour alone; include words and connect the message to its field.

**Try:** describe one measurable check for a ticket form.

**Check:** “Using only the keyboard, reach quantity, enter 5, submit and read the total without losing focus” is a concrete procedure. Also check an error can be identified without colour.

Collect only needed data. A quantity calculator does not need a home address. Use fictional records in tests. If a future version saves bookings, invalid input must not leave a partial booking or overwrite a valid one.

## 4. Choose the test level

| Term | Question it answers | Example |
|---|---|---|
| Unit | Does one small component work? | Call the price function with 5; expect 5000 |
| Integration | Do components connect correctly? | Convert `"5"`, calculate, format; expect `Total: EUR 50.00` |
| System | Does the assembled system meet its requirements? | Complete a booking and check its saved record |
| Acceptance | Does the result meet agreed user needs? | The customer checks the agreed booking scenarios |
| Regression | Did a change break earlier working behaviour? | After fixing 5 tickets, rerun the 1-ticket test |

The lab contains a calculator and text conversion. It does **not** contain a booking store; a system test involving storage can be designed, but cannot honestly be claimed to have run.

**Alpha testing** usually happens in a controlled environment associated with the developer. **Beta testing** involves selected external users trying a pre-release version in more realistic conditions. User feedback can reveal unclear wording or environment problems missed by function tests.

**Try:** does passing a calculation's unit tests prove its screen displays the correct amount?

**Check:** no. A connection or formatting fault can still exist; test the full path too.

## 5. Distinguish behaviour from quality

**Functional tests** check what the system does: computes a total, rejects input, displays a required message. **Non-functional tests** check qualities such as performance, reliability, usability, accessibility and security.

“Fast” is vague. “In the agreed test environment, 95% of responses arrive within one second” defines a measurable threshold and population. Report the machine, data and workload used.

A **load test** examines expected or increased demand. A **stress test** pushes beyond normal capacity to inspect failure and recovery. Neither is established by running one small example quickly. Some checks overlap categories: checking that an unauthorised account is rejected also tests a functional access rule.

## 6. Choose data that can reveal a fault

| Data | Category | Expected outcome |
|---|---|---|
| 2 | Ordinary valid value | 2400 cents |
| 1 | Minimum valid boundary | 1200 cents |
| 4 | Last full-price boundary | 4800 cents |
| 5 | First discount boundary | 5000 cents |
| 8 | Maximum valid boundary | 8000 cents |
| 0, 9 | Just outside allowed range | Error |
| `2.5`, `"five"` | Invalid types for the function | Error |

A **boundary** is a limit or change in rule. For the discount, test below, at and above: 4, 5, 6. **Equivalence partitioning** groups inputs expected to follow the same rule, such as 1–4 and 5–8, then chooses representative cases and edges.

The calculation function requires an integer. Numeric text `"5"` is valid for the input interface, but must be converted before reaching the function. Test each layer against its own contract.

**Try:** classify quantity 7 and quantity 9.

**Check:** 7 is ordinary valid discounted data; 9 is invalid and just beyond the upper boundary.

## 7. Know where the expected answer comes from

A **test oracle** supplies the expected result. Here, hand calculation gives `5 × 1000 = 5000`. A specification or trusted independent implementation can also provide an oracle.

Do not calculate every expected result with the same branch as the program. The same mistake could then make both wrong in the same way.

Record input / expected / actual / pass or fail. An assertion compares values automatically, but you still need the right expectation.

**Coverage** describes what tests exercised. Statement coverage records which statements ran; branch coverage checks decision outcomes. Neither proves correctness: the test can run a wrong calculation without checking its result, or the requirement itself may be wrong.

**Try:** one test prints 6000 for 5 tickets and reports no exception. Has it passed?

**Check:** no. The required 5000 differs from the actual value. “It ran” is weaker evidence than “its result matches the requirement”.

## 8. Debug one cause at a time

1. **Reproduce:** find an input that reliably shows the problem.
2. **Reduce:** use the smallest useful failing case.
3. **Inspect:** trace values, add a temporary print or use a debugger breakpoint.
4. **Form a hypothesis:** name what you think is wrong.
5. **Repair:** change the cause.
6. **Retest:** rerun the failing case and earlier working cases.

For this branch:

```python
if quantity > 5:
    price = 1000
else:
    price = 1200
```

Quantity 5 enters the wrong branch, costing 6000. The requirement includes 5 in the discounted group, so change `>` to `>=`. Keep the expected answer 5000; changing the test would conceal the bug.

| Error kind | Example | Evidence |
|---|---|---|
| Syntax | Missing colon | Python cannot parse the code |
| Runtime | Index outside a list | An operation fails during execution |
| Logical | Wrong threshold | Program runs but expected/actual results differ |

A **traceback** identifies the error type and relevant call/line. A **breakpoint** pauses execution so you can inspect current values. The absence of an error message does not prove the answer is right.

## 9. Read the language actually printed

Some archived questions use JavaScript or pseudocode. Similar-looking operators can behave differently.

```javascript
let x = 4;
let before = x++;
let after = ++x;
console.log(x, before, after);
```

**Postfix** `x++` produces the old value, then increments x. **Prefix** `++x` increments x, then produces the new value.

| After line | x | before | after |
|---|---:|---:|---:|
| `let x = 4` | 4 | Not declared | Not declared |
| `let before = x++` | 5 | 4 | Not declared |
| `let after = ++x` | 6 | 4 | 6 |

Output: `6 4 6`. Python has no increment operator; use `x += 1` to increase x.

| Expression | JavaScript | Python |
|---|---|---|
| `3 == "3"` | `true` through type conversion | `False` |
| `3 === "3"` | `false`, no type coercion | Not Python syntax |
| `"3" + 4` | String `"34"` | `TypeError` |
| Both conditions | `true && false` → `false` | `True and False` → `False` |

**Coercion** is automatic type conversion. JavaScript's strict equality `===` avoids it in this comparison.

**Try:** start again at x = 4 and execute only `let y = ++x;`.

**Check:** x = 5 and y = 5. Starting afresh matters; do not carry over the earlier x = 6.

## 10. Evaluate with evidence

Use three statements:

1. **Met:** “The corrected price function returns the hand-calculated result for all quantities 1–8.”
2. **Limit:** “I have not tested a booking store; the program does not contain one.”
3. **Next:** “I will test the text input path with `five` and confirm it gives a useful message.”

“All tests passed” means the checks you actually ran passed. Keep a test for the original defect and rerun it after changes. User feedback should lead to a specific improvement and another relevant check.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-09-testing/book-01-practice">2. Practise: repair the ticket calculator</a>. <a href="https://tutors.dev/note/lc-cs/topic-09-testing/note-02-feedback">Open the answers</a>.

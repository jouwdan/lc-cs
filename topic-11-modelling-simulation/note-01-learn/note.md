---
order: 1
---
# 1. Learn: Models

Test a model and explain its limits.

A short queue experiment shows how rules, randomness, and assumptions affect a result.

## 1. Model and simulation are different words

A **model** is a simplified representation of a system. A map is a model of a place. Our program is a model of a fictional help-desk queue. A **simulation** runs the model's rules to see what happens.

The question is: *what happens to the queue if service is more likely to finish each minute?* We keep arrivals, service, and waiting people. We leave out different request lengths and people abandoning the queue. This choice is **abstraction**. It makes the experiment manageable but limits what we can conclude about a real help desk.

**Try:** would the colour of the desk help answer our question? Would the time needed per request?

**Check:** colour probably would not; service time could matter greatly.

## 2. Use three rules in a fixed order

Start with zero people waiting. Each minute:

1. At most one person arrives: add 0 or 1.
2. A service opportunity can remove one person **if someone is present**.
3. Record how many people remain.

Arrivals happen before service, so a new arrival can be served in that minute. A service opportunity with nobody present removes nobody. The queue must never be negative.

| Minute | Before | Arrives | Service opportunity | Remaining |
|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 | 0 |
| 3 | 0 | 1 | 0 | 1 |
| 4 | 1 | 1 | 1 | 1 |
| 5 | 1 | 0 | 1 | 0 |

**Try:** arrivals `[1,1,1]`, services `[0,1,0]`. Trace each minute.

**Check:** remaining queues are `[1,1,2]`. Three people arrived, one was served, and two remain.

## 3. Name the parts of the experiment

| Part | Meaning | In this model |
|---|---|---|
| Initial condition | Starting state | Queue starts at 0 |
| State variable | Changes during the run | Current queue length |
| Parameter | Setting chosen for a run | Arrival/service probability, duration |
| Output | Measurement we collect | Remaining queue after each minute |

The **final queue** is the last value. The **maximum queue** is the largest. The **mean queue** averages all recorded values. For `[1,0,1,1,0]`, these are 0, 1, and 0.6 people. They are not waiting times, which would be measured in minutes.

To measure a person's wait, an extended model must record when that person arrived and when they were served. Do not relabel an easier number as the quantity you wanted.

## 4. Add controlled randomness

A probability is between 0 and 1. A service probability of 0.8 means an 80% chance of a service opportunity each minute under our rules. It does not promise exactly eight successes in every ten minutes.

```python
from random import Random
rng = Random(7)
arrives = rng.random() < 0.6
```

`random()` produces a number from 0 inclusive to 1 exclusive. Comparing it with 0.6 creates an event with probability 0.6. `Random(7)` uses a **seed**: the same seed recreates the same pseudo-random sequence, which is useful for checking a result. Create the generator once before the loop. Reseeding it every minute would keep restarting its sequence.

For dice, `rng.randint(1, 6)` includes 6; `rng.randrange(1, 6)` excludes it. `rng.choice(items)` chooses from a non-empty list. A six-roll sample need not contain every face once, even if the model is fair.

## 5. Compare fairly

Change one setting at a time. Our comparison holds arrival probability at 0.6 and duration at 120 minutes; it changes service probability from 0.5 to 0.8. Run each case with seeds 0–19. Record the settings so someone else can repeat the experiment.

A **stochastic** model uses randomness. Repeating it helps reveal variation: report a typical result and its spread, such as the lowest and highest run means. More runs reduce random sampling noise, but do not repair a missing real-world factor. A seed makes an experiment repeatable, not realistic.

**Predict:** which service setting should usually leave fewer people? Explain a mechanism before running it.

**Check:** the higher setting gives more service opportunities. In our paired runs, the same random arrival and service draws are used for each seed, so raising the service threshold cannot increase the queue under these particular rules. Different models or unpaired runs require their own comparison.

## 6. Ask two separate checking questions

**Verification:** does the program follow our rules? Compare it with the five-minute hand trace. Try no arrivals, no service, full service, and zero minutes. A useful invariant is a rule that must always remain true: `final queue = arrivals - served`, because we started with zero.

**Validation:** are those rules suitable for the real question? Compare with real observations, such as arrival rates and service times. A program can be verified and still leave out a crucial factor. **Calibration** adjusts parameters using evidence; it does not mean choosing values until you get the answer you hoped for.

Zero minutes have no mean recorded queue; our program returns `None`. Invalid probabilities such as 1.2 produce a clear error instead of silently changing the value.

## 7. Higher Level depth: agents and emergence

An **agent-based model** represents individual entities with their own state and local rules. A pedestrian agent has a position, moves towards an exit, and avoids nearby pedestrians. A crowd pattern such as lanes or congestion can arise from many interactions. That system-level pattern is called **emergence**; no pedestrian needs a global “make a lane” instruction.

Specify the environment, each agent's state, its interactions, and update order. If agent B sees agent A's newly updated position, that is sequential updating. If all decide from the old positions before moving, that is simultaneous updating. Results can differ.

**Small paper task:** put two agents beside a narrow doorway. State one movement rule and one collision rule. Explain whether they update together or in turn. You are defining a model, not claiming to predict a real crowd.

## 8. Finish with a limited conclusion

Use: “With these rules and settings, ___ changed from ___ to ___. This is explained by ___. The model omits ___. To improve it, I would measure ___.”

If you only measured remaining people, do not claim a reduction of a certain number of minutes waiting. If service was simplified to one opportunity per minute, do not infer an exact staffing recommendation for your school.

The practical begins with fixed events and adds randomness only after that trace works. The optional notebook repeats the **same** rules and function signature, so you can use it instead of installing Jupyter.


---

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-11-modelling-simulation/book-01-practice">2. Practise</a>. <a href="https://tutors.dev/note/lc-cs/topic-11-modelling-simulation/note-02-feedback">Open the answers when you have tried it</a>.

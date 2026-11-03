---
order: 4
---
# 4. Answers: Models

Check your reasoning and repair one gap.

Use the small trace to diagnose a rule error before changing the random model.

## Practical checkpoints

For arrivals `[1,0,1,1,0]` and service opportunities `[0,1,0,1,1]`, remaining queues are **`[1,0,1,1,0]`**. Arrivals total 3, served total 3, final queue 0. A service opportunity cannot serve a nonexistent person.

For `[1,1,1]` and `[0,1,0]`, queues are **`[1,1,2]`**. The final and maximum queue are 2; the mean queue is `4/3` people. None of those numbers is a waiting time.

With the supplied random model, `simulate(10, 0.6, 0.5, 7)` gives **`[0,0,0,1,1,1,2,2,2,2]`**. Repeating the same call reproduces it.

For 120 minutes, arrival probability 0.6, and seeds 0–19:

| Service probability | Mean of run means, people | Lowest to highest run mean |
|---:|---:|---|
| 0.5 | 7.379 | 1.333 to 16.200 |
| 0.8 | 0.581 | 0.175 to 1.267 |

Values are rounded for display. The higher service probability gives more opportunities to remove a waiting person. These are results of the specified model, not measurements from a real help desk. Same-seed comparisons use the same draws in both scenarios.

The no-arrival test checks an empty queue stays empty. The no-service test checks arrivals accumulate. Hand-trace agreement verifies the rules. Comparing with observations would help validate whether the rules fit reality.

## Quiz explanations

| Question | Correct choice | Why |
|---:|---|---|
| 1 | Run a model's rules | A simulation executes a model; it does not guarantee a prediction. |
| 2 | Queue length | It changes during the run; duration and seed configure it. |
| 3 | Reproducible pseudo-random sequence | A seed does not prove realistic assumptions. |
| 4 | `randint(1,6)` | Both endpoints are included; `randrange` excludes its stop. |
| 5 | Model validation | The code can follow rules that omit a crucial real factor. |
| 6 | Examine variation and typical outcomes | One stochastic run can be unusual. |
| 7 | Pattern from local interactions | Emergence is a collective result, not a global instruction. |
| 8 | 2 | The three remaining queues are 1, 1, 2. |
| 9 | No: different definitions and units | Queue length counts people; waiting time measures duration. |

**Retry:** if the trace was wrong, record arrivals before service and include the initial zero. If a seed confused you, rerun the same call twice, then change only the seed. For an agent explanation, name a state, local rule, and possible collective pattern.


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-11-modelling-simulation/note-03-exam-practice">5. Try one exam question</a>. <a href="https://tutors.dev/topic/lc-cs/topic-11-modelling-simulation">Back to the topic</a>.

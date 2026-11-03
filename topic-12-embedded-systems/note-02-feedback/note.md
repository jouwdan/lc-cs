---
order: 4
---
# 4. Answers: Embedded

Check your reasoning and repair one gap.

Compare each row with the controller's stated rules.

## Practical checkpoints

Calibration uses dry 800 and wet 300. Raw values 800, 550, 300 give relative levels 0, 50, 100. For 655, `100 × -145 / -500 = 29`.

| Level | Previous state | New state | Reason |
|---:|---|---|---|
| 45 | Off | Off | Above 40 |
| 29 | Off | On | Below 30 |
| 32 | On | On | Keep state in the band |
| 39 | On | On | Keep state in the band |
| 41 | On | Off | Above 40 |

At 30, 35, and 40, **both** prior-state tests are needed. Previously off stays off; previously on stays on. At 29.9 both turn on; at 40.1 both turn off. Disabled monitoring always forces off. Re-enabling at level 20 turns on at the next update.

For noisy levels `[29,31,29,31]`, the single-threshold rule gives on/off/on/off. Hysteresis gives on/on/on/on. The second rule remembers the state until the upper threshold is exceeded.

Identical dry/wet values are invalid calibration because the formula would divide by zero. A simulator can detect that software condition. It cannot measure the actual sensor or prove wiring is safe.

## Quiz explanations

| Question | Correct choice | Why |
|---:|---|---|
| 1 | Moisture sensor | It supplies input; an LED or motor receives output commands. |
| 2 | 1024 | `2^10` possible codes, numbered 0–1023. |
| 3 | 50 | A negative denominator correctly handles the sensor direction. |
| 4 | Reject and investigate | Equal references provide no usable range. |
| 5 | Stays on | Level 35 lies inside the keep-state band. |
| 6 | No | Physical calibration needs actual reference measurements. |
| 7 | PWM with changing duty cycle | The output switches on/off; it is not arbitrary smooth voltage. |
| 8 | Delayed response | A blocked program cannot immediately react to an input. |
| 9 | False | An offline dedicated controller is still embedded. |

**Retry:** if calibration failed, substitute each reference into the formula. If hysteresis failed, draw the two states and trace from both starting states. For a hardware explanation, name one input, one decision, and one output; then distinguish a simulated test from a physical one.


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-12-embedded-systems/note-03-exam-practice">5. Try one exam question</a>. <a href="https://tutors.dev/topic/lc-cs/topic-12-embedded-systems">Back to the topic</a>.

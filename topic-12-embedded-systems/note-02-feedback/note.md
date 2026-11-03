# 12 · Embedded systems: quiz feedback

Use these explanations after your first attempt. Correct the reasoning, then retry after a delay.

## Question 1

**Answer: A moisture sensor.** The sensor supplies information. LEDs and motors receive output commands.

## Question 2

**Answer: 1024.** There are 2^10 = 1024 combinations. Counting from zero gives a maximum code of 1023.

## Question 3

**Answer: 50.** 100 × (550−800)/(300−800) = 50. A negative denominator handles the direction correctly.

## Question 4

**Answer: Reject the calibration and investigate.** The denominator is zero, and the references provide no usable distinction. Check conditions and wiring.

## Question 5

**Answer: It stays on.** Inside the hysteresis band the previous state is preserved.

## Question 6

**Answer: No.** Simulation checks the model and decision logic. Physical calibration requires actual reference measurements.

## Question 7

**Answer: PWM with varying duty cycle.** The output switches digitally; changing the duty cycle changes average delivered energy for appropriate loads.

## Question 8

**Answer: It may delay response to a stop or enable input.** Polling cannot respond while the program is blocked. Choose timing to meet the system requirements.

## Question 9

**Answer: False.** Dedicated offline controllers are embedded systems too. Network connectivity is an additional design choice.

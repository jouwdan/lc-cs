# Embedded systems

Concepts, worked examples and practical reasoning for embedded systems.

## A computer inside a product

An embedded system is a computing system designed for a specific role within a larger device or environment. A washing-machine controller, thermostat or bicycle light can contain a processor, memory, inputs, outputs and a program. “Embedded” does not mean “connected to the Internet”: an offline controller is still embedded. An Internet of Things device adds network communication, introducing benefits such as remote monitoring and concerns such as security, power use and connectivity failure.

A general-purpose laptop supports many tasks. A microcontroller typically combines a processor, memory and peripheral interfaces on a chip and is often used for a dedicated control task. Select hardware according to inputs, outputs, timing, power, cost and operating conditions. A faster processor is not automatically the best choice for a battery-powered sensor that spends most of its time waiting.

## Electronics and real-time requirements

Voltage is electrical potential difference, measured in volts; current is the rate of charge flow, measured in amperes; resistance opposes current, measured in ohms. For an ohmic resistor, `V = I × R`. A resistor limits current or forms part of a voltage divider. A capacitor stores charge and can help smooth supply fluctuations or contribute to timing circuits. A transistor can act as an electronically controlled switch or amplifier; its switching behaviour is fundamental to digital logic. These components have different roles and are not interchangeable.

A **real-time system** must respond within a specified deadline. Correctness includes timing as well as the computed value. “Very fast” alone is not a definition: a response after the deadline may be useless even if it is numerically correct. A vehicle safety controller has stricter timing consequences than a classroom plant indicator. State a response requirement and test the worst relevant delay, including sampling and blocking operations.

## Follow the signal

Use an input-process-output diagram. In a plant-care indicator, the input is a moisture sensor reading and an enable button; processing converts the reading, compares thresholds and updates state; output is a warning symbol or LED. A sensor measures something in the environment. An actuator changes something physically, such as a motor moving a valve. A display is an output too, even when it does not control the environment.

Digital signals are interpreted as discrete states, often 0 and 1. Analogue signals vary over a continuous range. An analogue-to-digital converter (ADC) samples a voltage and represents it with a discrete number. With ten-bit readings there are 1024 possible codes, 0 through 1023. The code is not automatically a percentage or a temperature. It must be interpreted using the sensor and circuit's behaviour. A higher bit count gives finer code resolution, but accuracy also depends on calibration, noise and sensor quality.

On micro:bit MicroPython, `pin0.read_analog()` returns an integer from 0 to 1023, while a digital input returns 0 or 1. `write_analog` produces pulse-width modulation (PWM), not an arbitrary smooth output voltage. PWM varies the fraction of time a digital output is on. These API details come from the [official pin documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/pin.html). Other boards may use different ranges and voltage limits; read their documentation rather than copying constants.

## Calibration is part of the algorithm

Suppose a sensor reads 800 in your chosen dry reference and 300 in your chosen wet reference. A simple relative scale is:

```text
relative level = 100 × (reading − dry) / (wet − dry)
```

At 800 the scale is 0; at 300 it is 100; at 550 it is 50. The denominator is negative in this example, which correctly handles a sensor whose reading decreases as moisture increases. Do not assume all sensors have the same direction. If dry equals wet, calibration has failed and division would be invalid. Re-measure the references and inspect wiring.

This is a two-point relative calibration, not a scientifically certified percentage of water in soil. Sensor response may be nonlinear and affected by temperature or material. Record the physical conditions, several readings at each reference and the chosen values. Recheck when changing a sensor or environment. Values outside the reference range should be investigated and reported; clipping them to 0–100 can conceal a fault. Our practice program returns the calculated value so that this evidence remains visible.

## State, thresholds and hysteresis

A threshold controller makes a decision from a measurement. Turn a warning on below 30, for example. If the reading fluctuates between 29.9 and 30.1, a single threshold may cause repeated switching. Hysteresis uses two thresholds and remembers previous state: turn the warning on below 30, turn it off above 40, and keep the existing state in between. At exactly 30 or 40 our stated rules preserve state. Another convention is possible, but the tests must match it.

For levels `45, 29, 32, 39, 41`, starting off, warning states are `off, on, on, on, off`. Explain the memory in this system: an input of 35 does not determine the output on its own; the previous state matters. A finite-state diagram with two states makes the logic clear. An enable switch can force the output off. Define what happens when it is re-enabled and test that transition.

## Timing and noisy inputs

Polling repeatedly checks an input. An event-driven program reacts to events. The chosen sampling interval should match the rate of meaningful change. Sampling soil moisture thousands of times per second wastes energy and storage; sampling a fast-moving object once a minute misses important events. A blocking delay may make a stop button unresponsive, so consider how long the program can safely wait between checks.

Mechanical switches can bounce, creating several transitions during one press. Debouncing rejects changes that occur too quickly to be intentional, or uses an appropriate hardware circuit. A moving average can reduce random measurement fluctuations, but smoothing introduces delay and can hide brief changes. Explain the trade-off; do not add a filter simply because it looks sophisticated. Separate sensor-reading code from decision logic so simulated readings can test the controller.

## Build and test safely

For this course use an on-board display or a low-power LED indicator; do not connect mains electricity or drive a pump or motor directly from a board pin. A teacher should check the board's supply, pin limits, sensor compatibility and circuit before power is applied. An external LED needs the appropriate current-limiting component; a motor requires a suitable driver and protection. A labelled connection table is more reliable than relying only on wire colours.

Test individual components before integration: read the sensor, read the digital control, display a known pattern, then join the parts. Keep expected and actual results for dry/wet references, threshold boundaries, mid-band values, disable/re-enable and disconnected or implausible inputs. A software simulation verifies decision logic but cannot prove the wiring, calibration, voltage safety or response of real hardware. Record those limits explicitly.

## Data logging and automation

A useful log records time, raw reading, converted reading, digital input and output state. Include units and calibration identifiers. Store only what answers the investigation; long logs can fill limited memory. An offline system should continue to behave predictably if a network becomes unavailable. Decide a safe response to a failed sensor instead of assuming every reading is trustworthy. For our indicator, a distinct error message is better than displaying a plausible but invented moisture value.

Automation can improve consistency and reduce repetitive work, but it also transfers responsibility into the design. Who notices a failed sensor? Can a user override the decision? Is the output understandable without relying only on colour? These questions connect hardware, testing, accessibility and social impact. In an examination answer, explain a complete path from input through decision to output, and justify a chosen threshold with evidence rather than a guess.

## Practical achievement

The embedded ALT includes digital input/output and analogue measurement. A completed classroom task should include a design diagram, calibrated readings, executable control logic, a test record and an individual reflection. A simulator route supports learning when hardware is unavailable, but identify it clearly. The final practical check is whether you can predict a sequence of outputs, explain an unexpected reading and show which evidence would establish that the physical system works.

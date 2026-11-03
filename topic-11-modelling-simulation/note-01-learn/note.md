# Modelling and simulation

Concepts, worked examples and practical reasoning for modelling and simulation.

## The model is a deliberate simplification

A model represents selected features of a real system. A simulation executes a model's rules to explore what may happen. A drawing, equation or program can all be models; only some models are computer simulations. A useful model has a purpose. A lunch-queue model may help compare staffing options; it does not need to represent the colour of the counter. Abstraction removes irrelevant detail while retaining what affects the question.

List what is included and excluded before coding. For a simple queue we include arrivals, available servers, waiting people and time steps. We ignore individual order size, walking time and people leaving the queue. Those exclusions make the program manageable but restrict its conclusions. If order size strongly affects service time, ignoring it may produce unreliable staffing advice. A sophisticated animation cannot compensate for an unsuitable assumption.

## Variables, parameters and rules

A state variable changes as the model runs: queue length, current temperature or infected population. A parameter controls a run: arrival probability, service capacity or recovery rate. Initial conditions set the starting state. Inputs may include user-selected parameters or a data file; outputs might be a time series, maximum queue length or mean wait. Keep these categories explicit so another learner can reproduce the experiment.

For our queue, start with zero people. Each minute, one person arrives with probability `p`; then up to `servers` people are served; then record the queue remaining. The order matters. If service happened before arrivals, a new arrival could not be served until the next minute. Both conventions can describe a model, but switching silently changes results. State the convention and use it consistently in your hand trace, program and report.

With arrivals `[1, 1, 0, 1]`, one server able to serve one person every minute keeps the waiting queue at zero. That does not mean nobody used the service: it means nobody remains waiting after the service step. Output names must match what was measured. If arrivals can never exceed one and service always handles one, the model cannot produce congestion. To study queue formation, our executable version therefore gives the server a probability of completing service in each minute. This is a modelling decision, not merely a coding trick.

## Probability and pseudo-random numbers

A probability lies between 0 and 1. In Python, `rng.random()` returns a value in `[0, 1)`; `rng.random() < p` produces an event with probability `p`. For a die, `rng.randint(1, 6)` includes both endpoints. `randrange(1, 6)` excludes 6. Know the function's contract before interpreting output. A uniform die model assumes each face has equal probability; it does not prove a physical die is fair.

Pseudo-random generators calculate a reproducible sequence from internal state. A fixed seed helps reproduce a bug or compare a test. It does not guarantee the simulation represents reality, and changing the seed does not repair wrong rules. Do not reset the seed inside the loop: doing so can repeat the same first draw instead of producing the intended sequence. Use a local `random.Random(seed)` object to make the experiment's randomness explicit.

A single run may be unusual. If a fair die is rolled six times, there is no requirement that each face appears once. Repeated trials reveal variability. Report a distribution or at least mean, minimum and maximum across several seeds. More trials can reduce sampling noise in an estimate, but they do not remove bias from bad assumptions. Distinguish variation caused by random draws from uncertainty about the real arrival rate.

## Design an experiment before running it

Choose a baseline, change one parameter at a time, keep the run length and measurement definition fixed, and record seeds. For example, compare service probabilities 0.5 and 0.8 with arrival probability 0.6 for 120 minutes over 20 seeds. Predict that faster service will generally reduce queues. Do not promise every individual run will be lower, because random outcomes and model ordering matter.

Useful outputs include final queue length, maximum queue length and mean queue length over time. Mean queue length is not automatically mean waiting time; they are different quantities with different units. If you need each person's waiting time, record arrival times and remove them in queue order when served. A model should collect the quantity required by the question instead of substituting a convenient number.

## Verification and validation

Verification asks whether the program implements the intended rules. Hand-trace a short predetermined sequence and compare every state. Check invariants: queue length is never negative; a probability remains in range; total served never exceeds total arrivals plus the initial queue. Boundary tests include no arrivals, no service, full service, zero duration and invalid probabilities. Use exceptions to explain invalid inputs rather than quietly clamping them.

Validation asks whether the model is suitable for its real-world purpose. Compare simulated patterns with observations collected ethically, consult knowledgeable users and identify missing factors. A correct program can implement a poor model. Calibration adjusts parameters using evidence; it should not mean selecting values until a preferred conclusion appears. Reserve independent data for checking the calibrated model where possible.

## Higher Level extension: agents and emergence

An agent-based model represents individual entities with state and local rules. Agents could be pedestrians, vehicles or animals. A pedestrian may move towards an exit while avoiding nearby people. Large-scale lanes or congestion can emerge from many local interactions even when no rule directly says “form a lane”. Emergence is the appearance of a system-level pattern from interactions; it is not evidence that the model is intelligent.

Specify the environment, agent state, interaction radius, update order and movement rules. Updating agents one after another can differ from computing all decisions from the previous state and applying them together. Explain that choice. Compare before and after a rule change, document the new pattern and consider whether it matches plausible behaviour. Do not make claims about real populations from a toy model without appropriate evidence.

## Make conclusions proportional to evidence

A sound conclusion names the scenario, reports measurements, explains the mechanism and states a limitation. “Across these twenty seeded runs, a higher service probability reduced the mean remaining queue” describes the experiment. “One extra worker will eliminate all delays in our school” exceeds what the model supports. Recommend the next observation that would improve the model, such as service-time measurements at busy and quiet periods.

In examinations, read whether the task asks for a prediction, a trace, an explanation, a modification or an evaluation. The 2022 Higher Level practical uses random dice outcomes and frequencies; this gives a useful opportunity to distinguish expected proportions from guaranteed counts. The 2023 Higher Level guessing game and 2024 Higher Level fruit task also exercise randomness in programs. Our queue scenario is original practice. Consult each archived paper and scheme for precise requirements.

## Retrieval challenge

Explain the difference between a state variable and a parameter, why a seed supports reproducibility, and why a verified program can still be invalid for its purpose. Hand-trace three minutes with arrivals `[1, 1, 1]` and service successes `[0, 1, 0]`, applying arrivals before service. The remaining queue is `[1, 1, 2]`. Identify one assumption you would change before using the model to make an actual staffing decision.

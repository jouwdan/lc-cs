# Applied tasks and the project portfolio

Concepts, worked examples and practical reasoning for applied tasks and project portfolio.

## Learn by making and explaining

A computational artefact is something created using computing: a program, interactive site, model, visualisation or embedded system, for example. A useful artefact meets an identified need. Your portfolio should show both what works and how you reached it. A folder containing only a final screenshot cannot reveal decomposition, alternative designs, testing or your contribution. Keep evidence while working so reflection can be specific rather than reconstructed from memory.

The legacy course includes four collaborative applied learning tasks (ALTs): interactive information systems, analytics, modelling and simulation, and embedded systems. These learning activities develop skills for assessment. They are distinct from the SEC's individually completed coursework assessment. Collaboration is appropriate for ALTs; the assessed coursework follows the current brief and the teacher's authentication requirements. The [official coursework guidance](https://www.curriculumonline.ie/getmedia/b5e9833d-6842-4c85-b46e-a0897b72891e/CS-Coursework-Assessment-Guidelines-en.pdf) explains the distinction.

## A repeatable design cycle

Investigate the problem, plan the work, design a representation, create a version, evaluate it and document what you learned. These actions form an iterative cycle: evaluation often changes requirements or design. A staged process completes phases in sequence, which can help when requirements are stable; an iterative process revisits decisions through working versions and feedback. Neither label excuses poor testing or missing evidence. Explain why your approach fits the task.

A good requirement is observable: “A user can search by title and receives a clear no-match message.” A weak requirement is “the program is useful”. Separate functional requirements (what happens) from quality requirements such as response time, accessibility or robustness. Decide how you will test each requirement before writing code. Decompose the system into manageable responsibilities and define the data exchanged between them.

## ALT1 exemplar: community equipment library

**Brief:** help a fictional community centre discover what equipment is available. Interview classmates acting as users; do not collect real borrower details. Store item identifiers, descriptions, category identifiers and availability in a database. The interface must retrieve records, support a useful interaction such as search, and communicate unavailable items in text. A static page copied from a spreadsheet is insufficient evidence of retrieval.

Start from the database-to-browser pattern in topic 13, then design your own schema and interface. Deliver an entity/relationship sketch, at least two acceptance criteria, a working query, an accessible interface and a test record. **Higher Level extension:** use related tables, explain primary/foreign keys and compare two interface designs with evidence. Each learner should explain the whole data path and identify their own contributions. Evidence includes a successful search and a no-result or failed-request case.

## ALT2 exemplar: comparing fictional reading areas

**Brief:** investigate whether one reading area has lower synthetic sound readings during lunch. State a hypothesis and define fields, units and sampling assumptions. Use the supplied dataset or create a clearly labelled synthetic one. Preserve original rows, log cleaning decisions, calculate appropriate summaries and choose a graph that answers the question. Include a missing reading, an outlier and an uneven sample to make limitations visible.

Deliver the data dictionary, reproducible cleaning code, frequency/mean/median/mode calculations as relevant, a labelled graph and a restrained conclusion. Explain why the data cannot justify claims about all schools or every time of day. **Higher Level extension:** transform messy raw input and compare the effect of alternative defensible cleaning decisions. A successful investigation may reject the initial hypothesis. Marks in our classroom rubric reward the quality of reasoning, not a predetermined result.

## ALT3 exemplar: a help-desk queue

**Brief:** compare how service capacity affects a fictional queue. Define state, parameters, rules and outputs before coding. Use topic 11's model as a small starting point, then change one assumption deliberately. Run a baseline and a modified scenario over several seeds. Report variability, not only the most favourable run. Distinguish a waiting queue count from an individual's waiting time.

Deliver the model specification, a hand trace, tested code, recorded parameters/seeds and a comparison. Explain verification and validation separately. **Higher Level extension:** represent individual agents or investigate emergent behaviour, documenting interaction and update rules. A simulation does not become realistic because it contains many lines of code. Identify a real observation that would allow you to calibrate or challenge the model. Keep limitations next to conclusions so a reader cannot overlook them.

## ALT4 exemplar: plant-care indicator

**Brief:** combine a digital enable control, an analogue reading and an understandable output. Use the indicator in topic 12 to explore calibration, thresholds and hysteresis. A simulated sensor is acceptable for practising logic when hardware is unavailable, but mark the evidence as simulated. With hardware, use only teacher-approved low-voltage equipment and record actual calibration and response tests. The practice artefact is an indicator, not an unattended pump controller.

Deliver an input-process-output diagram, a connection table if physical, reference measurements, source code, logged test results and a demonstration. Include disable/re-enable, threshold boundaries and an invalid-input case. Explain the chosen sampling interval and a failure response. Each learner should be able to trace one reading from raw code to displayed state. This task connects electronics, abstraction, programming, testing and design decisions.

## Work effectively in a team

Agree roles such as coordinator, developer, tester and user researcher, then rotate them so everyone practises technical and communication skills. Pair programming can use a driver who enters code and a navigator who checks reasoning; swap regularly. Record decisions and tasks without turning the portfolio into surveillance of classmates. A brief contribution log should identify evidence, not merely state “we all helped”.

Resolve disagreements by returning to user needs and tests. If two designs both work, compare clarity, effort, accessibility and maintenance. A smaller complete artefact is often more educational than several half-working features. Use backups or version control and meaningful change descriptions. Keep data, code and reports organised so another learner can run the result without guessing the working directory or required files.

A role should be described through duties, not its title alone:

| Role | Two concrete responsibilities |
|---|---|
| Project manager | Plan tasks and milestones; monitor progress and coordinate changes when work falls behind. |
| Business analyst | Gather stakeholder requirements; translate needs into clear acceptance criteria and resolve ambiguities. |
| Developer | Implement the agreed behaviour; diagnose and fix defects in the code. |
| Tester | Design normal, boundary and invalid test cases; record outcomes and verify fixes. |
| UI designer | Produce interface layouts based on user tasks; check accessibility and refine the design after usability feedback. |

Small teams may combine roles, but responsibilities still need to be explicit. Rotating roles supports learning while keeping decisions accountable.

## Test plans and evidence

A test table contains requirement, input/setup, expected result, actual result, pass/fail and resulting action. Include normal, boundary and invalid cases. Test a component in isolation, then its connection to other components, then the complete user task. For a physical system, distinguish simulated expected output from measured behaviour. Save examples of a failure, its diagnosis, the fix and a successful retest.

“Tested and it worked” is weak evidence. A stronger entry says: “Searching an absent title should display a no-match message; the initial version showed old results; clearing the result list before processing the response fixed it; repeated test passed.” Explain why the change addresses the cause. Reflection should connect decisions to outcomes, including improvements still needed and the trade-offs they would introduce.

## Prepare for individual coursework

Read the relevant SEC brief with your teacher. Extract required features, permitted technologies, evidence, format, dates and authentication conditions. Do not assume a practice brief or a previous year's instructions applies unchanged. The legacy assessment allocates 30% to coursework and 70% to the end-of-course examination; the individual project is not simply the combined score of the four ALTs.

The coursework guidance describes digital artefact files and an HTML report including a demonstration video. Teach yourself to create semantic HTML, embed or link permitted local media correctly, explain design choices and demonstrate actual features. The live brief determines exact limits and structure. Keep your own code and narrative, acknowledge sources and follow supervision requirements. Practice examples in this course are learning aids, not finished work to submit as your personal assessed artefact.

## An original formative rubric

Use this 20-point classroom rubric for each practice ALT; it is **not an SEC marking scheme**. Award 0–4 in each area: (1) clear user need and testable requirements; (2) correct, understandable implementation; (3) meaningful testing and evidence of improvement; (4) communication and individual explanation; (5) responsible choices, accessibility and acknowledged limitations. A 4 means convincing specific evidence, 2 partial evidence and 0 no usable evidence. Intermediate scores reflect the quality between these descriptions.

Before teacher feedback, score your own evidence and justify each score with a file, result or decision. Then choose one achievable improvement. Mastery means you can explain, modify and test your artefact independently. A polished report cannot compensate for not understanding the program, and a working program still needs evidence that it meets its user's needs.

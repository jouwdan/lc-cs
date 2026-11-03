# 1. Learn: Projects

Organise evidence from a small project.

A **computational artefact** is something you make using computing: a program, website, graph, model or sensor system. A **portfolio** is a small collection showing the problem, your work, tests and improvements.

Here you will organise **one piece of existing practice work**. You do not need to finish four new projects before starting. Allow two 40-minute sessions.

## ALTs and the assessed project are different

| | Four applied learning tasks (ALTs) | Individual coursework assessment |
|---|---|---|
| Purpose | Learn by investigating and making things | Complete the project in the relevant SEC brief |
| Working with others | Collaborative learning | Individual work under the applicable assessment and authentication rules |
| What directs the work? | Four practical contexts in the specification | The brief, official instructions and teacher supervision |
| This course provides | Small practice examples and shared solutions | Preparation skills, not a finished project to submit |

**Authentication** means establishing that submitted work is your own. The specification used for these papers allocates 30% to coursework and 70% to the final examination. The ALTs are not four group submissions replacing that project. Read the [official coursework guidance](https://www.curriculumonline.ie/getmedia/b5e9833d-6842-4c85-b46e-a0897b72891e/CS-Coursework-Assessment-Guidelines-en.pdf) with your teacher. The actual brief sets your cohort's exact requirements.

## Start with one clear requirement

A **requirement** says what the system must do. An **acceptance test** checks whether it does that.

| Too vague | Testable version | Check |
|---|---|---|
| Make searching useful | Show “No items found” when no title matches | Search for an absent title |
| Make the page accessible | Give the search field a connected text label | Check the label and use the field with a keyboard |
| Calculate correctly | Return mean 6 for `[4,6,8]` | Compare with the hand calculation |

**Functional requirements** describe behaviour. **Quality requirements** describe qualities such as response time, accessibility and handling errors. Break the work into small parts: get input → check → process → show the result.

**Try:** rewrite “make a good indicator” as an input, rule and output. One answer: “When enabled and the level falls below 30, show a warning.”

## Use a small design cycle

1. **Investigate:** who needs what? Ask a user or use the fictional brief.
2. **Plan and design:** write requirements; sketch the data, algorithm or screen.
3. **Create:** build one working feature.
4. **Test and evaluate:** compare results with requirements and the user's need.
5. **Improve and record:** fix one issue, retest and explain the change.

An **iterative** approach repeats this cycle using feedback. A **staged** approach completes phases mainly in sequence and can suit stable requirements. Both need planning and testing. If a user changes a requirement after trying a prototype, iteration gives you a way to respond.

## Four ALT contexts: start small, then grow

These are original practice briefs. The starting tasks help you build towards the full learning context.

### ALT1 — interactive information systems

**Need:** a fictional centre wants people to find available equipment. Begin with <a href="https://tutors.dev/lab/lc-cs/topic-13-information-systems/book-01-practice">Topic 13&#x27;s database-to-browser lab</a>.

- **Start:** search a small database and display matching records. Show unavailable items in text. Use fictional item IDs, descriptions, categories and availability.
- **Keep:** a table sketch, two requirements, a working query, the screen and tests for a match and no match. A query demonstrates retrieval; a list typed into HTML does not.
- **Build further:** compare two screen designs with classmates acting as users. **Higher Level extension:** use related tables and explain primary/foreign keys. Explain the query-to-screen path and your contribution.

### ALT2 — analytics

**Question:** do synthetic readings suggest one reading area is quieter? Begin with <a href="https://tutors.dev/lab/lc-cs/topic-10-data-analytics/book-01-practice">Topic 10&#x27;s data lab</a>.

- **Start:** state a prediction, describe fields/units and analyse a small labelled synthetic dataset.
- **Keep:** original rows, cleaning log, appropriate frequency/mean/median/mode calculations, labelled graph and conclusion. Include missing data, an outlier and uneven samples to test decisions.
- **Build further:** compare two justified missing-data policies. Explain why the sample cannot describe all schools or every time of day. **Higher Level extension:** transform messy input and measure the effect of cleaning choices. A result that disagrees with your prediction is still useful.

### ALT3 — modelling and simulation

**Question:** how does service capacity affect a fictional queue? Begin with <a href="https://tutors.dev/lab/lc-cs/topic-11-modelling-simulation/book-01-practice">Topic 11&#x27;s queue lab</a>.

- **Start:** record state, parameters, rules and outputs; hand-trace a few steps; run a baseline and change one assumption.
- **Keep:** rules, tested code, parameters/seeds and results across several runs. Queue length and a person's waiting time are different measurements.
- **Build further:** explain verification (correct rules implemented) and validation (suitable model for the purpose). Name a real observation that could check the model. **Higher Level extension:** model agents and explain interactions, update order and patterns that emerge.

### ALT4 — embedded systems

**Need:** warn when a plant-care sensor level is low. Begin with <a href="https://tutors.dev/lab/lc-cs/topic-12-embedded-systems/book-01-practice">Topic 12&#x27;s indicator lab</a>.

- **Start:** combine a digital enable input, analogue reading and warning output in the simulator. Practise calibration, thresholds and hysteresis.
- **Keep:** input → process → output diagram, reference readings, code and tests. Include disable/re-enable, boundaries and invalid input. Label simulated results clearly.
- **Build further:** with teacher-approved low-voltage hardware, record connections, real calibration and response tests. Explain the sampling interval and fault response. Simulation checks logic, not wiring safety or physical accuracy. This practice is an indicator, not an unattended pump controller.

## A portfolio you can finish

Choose **one** practice artefact for this workshop. Make a folder with five items:

| Item | Minimum useful content |
|---|---|
| `start-here` document | Two sentences: user need and what works; instructions to run it |
| `design` | One sketch or trace and two requirements |
| `code-and-data` | Program and needed fictional data; credit starter examples |
| `tests` | Inputs, expected/actual results and a retest after a change |
| `reflection` | Your contribution, what changed, one limit and one next step |

These names are **practice suggestions**, not SEC submission rules. Later, link evidence from all four ALTs. Record unfinished contexts as “next to practise”; do not claim work you have not done.

### Worked evidence row

| Requirement | Test | Before | Change | Retest |
|---|---|---|---|---|
| No-match search displays a clear message | Search an absent title | Old results remained | Clear old results before showing the response | “No items found”; a normal search still works |

Keep the failure: it explains the change. Check a component alone, then connected components, then a whole user task: unit, integration and system checks.

## Teamwork: describe actions

| Role | Two responsibilities |
|---|---|
| Project manager | Plan tasks/dates; track progress and agree changes |
| Business analyst | Gather user needs; turn them into clear requirements |
| Developer | Implement behaviour; find and fix code defects |
| Tester | Design normal, boundary and invalid tests; record results and check fixes |
| UI designer | Sketch screens for user tasks; improve accessibility after feedback |

Rotate roles in collaborative practice. In pair programming, the **driver** enters code and the **navigator** checks reasoning; swap regularly. Keep one sentence about your contribution. Back up working versions. Resolve design disagreements by checking the same user need and tests.

## Before assessed coursework

With your teacher, read the relevant brief: required features, allowed tools, files, format, dates and authentication conditions. The coursework guidance describes artefact files and an HTML report with a demonstration video; the live instructions set exact structure and limits.

Practise clear HTML headings, working local links, readable media and demonstrations of real behaviour. Credit sources and keep your own code and explanation. Course examples are for learning, not for submission as your own assessed artefact.

## Practice self-check out of 20

This is our **classroom feedback rubric**, not an SEC marking scheme. Give 0–4 per row: 0 = no evidence, 2 = partial, 4 = clear specific evidence; use 1 or 3 for stages between.

| Area | Point to evidence |
|---|---|
| Need and requirements | Who is helped, and can you test success? |
| Implementation | Does it work, and can you explain it? |
| Testing and improvement | What failed, changed and passed on retest? |
| Communication and contribution | Can someone run it, and say what you did? |
| Responsible choices | Did you consider access, data, sources and limitations? |

Choose one small improvement from your weakest row. You should be able to explain, change and test the work; a polished cover page is not enough.


**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-15-project-portfolio/book-01-practice">2. Practise</a>.

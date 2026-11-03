# Student walkthrough and revision

Reviewed on 3 November 2026 from the perspective of a Leaving Certificate learner studying independently. This was a complete editorial walkthrough of all 17 topics, supported by executing the practical work and testing selected journeys in Tutors. It was not a classroom trial with students.

## What made the course hard to follow

The original course had broad coverage but often presented it as a reference manual. A new student had to infer the learning order, understand vocabulary before it was explained, locate files in a repository and decide what counted as a successful attempt. Long card titles and descriptions were clipped, hiding useful context.

The revision gives each topic a visible route: **Learn → Practise → Quiz → Answers → Exam practice**, with recap slides for later review. A session can end after one small example. The content and answers remain available for deeper study.

## Changes across the course

| Pain point | Change |
|---|---|
| The course opened with a large catalogue and no visible first action. | A short welcome panel links directly to Start here and explains the study route. |
| Resource cards appeared in type order, with recap slides before learning notes. | A numbered route sits above the cards. Titles identify each stage. |
| Ordinary Markdown links opened new tabs; fragment links could be rewritten to the asset host. | Internal course links use same-tab HTML anchors. Year/index jumps stay on the current page. |
| Titles repeated long topic names; descriptions were too long for cards. | Short contextual titles and one-sentence summaries; setup instructions and caveats stay inside activities. |
| Lessons introduced several abstract terms in one paragraph. | Short sections define terms, show worked examples and give small questions with checks. |
| Labs described a large finished project rather than how to begin. | Numbered actions, complete starting examples, filenames, inputs, expected results and a clear stopping point. |
| Some labs used syntax or concepts before teaching them. | Prerequisites are taught first; early algorithm work can be done on paper, and optional extensions follow the core. |
| Quiz feedback was difficult to find or too abstract. | Every quiz links to its Answers page; explanations connect to worked examples and suggest a repair. |
| External media appeared above the essential route. | Video, podcast and panel slides are optional reference resources with written alternatives. |
| Model files, notebooks and lab instructions were inconsistent. | Examples, starter packs, saved notebook outputs and instructions were checked together. |
| Exam lists required students to choose from many links without guidance. | Each topic suggests a first question. The full index pairs all 176 question groups with their matching schemes. |
| Teacher planning appeared in the first student lesson. | The 180-hour suggestion and teaching guidance sit in the teacher reference page. |

## Topic-by-topic walkthrough

| Topic | Main repair |
|---|---|
| 01 · Start here | A first 25-minute session, a complete `hello.py`, expected output, common setup fixes and a one-row study log. The initial diagnostic is optional. |
| 02 · Computer systems | One library example explains components, RAM/storage and OS jobs. The trace shows each instruction's effect. Registers versus RAM is explicit; `STORE` to main memory is distinguished from saving a disk file. |
| 03 · Binary and logic | Place-value and storage calculations are shown step by step. Core logic starts with two inputs; the three-input door is a labelled extension. Encoding, capacity, compression and higher-level reasoning remain. |
| 04 · Networks | Device and protocol roles have short examples. A request follows a concrete route. Threat/control tables include a mechanism and limitation, with specific failure checks. |
| 05 · Algorithms | A paper-first bus problem precedes optional runnable Python. Decision tables, state-space work and strategies are broken into traceable tasks. |
| 06 · Python | Values, functions, assertions and input handling are introduced before use. A ticket calculator grows through separate runnable files with expected boundary results. |
| 07 · Lists and files | A scaffolded median leads to a clearly located CSV file and complete reader. Missing/invalid file cases are explicit; dictionaries, runs and check digits are taught before extensions. |
| 08 · Search and sort | Each first pass is visible. Search edits specify indentation. Recursion precedes recursive tasks, and efficiency is explained as growing work. |
| 09 · Testing | A deliberately faulty booking program reproduces an observable error. Learners repair it, rerun previous checks and separate conversion, validation and logic faults. |
| 10 · Data | A four-number experiment comes before CSV cleaning. Exact rejection messages and results let students check their work. SQLite is a separate experiment. |
| 11 · Models | The lesson, lab and notebook share one queue model and update order. A hand trace precedes seeded random runs and comparison. Notebook cells are independently runnable. |
| 12 · Embedded | Software-only calibration comes before control state and hysteresis. Expected sensor and warning traces are shown. Physical hardware is an optional supervised extension. |
| 13 · Web and databases | A two-file local library demo gives a working first result. File placement, running, browser address, stopping and one-change-at-a-time edits are explicit. |
| 14 · Computing and society | Worked stakeholder reasoning, defined AI vocabulary, a numerical accuracy example and an explicit Turing-machine trace replace abstract prompts. |
| 15 · Projects | Students improve one existing artefact and keep five small pieces of evidence. Collaborative ALTs are clearly distinguished from individually assessed coursework. |
| 16 · Exam skills | A one-question attempt/mark/repair route comes before full papers. The original mock keeps its questions and 100-mark allocation, with clearer preparation and checking instructions. |
| 17 · Past papers | Each year has a level/language table pairing written paper, programming paper and scheme. Missing source variants and the separate Section C starter-file requirement are labelled. |

## What was preserved

- All **63 original PDFs**, byte-for-byte: 44 papers and 19 schemes from 2020–2025.
- All **176 English numbered question-group mappings**, with source-page references.
- All **16 quizzes / 153 questions**, plus the original mock and guide.
- All **14 Tutors learning-object types**, including notebooks, whiteboards and media.
- All existing topic, note, quiz and `book-*` lab paths. Optional embedded-media locations changed; they are linked from the relevant lessons.
- Ordinary/Higher Level support, all four applied learning contexts, original code examples and the full teacher reference.

## Verification and limits

See [VALIDATION.md](VALIDATION.md) for the final build and execution checks. The repository validator now also checks visible learning routes, answer links, course-owned link destinations, card-copy lengths and download consistency.

Browser checks cover the start-to-lesson-to-lab route, step navigation, quiz interaction, feedback, paper navigation and representative rendered cards. The local library application was checked with keyboard submission, visible focus, case-insensitive search and a no-results message. Executable examples and all core edits in the guided programming labs were exercised; deliberately broken examples were checked for the intended failure.

This work does not certify Irish/English paper equivalence, every browser/device, real hardware or third-party streaming availability. Written and software-only routes cover the core learning. The course remains scoped to the specification and archived exam period stated in the course reference.

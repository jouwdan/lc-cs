# Validation record

Validated on 3 November 2026 before the initial repository publication.

- Built with the published full generator `@tutors/tutors@5.3.0` under Deno 2.9.8. The generated tree contains **269 learning objects/steps**, including all **14 simple learning-object types**, 17 topics and 6 year units. Titles are nonempty and navigable internal routes are unique.
- Downloaded every one of the 63 source-listed PDFs. All parse successfully: **1,324 pages** total. SHA-256, byte count and page count are recorded in the manifest; copied build PDFs are byte-identical. Selected diagram-heavy pages were inspected visually.
- The coverage index has **176 English numbered question groups** with valid paper, scheme and page references. An independent review compared the taught material and worked examples with this index and the marking schemes; identified gaps were addressed.
- Ran all **153 questions in 16 quizzes** through the actual Tutors `extractQuizBlock` and `parseQuizMarkdown` functions from the accompanying Tutors monorepo. No questions were silently discarded. Reviewed keys and explanations, including code traces and boundary cases.
- Rendered **17 Marp decks / 116 slides** successfully with the installed Marp engine.
- All **12 Python example programs** passed their assertions, including local HTTP/database integration tests for successful queries and 400/404 responses. JavaScript operator assertions passed. Both notebooks execute from the first cell with Python's standard library; their saved outputs are included.
- The practical ZIP passed its CRC check. Both editable Excalidraw diagrams have populated elements. Course links into this repository resolve to existing files.
- Downloader parser tests: **2 passed**. The repository's `scripts/check_course.py` checks archive checksums, source structure, quiz answer ranges, notebook execution, diagram/ZIP structure and generated assets.
- Visually opened the generated course in Tutors Reader 17.0.0 and exercised quiz answering and progression. The local reader needed temporary aliases for existing workspace packages; no source changes were made to the Tutors monorepo.

## Limits

This is educational review and automated checking, not official SEC endorsement or a classroom trial. Irish PDFs were archived intact; their equivalence to the English versions was not independently certified. Every PDF page was not visually inspected. The 176 entries are numbered question groups, not separate records for every subpart.

Physical wiring, sensor calibration and device timing require checks on actual classroom hardware. External video/podcast availability and playback can vary; written alternatives are included. The notebook and quiz source contains answers and is suitable for self-study, not secure assessment. The course is now hosted at https://tutors.dev/course/lc-cs. An already-open reader tab retains its course data until a full reload.

## Lab navigation correction — 3 November 2026

The original generator-only checks missed a reader naming constraint: a `lab-*` root is mistaken for a chapter URL, while `book-*` opens correctly. Renamed all 16 topic lab folders to `book-01-practice`; their contents and runtime `lab` type are unchanged. The reference study journal already used `book-*`.

A regression check using the actual course service, Markdown conversion, LiveLab and lab page loader reproduced the failure against the original deployed JSON. Against the corrected build, all **17 lab roots and 67 step URLs** pass, including first-step activation, cached reopening, step indexes and previous/next boundaries (2 Vitest tests passed). The repository validator now enforces the compatible `book-*` source and generated IDs. Existing bookmarks containing `lab-01-practice` should be replaced by the updated links from the course topic page.

## Student-experience revision — 3 November 2026

See [the complete walkthrough](STUDENT-EXPERIENCE.md) for the pain points and topic-by-topic repairs.

- Rebuilt successfully with `@tutors/tutors@5.3.0`: **292 objects/steps**, all **14** simple learning-object types, **17** topics, **16 quizzes / 153 questions**. All **63** source PDFs and generated copies retain their original hashes; all **176** indexed question groups remain.
- Used the actual Tutors course service, lab page loader, Markdown conversion and quiz parser. **3 integration checks passed**, covering the prior failure reproduction, all **17 lab roots / 67 steps**, all **17 topic routes / 53 notes**, all quiz questions and same-tab study-route anchors. Tests used the built course JSON and mocked only network delivery and Svelte state seams.
- Rendered all **17 Marp decks / 153 slides** with the installed Marp engine. Every quiz passed the actual parser; the Python quiz was completed in the browser, including its code-trace question, submission and results. Corrected a quoted-string option that the reader had displayed with a missing opening quote.
- Programming topics 05–09: **56 execution/content checks** passed. These include completing the published inline starters, valid/invalid interactive input, exact outputs, CSV failures, empty inputs, original model assertions and JavaScript checks. Four expected-failure scenarios are intentional teaching examples, not unexplained failing checks.
- Extracted all four new starter packs for Topics 10–13 into fresh folders. Executed every instructed core edit and checked the stated results. Notebook cells run independently and match saved output. Library database/HTTP self-checks passed; browser checks confirmed initial results, keyboard submission, case-insensitive search, visible keyboard focus and the no-results message.
- Refreshed the complete practical ZIP to **40 files**. The validator checks its code/notebook bytes and the separate starter ZIPs against their source files.
- Checked short metadata in **251 source entries**. The built course's **190 cards** have titles of at most **27 characters** and descriptions of at most **45**. Browser measurement across the course home and all 17 topics found no clipped titles or descriptions in the tested desktop viewport after shortening the remaining seven titles. The validator enforces title/description limits for future edits.
- Every course-owned Tutors, repository-file and hosted-file link is checked locally. All 63 year-table document links match the archive manifest. The 176-row index has matching scheme links and valid PDF page references.
- Source lesson notes went from **79 prose blocks over 70 words to zero** using a simple paragraph count (excluding headings, tables, lists and code). This is evidence of shorter chunks, not a formal reading-age or learning-outcome measurement.
- Downloader tests: **2 passed**. `scripts/check_course.py` and `git diff --check` pass.

This remains an editorial and software walkthrough, not a classroom trial. Browser checks used desktop Tutors; every viewport, browser and assistive technology was not tested. Hardware, Irish/English equivalence and streaming limits still apply. Reload an already-open course tab after publication to replace its cached course data.

## Resource ordering correction — 3 November 2026

Numbering the titles did not override Tutors' default grouping by resource type. Added explicit `order: 1` through `order: 6` to all 96 primary resources across the 16 teaching topics. The reader now places Learn, Practise, Quiz, Answers, Exam and Recap before extra resources.

Rebuilt with the pinned 5.3.0 generator. A check using the actual Tutors `getUnits()` function passes for all 16 topics, including extras following the six stages. All 292 routes are unchanged. The repository validator now checks source and generated ordering metadata; its complete checks and `git diff --check` pass.

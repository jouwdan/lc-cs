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

Physical wiring, sensor calibration and device timing require checks on actual classroom hardware. External video/podcast availability and playback can vary; written alternatives are included. The notebook and quiz source contains answers and is suitable for self-study, not secure assessment. A hosted Netlify deployment has not been created by this repository publication; configuration and instructions are supplied.

# Leaving Certificate Computer Science

A comprehensive [Tutors](https://tutors.dev) study course for **Higher and Ordinary Level**, based on the **2020–2025 papers and marking schemes**. It follows the legacy Irish specification identified by Curriculum Online as applying to examinations through June 2028.

## What is included

- **63 intact PDFs:** 44 exam papers and 19 marking schemes, in every level/language variant listed by [Better Exams](https://www.betterexams.ie/leaving-cert/computer-science).
- **16 teaching topics plus an exam library:** substantial concept notes, worked examples, scaffolded labs, recap slides, quizzes and detailed feedback.
- **153 quiz questions** across 16 formative quizzes, plus an original 100-mark practice mock and worked marking guide.
- **All 14 Tutors learning-object types:** notes, labs/books, talks, tutorials, quizzes, notebooks, whiteboards, archives, web links, GitHub links, podcasts and the three panel types.
- **176 English question groups mapped to lessons**, with original-paper and matching-scheme page references.
- Executable Python and JavaScript examples, an HTML/database application, synthetic data, two notebooks, two editable whiteboards and a downloadable practical pack.
- All four applied learning contexts, separate individual-coursework guidance, differentiation, accessibility, a suggested 180-hour plan and an educator rubric.

All teaching examples and quizzes are newly authored. This is an independent learning resource, not an official SEC course or marking scheme. Answers are public for self-study.

## Study route

**[Open the course in Tutors](https://tutors.dev/course/lc-cs)** · [Start here](https://tutors.dev/topic/lc-cs/topic-01-start-here)

Every topic opens with a visible numbered route. Lessons use short sections, worked examples and check questions. Labs provide manageable steps, expected outputs and optional extensions. The original coverage and all 63 PDFs are retained.

[Student walkthrough and changes](STUDENT-EXPERIENCE.md)

### Topics

| Topic | Study |
|---|---|
| 01 | [Study routine, setup and feedback](topic-01-start-here/topic.md) |
| 02 | [Hardware, software and operating systems](topic-02-computer-systems/topic.md) |
| 03 | [Number bases, encodings and Boolean logic](topic-03-representation-logic/topic.md) |
| 04 | [Networks, protocols and cybersecurity](topic-04-networks-security/topic.md) |
| 05 | [Algorithms and computational thinking](topic-05-algorithms/topic.md) |
| 06 | [Python fundamentals](topic-06-python/topic.md) |
| 07 | [Strings, lists, functions and files](topic-07-data-structures/topic.md) |
| 08 | [Searching, sorting, recursion and efficiency](topic-08-search-sort/topic.md) |
| 09 | [Software design, testing and debugging](topic-09-testing/topic.md) |
| 10 | [Data, databases and analytics](topic-10-data-analytics/topic.md) |
| 11 | [Modelling and simulation](topic-11-modelling-simulation/topic.md) |
| 12 | [Embedded systems](topic-12-embedded-systems/topic.md) |
| 13 | [Interactive information systems and universal design](topic-13-information-systems/topic.md) |
| 14 | [History, society, ethics and AI](topic-14-society-ethics/topic.md) |
| 15 | [Four ALTs and the project portfolio](topic-15-project-portfolio/topic.md) |
| 16 | [Exam preparation and original mock](topic-16-exam-preparation/topic.md) |
| 17 | [2020–2025 paper library](topic-17-past-papers/topic.md) |

For each topic: **1. Learn → 2. Practise → 3. Quiz → 4. Answers → 5. Exam practice**. Use **6. Recap** for revision. Do one section and its task at a time; the suggested session lengths are guides, not deadlines. Shared core tasks support both levels; Higher Level extensions are labelled. The course is taught in English; archived Irish papers retain their original language.

## Exam archive and provenance

[Download manifest](exams/manifest.json) · [Question coverage table](exams/coverage.md) · [Machine-readable coverage](exams/coverage.json) · [Archive notes](exams/README.md)

| Year | Listed documents downloaded |
|---|---:|
| 2020 | 5 |
| 2021 | 12 |
| 2022 | 12 |
| 2023 | 12 |
| 2024 | 11 |
| 2025 | 11 |
| **Total** | **63** |

The archive contains 1,324 pages and 90,734,963 bytes of PDFs. Each manifest entry records its source, year, level, language, section, size, page count and SHA-256 checksum. All documents were retrieved on 3 November 2026.

**Source gaps:** Better Exams lists Higher Level only for 2020. It lists no Irish Ordinary Level marking scheme for 2024 or 2025. No documents have been invented to fill those gaps. The separate SEC Section C programming starter files are not part of this PDF collection; obtain them through a teacher or recreate the printed code carefully for practice. Historic timings, marks and question choices vary: follow the particular paper.

The coverage index maps every numbered English question group; multi-part questions can span several lessons. It does not independently translate or certify equivalence of the Irish versions. Original PDFs and the matching schemes remain authoritative.

## Build the Tutors course

Install [Deno](https://deno.com), then run from this repository:

```sh
deno run -A jsr:@tutors/tutors@5.3.0
```

This produces `json/tutors.json` and the PDF/ZIP/whiteboard assets. Generated files are ignored by Git. Author lab folders as `book-*`; they still generate Tutors learning objects of type `lab`. The current reader relies on that folder prefix when opening the first step, and the validation script checks it.

Use the full Tutors generator: `tutors-lite` does not provide all the interactive object types used here.

The six study cards in each teaching topic use YAML front matter `order: 1` through `order: 6`. Keep this metadata on the resource's Markdown file (the first step for labs, `talk.md` for slides). Numbers in titles alone do not control display order. Unordered extra resources follow the six study stages.

The course is published at [tutors.dev/course/lc-cs](https://tutors.dev/course/lc-cs), using assets at `https://lc-cs.netlify.app`. Netlify builds the `main` branch using `netlify.toml`.

For your own copy, connect the repository to a Netlify site and use that site name in the Tutors course URL. Internal course links in the source currently point to `lc-cs`; update them when making a separately hosted copy.

Internal links use plain HTML anchors because the current reader opens Markdown links in new tabs. This keeps the study route in one tab. After a published update, fully reload an already-open course tab to clear the reader’s in-memory course cache.

## Verify or maintain

Python 3 is sufficient for the offline source and checksum checks and for the worked programs. The published course itself does not require a Python server.

```sh
python3 scripts/check_course.py
python3 scripts/test_download_exams.py
```

The first command verifies the 63 PDF checksums, 176 coverage references, quiz structure, executable notebooks, course-owned link destinations, visible study routes, answer links and download contents. After a build, it also verifies all 14 learning-object types, unique navigable routes and byte-identical copied PDFs. The actual Tutors quiz parser and Marp renderer were additionally exercised during authoring; see [validation notes](VALIDATION.md).

The reference `solution.py` and `solutions.py` programs include assertions. The guided lab files also include interactive examples and a deliberately faulty booking program, so do not expect every `.py` file to pass without input. Run the reference solutions for their checks; run `python3 code/information-system/server.py --check` for the local HTTP/database tests. `node code/topic-09-testing/operator-checks.js` verifies the historical JavaScript examples. The web application runs on loopback only and uses fictional data. Embedded examples are simulations; real devices require safe wiring checks and calibration.

To refresh the source PDFs, run `python3 scripts/download_exams.py` from the repository. It downloads the listed collection and updates provenance. Review any changed source files and counts before committing.

[Educator guide](side-reference/note-02-educator-guide/note.md) · [Curriculum mapping and primary sources](side-reference/note-01-specification/note.md) · [Practical ZIP](topic-01-start-here/archive-01-practical-pack/practical-pack.zip) · [Sources and rights](RIGHTS.md)

## Rights and boundaries

The SEC papers and embedded third-party material retain their original copyright notices; no blanket repository licence covers them. External recordings are linked or embedded from their creators. Newly authored lessons and practice tasks are clearly distinct from official exam material. The course is scoped to the 2020–2025 paper set and legacy specification, not the replacement specification introduced in September 2027.

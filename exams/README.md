# Exam archive and provenance

Downloaded from [Better Exams: Leaving Certificate Computer Science](https://www.betterexams.ie/leaving-cert/computer-science) on 3 November 2026. The source attributes these documents to the State Examinations Commission.

All 63 listed PDFs are preserved byte-for-byte: 44 question papers and 19 marking schemes, 1,324 pages in total. The archive is organised as Tutors tutorial learning objects in the past-paper topic. English and Irish versions are available only where the source lists them.

| Year | Papers | Schemes | Total |
| --- | ---: | ---: | ---: |
| 2020 | 4 | 1 | 5 |
| 2021 | 8 | 4 | 12 |
| 2022 | 8 | 4 | 12 |
| 2023 | 8 | 4 | 12 |
| 2024 | 8 | 3 | 11 |
| 2025 | 8 | 3 | 11 |

## What the evidence files contain

- [manifest.json](manifest.json): source URL, year, level, language, section, local file path, byte count, SHA-256 checksum and PDF page count for every download.
- [coverage.md](coverage.md): readable question-to-module map for every numbered question group in the English papers.
- [coverage.json](coverage.json): the same map as structured data, together with marking guidance and source caveats. A row summarises all parts of a numbered question; it is not an official SEC learning-outcome classification.

The 2020 listing supplies Higher Level only. It has no Irish marking scheme. The 2024 and 2025 listings have no Irish Ordinary Level marking scheme. These are source-listing gaps, not failed downloads. They do not establish what existed elsewhere or which assessments were administered.

## Using the archive

Attempt a question before opening its scheme. Match year, level and section, and follow the instructions printed on that year's paper. Record misconceptions, redo the related course activity and retry later without notes. Schemes contain indicative alternatives and examiner guidance; self-marking is formative. In particular, 2021–2022 papers use different choices and mark totals from later papers.

The PDFs retain their original copyright notices and are excluded from any licence covering original course material. SEC and third-party rights remain with their owners. The archive supports educational examination preparation; inclusion does not grant a general right to republish or adapt third-party content.

## Verify or repeat the download

Run `python3 scripts/test_download_exams.py` from the repository root for the small offline parser check. Run `python3 scripts/download_exams.py` to re-read the six listings and fill missing files. The downloader checks expected counts, PDF signatures and existing recorded checksums. It stops on a changed listing count or changed archived content so an educator can inspect the change. The checked-in manifest additionally records page counts validated with pypdf.

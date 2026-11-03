---
order: 1
---
# 1. Learn: Exam skills

Attempt, mark, repair and retry.

Use this cycle: **attempt → mark → fix one gap → retry**. Start with one question. Build up to whole sections after you can use the cycle yourself.

You need paper or a document, a timer and the question PDF. For programming, you also need Python and the required starting code. Allow two 30-minute sessions for your first attempt and review.

## 1. Pick one question

Choose a skill you have already studied. Use the links below or the <a href="https://tutors.dev/note/lc-cs/topic-16-exam-preparation/note-03-exam-practice">topic question list</a>. Start at your level; a short Ordinary Level task can also help repair a shared skill.

| Starting task | Paper | Scheme: open after trying |
|---|---|---|
| Selection-sort trace | [2025 Ordinary Q11](https://raw.githubusercontent.com/jouwdan/lc-cs/main/topic-17-past-papers/unit-2025/tutorial-exam-paper-section-aandb-ordinary-level-ev/exam-paper-section-aandb-ordinary-level-ev.pdf#page=9) | [Scheme](https://raw.githubusercontent.com/jouwdan/lc-cs/main/topic-17-past-papers/unit-2025/tutorial-marking-scheme-ordinary-level-ev/marking-scheme-ordinary-level-ev.pdf#page=8) |
| Python output trace | [2025 Higher Q1](https://raw.githubusercontent.com/jouwdan/lc-cs/main/topic-17-past-papers/unit-2025/tutorial-exam-paper-section-aandb-higher-level-ev/exam-paper-section-aandb-higher-level-ev.pdf#page=3) | [Scheme](https://raw.githubusercontent.com/jouwdan/lc-cs/main/topic-17-past-papers/unit-2025/tutorial-marking-scheme-higher-level-ev/marking-scheme-higher-level-ev.pdf#page=4) |

Open the paper first. Read the whole selected question, including diagrams and subparts. Write its **year, level, section and question number** above your work. Keep the scheme closed until you have tried.

## 2. Check instructions and set a small target

For one question, choose a study target such as “10 minutes, without notes”. This is your practice choice, not an official allowance. For a full paper, read its front pages for choices, marks, duration and permitted materials.

Historical instructions differ. The 2020 Higher A/B paper says answer all questions. The 2025 Higher A/B paper asks for nine short and two long questions. Section C is worth 50 marks in 2021–2022 and 80 in 2020 and 2023–2025. Use the actual paper, not a remembered rule or a future prediction.

### Example: a full 2025 Higher Level practice session

| Paper | Printed total | Suggested practice split |
|---|---|---|
| A/B | 90 minutes; 130 marks: A 54 + B 76 | Read/select 5; A 32; B 45; check 8 minutes |
| C | 60 minutes; 80 marks | Inspect 5; code 40; test 10; saved-file check 5 minutes |

For B, that gives about 22–23 minutes per chosen long question. Adjust within the session using subpart marks and progress. These splits are teaching suggestions; read permitted materials and submission rules separately. Save regularly throughout C.

## 3. Answer the command word

| Word | What to put on the page | Small example |
|---|---|---|
| State | A fact or result | “RAM is volatile.” |
| Describe | Features or steps | Describe what changes during a loop |
| Explain | Why or how | “A missing update can leave the condition true, so the loop repeats.” |
| Compare | Relevant similarities/differences | Compare RAM and SSD by volatility |
| Evaluate | Benefit, limitation and supported judgement | Explain when an automated system would be useful |
| Justify | A choice with reasons | Explain why a line graph suits a time series |
| Trace | Execution in order | Record variables after each loop iteration |
| Calculate | Working and answer | Sort values, then find the median |
| Design | A solution meeting the constraints | Draw an algorithm with a valid exit path |

If asked for two reasons, give two different reasons. Apply them to the scenario. A longer answer does not automatically earn more marks.

## 4. Make your reasoning visible

- **Code trace:** record assignments, loop limits and exact printed output; distinguish a variable's value from a printed line.
- **Numbers/logic:** show place values, requested bit width and intermediate truth-table columns.
- **Systems:** label components and show information direction.
- **Data/models:** show sorted values for a median, explain missing-data choices and state model assumptions. Distinguish verification from validation.
- **Society:** name the feature, person affected, consequence and limit or mitigation.

When time ends, keep the first attempt. Put later untimed work in a different colour or separate copy.

## 5. Mark with the matching scheme

1. Open the scheme from the **same row** as the paper link. Check year, level and question number.
2. Read one subpart's allocation. Underline the evidence in your answer that meets it.
3. Record marks earned and available, plus a short reason for lost marks. Use the scheme's own allocation; there is no universal rule for partial marks.
4. If your wording differs but the meaning may be valid, flag it for a teacher rather than assuming it is right or wrong. Schemes can allow alternatives.

**Example error log:** “I wrote only the final sorted list; the question asked for each swap. Repair: record the list after every swap. Retry: a different sorting trace.”

A raw practice score describes that attempt under those conditions. It is not a prediction of your final grade.

## 6. Repair and retry

Choose one cause: missing fact, wrong idea, calculation slip, incomplete explanation, code error or time pressure. Do a small repair: trace one loop, explain one difference or test one boundary. After a day or two, attempt a different question on that skill without notes. If you needed help, record it and try again later.

## Programming: prepare before the timer

Read supplied code to identify inputs, outputs, initial values, loops and required filenames. Save a working copy as instructed. Add one requirement, run it, then add the next. If output is wrong, trace a small input before changing several lines.

The PDF archive does **not** contain every official Section C `.py` starter file. Get the files through your teacher when available. For practice you can carefully recreate code printed in the PDF, checking indentation and names against the actual page. This course's programs are original examples, not official starters.

Predict a normal, boundary and invalid case before testing. For a median: empty, odd, even and unsorted lists. For a longest run: a break in the middle and a run at the end. Check output spacing and saved filenames when the question requires them. One passing sample is not enough.

## Build up your practice

Use topic questions first, mixed questions next and whole sections last. Practical contexts include:

| Year | Higher Level | Ordinary Level |
|---|---|---|
| 2020 | Password scoring | No Ordinary paper listed in this collection |
| 2021 | Anagrams | PIN/ATM logic |
| 2022 | Dice frequencies | Shop calculations |
| 2023 | Guessing game | Times tables and temperature alerts |
| 2024 | Random fruit | Age eligibility and bill splitting |
| 2025 | Grade statistics | Tiling costs |

The contexts change, but you keep using validation, selection, loops, counts, totals, comparisons and explanations. Open the exact question before assuming its requirements.

## When ready: the original mock

<a href="https://tutors.dev/note/lc-cs/topic-16-exam-preparation/note-03-original-mock">Open the 100-mark course mock</a>. Allow 60 minutes for written work and 60 for Python, or split it into two sessions. Its format and marking are original teaching choices, **not an SEC paper format**. Keep the first attempt, then use its separate guide and choose three repairs.


**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-16-exam-preparation/book-01-practice">2. Practise</a>.

# 4. Answers: Web apps

Check your reasoning and repair one gap.

Check the visible result and the data path that produced it.

## Practical checkpoints

| Search/action | Expected baseline |
|---|---|
| Empty search | 4 books |
| `river` or `RIVER` | River Patterns; The River Journey |
| `volcano` | No-match message |
| `Stars &` | Stars & Stories; Available |
| Stop server, then submit | Clear connection/server error |

River Patterns is in Science and is Available. The River Journey is in Stories and is On loan. Changing only its final database value from 0 to 1, restarting, and refreshing makes it Available. Restoring 0 restores On loan. Editing the heading changes visible page content but not database records.

The path is: form input → HTTP request → Python handler → parameterised SQLite join → JSON response → JavaScript → visible result. The join matches `Book.category_id` with `Category.category_id`. It brings in the category's name without repeating that name in every book row.

A useful requirement is “the search works using Tab and Enter, with visible focus”. A useful test records the actual outcome at 200% zoom or on a narrow window; do not claim accessibility only because the source includes a label.

## Quiz explanations

| Question | Correct choice | Why |
|---:|---|---|
| 1 | Connected label | The matching `for`/`id` gives the control a persistent accessible name. |
| 2 | Presentation and layout | CSS styles; HTML structures; JavaScript adds behaviour. |
| 3 | Treat returned values as text | `textContent` does not interpret an unexpected title as HTML. |
| 4 | Secured server if needed | Browser source is delivered to users and cannot hold a server secret. |
| 5 | Relates a record to another table's key | The foreign key connects Book to Category; a primary key identifies a row. |
| 6 | Page checks can be bypassed | The server must enforce its own input contract. |
| 7 | System test | It exercises the whole user task through the integrated system. |
| 8 | No | A static copied list does not demonstrate a database query. |
| 9 | River search returns matching titles | It has a clear input and observable expected result. |

**Retry:** if the technologies blur together, label one line of HTML, one CSS rule, and one JavaScript action in `index.html`. If the join is unclear, match the two category keys on paper. If a test failed, restore the supplied baseline and change one thing at a time.

**Example reflection:** “A reader needed availability in plain text. I changed a seeded record and confirmed the displayed label changed after restarting. The search worked with my keyboard and at 200% zoom. This local demo has no persistent editing, authentication, or real library records.” Only claim the checks you actually performed.


---

**Next:** <a href="https://tutors.dev/note/lc-cs/topic-13-information-systems/note-03-exam-practice">5. Try one exam question</a>. <a href="https://tutors.dev/topic/lc-cs/topic-13-information-systems">Back to the topic</a>.

# Interactive information systems

Concepts, worked examples and practical reasoning for interactive information systems.

## Begin with people and requirements

An information system combines people, procedures, data, hardware and software to support a purpose. A website is one possible interface to that system. Begin by identifying an actual user task: “A learner can find which fictional library books are available.” A vague goal such as “make a good website” cannot be tested. Write measurable acceptance criteria: searching for `river` finds matching titles; an empty search lists all books; unavailable books are identified in text; keyboard users can reach every control.

Gather several perspectives before choosing a design. A reader wants clear results; a librarian wants accurate stock; a learner using a screen reader needs meaningful labels. Use synthetic records during development. Requirements may conflict: collecting more personal data could aid recommendations but reduce privacy. Explain the choice and collect only what is needed. A classroom information system can be useful without account registration or any personal data.

## Sketch before styling

A wireframe shows the arrangement of headings, controls and results without detailed decoration. Draw a search field, a clearly labelled button, a status message and a results list. Walk through the task with a partner. What happens on first load, after no match, while loading and after a server error? Error states belong in the design; a blank screen is not helpful feedback. Keep navigation predictable and distinguish a control's label from placeholder text that disappears while typing.

Usability concerns how effectively and comfortably people achieve their tasks. Accessibility removes barriers for people with differing abilities and technologies. Use sufficient contrast, readable text, visible keyboard focus, semantic structure and alternatives for non-text content. Do not communicate “available” only through green colour. Test at increased zoom and with only the keyboard. **Higher Level extension:** compare two interfaces using the same task and evidence, rather than saying one “looks nicer”. Explain the benefit and cost of each design decision.

## Seven universal-design principles in practice

The [Centre for Excellence in Universal Design](https://universaldesign.ie/about-universal-design/the-7-principles) names seven principles. The examples here are original applications to our library task:

| Principle | Concrete application |
|---|---|
| Equitable use | Offer the same search information to keyboard and pointer users. |
| Flexibility in use | Permit either typing a title or browsing all titles. |
| Simple and intuitive use | Use a clear “Search books” action and predictable reading order. |
| Perceptible information | Show availability in text, with sufficient contrast. |
| Tolerance for error | Explain an invalid query and preserve the user's input for correction. |
| Low physical effort | Avoid unnecessary repeated input and long sequences of clicks. |
| Size and space for approach and use | Give controls adequate target size and spacing, including on small screens. |

A principle should lead to an observable design decision. Merely listing seven names does not evaluate an interface. Test with users and acknowledge that preferences can differ.

## HTML describes meaning

HTML supplies document structure. Use a single main heading, logical subheadings, paragraphs, lists and appropriate form elements. A label connected through `for` and `id` gives an input an accessible name. A `button` is already a keyboard-operable control; a clickable `div` is not an equivalent replacement. A table is appropriate for genuinely tabular data and needs column headings. Images require useful alternative text unless decorative.

```html
<label for="search">Book title</label>
<input id="search" name="q" type="search" maxlength="100">
<button type="submit">Search books</button>
<p id="status" role="status"></p>
```

The status region can announce changed results to assistive technology without moving focus unexpectedly. Do not put the entire interface inside a live region. Set the page language and a descriptive browser title. These small structural choices improve meaning for people and software.

A complete minimal page has a document declaration, a root `html` element, metadata in `head`, a browser-tab `title`, and visible content in `body`. An anchor's `href` identifies its destination; it is not the link's visible wording. A `ul` contains unordered-list items marked with `li`.

```html
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Library guide</title></head>
<body>
  <h1>Library guide</h1>
  <ul><li>Search by title</li><li>Check availability</li></ul>
  <a href="https://www.curriculumonline.ie/">Curriculum resources</a>
</body>
</html>
```

## CSS controls presentation

CSS describes layout, colour, spacing and typography. Use classes for reusable styles and keep content understandable if styling is unavailable. Relative widths and a maximum content width help the layout fit narrow screens and large monitors. A visible focus outline tells a keyboard user where they are. Styling should reinforce hierarchy: a heading should be recognisable because it is a heading, not merely a large bold paragraph.

Separate presentation from data. A database field should store whether a book is available, not the colour of its label. If the colour palette changes, the data should remain meaningful. Avoid fixed heights that clip enlarged text. Test long titles and zero results, because layouts often appear correct only with ideal sample content.

## JavaScript adds behaviour

JavaScript can listen for a form submission, read a value, request data and update the Document Object Model (DOM). Prevent the form's default navigation when handling it asynchronously. Show a loading status, then either results or an understandable error. A failed request must not leave the user believing old results are current.

Use `textContent` when inserting a title obtained from data. Treat data as text instead of interpreting it as HTML. A string containing angle brackets should display as a title, not become executable markup. Client-side validation improves feedback, but the server must validate input too because callers can bypass the page. For a search field, a length limit and an explicit query contract keep the example understandable.

## The browser does not directly own the database

Our runnable example uses this path:

```text
Browser form → HTTP GET /api/books?q=river
→ Python request handler → parameterised SQLite query
→ JSON response → JavaScript → visible results
```

The server mediates database access. It chooses permitted operations and returns only the required fields. A server-side database password must never be included in browser JavaScript. Our local demonstration needs no password because it uses only seeded synthetic data and binds to the loopback address `127.0.0.1`. It is a learning server, not a hosted school records system.

HTML, CSS and JavaScript are distinct from the data representation JSON. JSON contains values; JavaScript is a programming language that can parse those values. HTTP is a request/response protocol. Explain which component performs each step rather than referring to everything as “the website”.

## Relational design and queries

We store `Category(category_id, name)` and `Book(book_id, title, category_id, available)`. The category key links a book to its category. A join retrieves a book title and category name without repeating the name in every book record. Primary keys identify rows; foreign keys describe relationships and can enforce integrity when configured. A many-to-one relationship means several books may refer to the same category.

```sql
SELECT book.title, category.name, book.available
FROM book JOIN category
ON book.category_id = category.category_id
WHERE book.title LIKE ?
ORDER BY book.title;
```

For a concrete trace, suppose Category contains `(1, Science)` and `(2, Stories)`. Book contains `(1, River Patterns, 1, 1)` and `(2, The River Journey, 2, 0)`. With the parameter `%River%`, the join returns `River Patterns | Science | 1` and `The River Journey | Stories | 0`, in title order. The foreign-key value 1 retrieves Science; it is not the book's availability value even though both happen to be 1. Changing category 1's name changes the joined label for every book in that category without changing each book record.

The placeholder receives a search pattern as a parameter. User text does not become SQL instructions. Decide whether wildcard characters are permitted and explain that contract; our small example follows SQLite's `LIKE` pattern semantics. The result order is explicit. For a larger system, constraints, indexing, authorisation and deployment security would require further design, but they are not reasons to hide the essential data path from beginners.

## Test the experience and the implementation

Unit tests can check query results. Integration tests check that an HTTP request produces the expected JSON and status. System tests follow the whole user task in a browser. Include empty search, no match, long input, special characters, unavailable records and server failure. Check that all returned text is inserted safely, and that keyboard focus remains visible. A successful query does not prove the interface is usable; a polished interface does not prove its records are correct.

The ALT1 brief asks learners to create an interactive information system. Copying a static list into HTML does not demonstrate database retrieval. Show the database structure, an actual query, the response and its visible result. In your reflection, explain a user need, one change after feedback, a testing result and a remaining limitation. Keep each student's contribution and learning clear even when the ALT is developed collaboratively.

## Review before moving on

Trace a search from input to displayed result. Explain why HTML semantics, SQL parameters, server validation and error messages solve different problems. Compare an interface with clear text availability labels against one that uses colour alone. Then change the practice site's context and requirements to produce your own design, rather than merely changing the heading.

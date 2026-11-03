# 1. Learn: Web apps

Connect a web page to a database.

Use a small fictional library to follow the complete path from a user's question to a result.

**Study in two parts:** sections 1–4 explain the page. Sections 5–8 explain the database and testing. The practical supplies a working site, so you can run it before editing it.

## 1. Begin with a person and a task

An **information system** combines people, procedures, data, hardware, and software for a purpose. A website is one interface to it. Our task is: *find a book by title and see whether it is available*.

A **requirement** says what the system must do. “Look nice” is hard to test. “Searching `river` returns two matching books, with availability written in words” is testable. A reader needs understandable results; a librarian needs accurate records; a keyboard user needs reachable controls. These people are **stakeholders** because the system affects them.

**Try:** write one testable requirement for an empty search.

**Check:** “An empty search lists all four fictional books” is precise. No accounts or personal records are needed for this example.

## 2. Sketch the interaction before decorating it

A **wireframe** is a simple layout sketch. Draw a heading, labelled search box, Search button, status message, and results. Then draw what happens when there are no matches or the server is unavailable. A blank area is not a useful error message.

**Usability** concerns how easily people complete the task. **Accessibility** concerns removing barriers for people with different abilities and technologies. A green dot alone does not tell everyone a book is available; include the word “Available”. A placeholder disappears when someone types, so it should not replace a persistent label.

## 3. Give HTML, CSS, and JavaScript different jobs

| Technology | Job | Example |
|---|---|---|
| HTML | Structure and meaning | Heading, label, input, list |
| CSS | Presentation | Spacing, colour, layout, visible focus |
| JavaScript | Behaviour | Submit search and display returned books |

```html
<label for="search">Book title</label>
<input id="search" type="search">
<button type="submit">Search books</button>
<p id="status" role="status"></p>
```

The label's `for` matches the input's `id`. A real button already supports normal keyboard operation. The status region can announce new results to assistive technology without unexpectedly moving focus.

A complete HTML file also needs a document declaration, a root element with a language, a `head` containing metadata and a browser title, and a `body` for visible content:

```html
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Library guide</title></head>
<body>
  <h1>Library guide</h1>
  <ul><li>Search titles</li><li>Check availability</li></ul>
  <a href="https://www.curriculumonline.ie/">Curriculum resources</a>
</body>
</html>
```

**Try:** which part is the link destination, and which words appear on screen?

**Check:** `href` gives the destination; “Curriculum resources” is the visible text. A `ul` holds an unordered list of `li` items.

CSS should allow narrow screens and enlarged text. Avoid fixed heights that cut off text. Keep visible focus outlines so a keyboard user can see the selected control. Store availability as data, not as a colour name: a later design change should not alter its meaning.

## 4. Make the behaviour understandable

The JavaScript listens for form submission, reads the search text, requests data, and updates the **DOM**: the browser's representation of page elements. It first shows a loading message, then results, no-match feedback, or an error.

Insert returned titles with `textContent`. A title containing angle brackets then stays text; it does not become HTML instructions. Client-side checks help the user, but a caller can bypass the page. The server must also enforce the 100-character query limit.

**Check yourself:** do a clear label and a safe data-insertion method solve the same problem?

**Answer:** no. The label makes the control understandable; `textContent` prevents a data string being interpreted as markup.

## 5. Trace one search through the system

```text
Type river → browser sends HTTP request
→ Python server queries SQLite
→ server returns JSON
→ JavaScript displays two records
```

**HTTP** is a request/response protocol. **JSON** is a format for data values; it is not the JavaScript program itself. The browser does not receive a database password. A server mediates the permitted database operations and returns only needed fields.

Our server runs on `127.0.0.1`, meaning your own computer. It uses fictional records and Python's built-in SQLite library. No database app, hosting account, or package installation is required. It recreates its small in-memory database for each search; it is a learning example, not a school records service.

## 6. Join two tables

`Category` contains:

| category_id | name |
|---:|---|
| 1 | Science |
| 2 | Stories |

Two of the `Book` records are:

| book_id | title | category_id | available |
|---:|---|---:|---:|
| 1 | River Patterns | 1 | 1 |
| 2 | The River Journey | 2 | 0 |

A **primary key** uniquely identifies a row. `Book.category_id` is a **foreign key** referring to a Category row. Several books can belong to one category: this is a many-to-one relationship from books to categories.

```sql
SELECT book.title, category.name, book.available
FROM book JOIN category
ON book.category_id = category.category_id
WHERE book.title LIKE ?
ORDER BY book.title;
```

The join matches the category keys. For a search pattern `%river%`, the results are:

```text
River Patterns | Science | 1
The River Journey | Stories | 0
```

The page turns 1/0 into “Available”/“On loan”. Changing the category name once changes all joined labels for that category, without editing every book.

The `?` receives a parameter rather than pasted SQL instructions. In this demo, SQLite's `LIKE` treats `%` as any sequence and `_` as any one character. Ordinary searches use title substrings; those wildcard characters deliberately keep their `LIKE` meaning. Parameters protect the SQL structure, but do not replace length or business-rule checks.

## 7. Apply universal design to a concrete change

The [seven universal-design principles](https://universaldesign.ie/about-universal-design/the-7-principles) are useful when each is tied to a real design decision:

| Principle | Library example |
|---|---|
| Equitable use | Keyboard and pointer users get the same information |
| Flexibility in use | Search a title or browse with an empty query |
| Simple and intuitive use | A clearly named “Search books” button |
| Perceptible information | Availability written in words with sufficient contrast |
| Tolerance for error | Explain a bad input and let the user correct it |
| Low physical effort | Avoid repeated typing and unnecessary clicks |
| Size and space for approach and use | Adequate target size and spacing |

**Try:** choose one principle and propose one observable improvement. “Improve accessibility” is too broad; “keep a visible outline on keyboard focus” gives you something to check.

## 8. Test the whole task

A unit test can check a query function. An integration test checks the HTTP response. A **system test** follows the complete search task in a browser. Try empty search, mixed case, no match, punctuation, unavailable books, oversized input, and server failure. Then use Tab/Enter, zoom in, and narrow the window.

For ALT1, show actual database retrieval: schema → query → response → displayed result. A static list pasted into HTML does not demonstrate that path. Work collaboratively where appropriate, but keep your own explanation of the user need, change made, test result, and limitation.

**Higher Level extension:** compare two wireframes with the same task and test criteria. Explain the trade-off using evidence, rather than only saying which looks nicer.


---

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-13-information-systems/book-01-practice">2. Practise</a>. <a href="https://tutors.dev/note/lc-cs/topic-13-information-systems/note-02-feedback">Open the answers when you have tried it</a>.

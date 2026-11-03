"""Local, read-only ALT1 example using synthetic data and Python's standard library."""
import json
import sqlite3
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


def search_books(query):
    if not isinstance(query, str) or len(query) > 100:
        raise ValueError("Search must contain at most 100 characters.")
    # shortcut: rebuild a tiny synthetic database per query; add persistence when teaching editing.
    with sqlite3.connect(":memory:") as db:
        db.execute("PRAGMA foreign_keys = ON")
        db.execute("CREATE TABLE category(category_id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        db.execute("CREATE TABLE book(book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, category_id INTEGER REFERENCES category, available INTEGER CHECK(available IN (0, 1)))")
        db.executemany("INSERT INTO category VALUES (?, ?)", [(1, "Science"), (2, "Stories")])
        db.executemany("INSERT INTO book VALUES (?, ?, ?, ?)", [
            (1, "River Patterns", 1, 1), (2, "The River Journey", 2, 0),
            (3, "A Small Computer", 1, 1), (4, "Stars & Stories", 2, 1)])
        rows = db.execute("SELECT book.title, category.name, book.available FROM book JOIN category ON book.category_id = category.category_id WHERE book.title LIKE ? ORDER BY book.title", ("%" + query + "%",)).fetchall()
    return [{"title": title, "category": category, "available": bool(available)} for title, category, available in rows]


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        request = urlsplit(self.path)
        if request.path == "/":
            self.respond(200, Path(__file__).with_name("index.html").read_bytes(), "text/html; charset=utf-8")
        elif request.path == "/api/books":
            try:
                query = parse_qs(request.query, keep_blank_values=True).get("q", [""])[0]
                body = json.dumps(search_books(query)).encode("utf-8")
                self.respond(200, body, "application/json; charset=utf-8")
            except ValueError as error:
                self.respond(400, json.dumps({"error": str(error)}).encode("utf-8"), "application/json; charset=utf-8")
        else:
            self.respond(404, b"Not found", "text/plain; charset=utf-8")


def self_check():
    assert len(search_books("")) == 4
    assert len(search_books("river")) == 2
    assert search_books("no such title") == []
    assert search_books("' OR 1=1 --") == []
    assert search_books("Stars &")[0]["available"] is True
    try:
        search_books("x" * 101)
    except ValueError:
        pass
    else:
        raise AssertionError("oversized query accepted")
    from threading import Thread
    from urllib.error import HTTPError
    from urllib.request import urlopen
    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        worker = Thread(target=server.serve_forever, daemon=True)
        worker.start()
        base = f"http://127.0.0.1:{server.server_port}"
        try:
            with urlopen(base + "/api/books?q=river") as response:
                assert len(json.load(response)) == 2
            with urlopen(base + "/") as response:
                assert b'<label for="search">' in response.read()
            for route, expected in [("/missing", 404), ("/api/books?q=" + "x" * 101, 400)]:
                try:
                    urlopen(base + route)
                except HTTPError as error:
                    assert error.code == expected
                else:
                    raise AssertionError("error status missing")
        finally:
            server.shutdown()
            worker.join()
    print("Database and HTTP checks passed.")


if __name__ == "__main__":
    if "--check" in sys.argv:
        self_check()
    else:
        print("Open http://127.0.0.1:8000 (local synthetic-data demo; Ctrl+C stops)")
        with HTTPServer(("127.0.0.1", 8000), Handler) as server:
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass

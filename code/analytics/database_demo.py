"""Optional SQLite comparison. Keep beside solution.py and readings.csv."""
import math
import sqlite3
from pathlib import Path
from solution import read_rows, summarise


def database_means(rows):
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE reading(area TEXT NOT NULL, value REAL NOT NULL)")
        db.executemany("INSERT INTO reading VALUES (?, ?)", rows)
        return db.execute("SELECT area, AVG(value) FROM reading GROUP BY area ORDER BY area").fetchall()


if __name__ == "__main__":
    assert database_means([]) == []
    assert database_means([("A", 4), ("A", 8), ("B", 0)]) == [("A", 6.0), ("B", 0.0)]
    rows, rejected = read_rows(Path(__file__).with_name("readings.csv"))
    for area, sql_mean in database_means(rows):
        python_mean = summarise([value for name, value in rows if name == area])["mean"]
        assert math.isclose(sql_mean, python_mean)
        print(f"{area}: SQL mean={sql_mean:.2f}; Python mean={python_mean:.2f}")

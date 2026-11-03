"""Original practice: clean synthetic readings and compare Python with SQLite."""
import csv
import math
import sqlite3
from pathlib import Path


def summarise(values):
    ordered = sorted(values)
    n = len(ordered)
    if not n:
        return {"count": 0, "mean": None, "median": None, "modes": []}
    middle = n // 2
    median = ordered[middle] if n % 2 else (ordered[middle - 1] + ordered[middle]) / 2
    counts = {}
    for value in ordered:
        counts[value] = counts.get(value, 0) + 1
    peak = max(counts.values())
    return {"count": n, "mean": sum(ordered) / n, "median": median,
            "modes": [value for value, count in counts.items() if count == peak]}


def read_rows(path):
    accepted, rejected = [], []
    with Path(path).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["area", "value"]:
            raise ValueError("CSV header must be exactly area,value")
        for row_number, row in enumerate(reader, 2):
            try:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError("wrong number of fields")
                value = float(row["value"])
                if not math.isfinite(value) or not 0 <= value <= 120:
                    raise ValueError("outside finite 0–120 range")
                if row["area"] not in {"A", "B"}:
                    raise ValueError("unknown area")
            except ValueError as error:
                rejected.append((row_number, str(error)))
                continue
            accepted.append((row["area"], value))
    return accepted, rejected


def self_check():
    assert summarise([])["median"] is None
    assert summarise([9, 1, 3, 3])["median"] == 3
    assert summarise([12, 4, 6, 6, 2])["mean"] == 6
    assert summarise([7])["median"] == 7
    assert summarise([1, 1, 2, 2])["modes"] == [1, 2]
    values = [3, 1, 2]
    summarise(values)
    assert values == [3, 1, 2]
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as temporary:
        path = Path(temporary) / "test.csv"
        path.write_text("area,value\nA\nA,4,extra\nB,0\nA,NaN\n", encoding="utf-8")
        accepted, rejected = read_rows(path)
        assert accepted == [("B", 0.0)] and len(rejected) == 3
        path.write_text("wrong,header\nA,4\n", encoding="utf-8")
        try:
            read_rows(path)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid header accepted")


if __name__ == "__main__":
    self_check()
    rows, rejected = read_rows(Path(__file__).with_name("readings.csv"))
    assert len(rows) == 8 and len(rejected) == 3
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE reading(area TEXT NOT NULL, value REAL NOT NULL)")
        db.executemany("INSERT INTO reading VALUES (?, ?)", rows)
        for area, mean in db.execute("SELECT area, AVG(value) FROM reading GROUP BY area ORDER BY area"):
            result = summarise([value for name, value in rows if name == area])
            assert math.isclose(result["mean"], mean)
            print(area, result)
    print("Rejected rows:", rejected)

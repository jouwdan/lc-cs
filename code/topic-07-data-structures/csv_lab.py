import csv
from pathlib import Path
from list_lab import median

scores = []
with Path(__file__).with_name("scores.csv").open(newline="", encoding="utf-8") as source:
    reader = csv.DictReader(source)
    if reader.fieldnames != ["name", "score"]:
        raise ValueError("Expected name,score headers")
    for row in reader:
        if None in row or not row.get("name", "").strip():
            raise ValueError(f"Row {reader.line_num}: invalid name or extra fields")
        try:
            score = int(row["score"])
        except (TypeError, ValueError):
            raise ValueError(f"Row {reader.line_num}: score must be an integer")
        if not 0 <= score <= 100:
            raise ValueError(f"Row {reader.line_num}: score must be from 0 to 100")
        scores.append(score)
print(scores)
print("Median:", median(scores))

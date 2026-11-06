"""data.py - load a CSV (or generate sample data) and print summary statistics.

Usage:
    python data.py                 # uses built-in sample data
    python data.py path/to/file.csv
"""
import csv
import random
import statistics
import sys
from pathlib import Path


def sample_rows(n=20, seed=42):
    rng = random.Random(seed)
    return [
        {"id": str(i), "value": f"{rng.uniform(10, 100):.2f}", "category": rng.choice("ABC")}
        for i in range(1, n + 1)
    ]


def load_csv(path):
    with Path(path).open(newline="") as f:
        return list(csv.DictReader(f))


def numeric_columns(rows):
    cols = []
    for col in rows[0]:
        try:
            [float(r[col]) for r in rows]
            cols.append(col)
        except (ValueError, TypeError):
            pass
    return cols


def summarize(rows):
    if not rows:
        print("No rows found.")
        return
    print(f"Rows: {len(rows)}  Columns: {', '.join(rows[0])}\n")
    for col in numeric_columns(rows):
        vals = [float(r[col]) for r in rows]
        print(
            f"{col:>10}: min={min(vals):.2f} max={max(vals):.2f} "
            f"mean={statistics.mean(vals):.2f} median={statistics.median(vals):.2f}"
        )


def main():
    rows = load_csv(sys.argv[1]) if len(sys.argv) > 1 else sample_rows()
    summarize(rows)


if __name__ == "__main__":
    main()

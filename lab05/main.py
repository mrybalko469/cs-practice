"""lab05 — читает имя журнала из ввода, печатает сводку и пишет report.txt."""

import os

from logstats import count_levels, top_errors, format_report


def main():
    name = input().strip()

    # Два прохода по файлу дешевле, чем держать весь журнал в памяти.
    with open(name, encoding="utf-8") as log:
        counts = count_levels(log)
    with open(name, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    report = format_report(counts, errors)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "report.txt"), "w", encoding="utf-8") as out:
        out.write(report)


if __name__ == "__main__":
    main()

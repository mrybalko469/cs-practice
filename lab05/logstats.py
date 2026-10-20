"""lab05 — обработка журнала сервиса: построчное чтение, подсчёты, отчёт."""

LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line):
    """Строка «время уровень сообщение» -> словарь.

    Негодная строка (без уровня или с незнакомым уровнем) -> ValueError.
    Сообщение может содержать пробелы, поэтому делим не больше чем на 3 части.
    """
    parts = line.strip().split(None, 2)
    if len(parts) < 2:
        raise ValueError("нет уровня: " + line)
    time, level = parts[0], parts[1]
    if level not in LEVELS:
        raise ValueError("незнакомый уровень: " + level)
    message = parts[2] if len(parts) == 3 else ""
    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    """Сколько строк каждого уровня. Испорченные — под ключом BROKEN.

    Пустые строки пропускаются. lines — список строк или сам открытый файл.
    """
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    """n самых частых сообщений уровня ERROR.

    Возвращает пары [сообщение, сколько раз]; при равенстве — по алфавиту.
    """
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            freq[msg] = freq.get(msg, 0) + 1
    ordered = sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[msg, count] for msg, count in ordered[:n]]


def format_report(counts, errors):
    """Текст отчёта по готовым подсчётам. Уровни — по алфавиту."""
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, count in errors:
        lines.append(f"- {msg} — {count}")
    return "\n".join(lines) + "\n"

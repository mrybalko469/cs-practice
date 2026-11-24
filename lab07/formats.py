# lab07 · Рыбалко М.Р.
"""lab07 · Форматы хранения данных: CSV, простой YAML и JSON."""

import json


def csv_to_records(text: str) -> list[dict]:
    """Разбирает CSV с заголовком в список словарей. Значения остаются строками."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = [name.strip() for name in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [value.strip() for value in line.split(",")]
        records.append(dict(zip(header, values)))
    return records


def _convert(value: str):
    """Приводит строковое значение YAML к числу, логическому значению или строке."""
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #."""
    result = {}
    current_list = None
    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("-"):
            if current_list is not None:
                current_list.append(_convert(line[1:].strip()))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value:
            result[key] = _convert(value)
            current_list = None
        else:
            current_list = []
            result[key] = current_list
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника по значению ключа key.

    Поля самой записи важнее полей справочника.
    """
    merged = []
    for row in rows:
        info = extra.get(row.get(key))
        if info is None and row.get(key) is not None:
            info = extra.get(str(row.get(key)))
        if info:
            merged.append({**info, **row})
        else:
            merged.append(dict(row))
    return merged


def records_to_json(records: list[dict]) -> str:
    """Список словарей в JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)

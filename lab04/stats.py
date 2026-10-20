import math


def parse_record(line: str) -> dict:
    parts = [p.strip() for p in line.split(";")]
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(parts)}: {line!r}")
    city, raw_temp, date = parts
    if not city or not date:
        raise ValueError(f"пустой город или дата: {line!r}")
    try:
        temperature = float(raw_temp.replace(",", "."))
    except ValueError:
        raise ValueError(f"температура не число: {raw_temp!r}") from None
    if not math.isfinite(temperature):
        raise ValueError(f"температура не число: {raw_temp!r}")
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

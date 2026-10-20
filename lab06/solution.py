"""lab06 — файловая система: разбор путей и перевод размеров в единицы."""

from pathlib import PurePosixPath


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in paths:
        ext = PurePosixPath(path).suffix.lstrip(".").lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    if idx == 0:
        return f"{int(n_bytes)} {units[0]}"
    return f"{size:.1f} {units[idx]}"

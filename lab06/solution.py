"""lab06 — файловая система: разбор путей и перевод размеров в единицы."""

from pathlib import PurePosixPath


def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Сколько файлов каждого расширения.

    Расширение — то, что после последней точки в имени файла, в нижнем
    регистре и без точки. У файла без расширения (Makefile, .gitignore)
    ключ — пустая строка "".
    """
    counts: dict[str, int] = {}
    for path in paths:
        ext = PurePosixPath(path).suffix.lstrip(".").lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшей вложенностью.

    Вложенность считается по числу разделителей "/" в пути. При равенстве
    возвращается первый по алфавиту. Для пустого списка — пустая строка.
    """
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    """Размер в удобных единицах: 1536 -> «1.5 КБ».

    Единицы Б, КБ, МБ, ГБ, ТБ — каждая следующая в 1024 раза больше.
    Байты выводятся целым числом, остальные — с одним знаком после точки.
    """
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    if idx == 0:
        return f"{int(n_bytes)} {units[0]}"
    return f"{size:.1f} {units[idx]}"

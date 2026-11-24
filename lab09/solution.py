import numpy as np


def make_hours() -> list[int]:
    """Создаёт вектор часов: от 0 до 21 с шагом 3."""
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    """Возвращает третий, последний, средний срез, каждый второй и развёрнутый вектор."""
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }



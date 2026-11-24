import numpy as np

# Задание 1. Создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

# Задание 2. Индексы и срезы в векторе
print("\nЗадание 2")
print("третий элемент:", hours[2])
print("последний элемент:", hours[-1])
print("индексы 2–5:", hours[2:6])
print("каждый второй:", hours[::2])
print("в обратном порядке:", hours[::-1])

# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("shape:", temperatures.shape, "ndim:", temperatures.ndim, "size:", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[0:2, 1:3]
print("центральный фрагмент 2×2:\n", center, "shape:", center.shape)

# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
fragments = {
    "первые три строки": matrix[:3],
    "последние две строки": matrix[-2:],
    "первые два столбца": matrix[:, :2],
    "строки 1–3, столбцы 2–4": matrix[1:4, 2:5],
    "правый нижний блок 2×2": matrix[-2:, -2:],
}
for name, fragment in fragments.items():
    print(name + ":\n", fragment)
    print("shape:", fragment.shape)

# Задание 5. Изменение массива с помощью срезов
print("\nЗадание 5")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)

# .copy() нужна, потому что срез и простое присваивание (changed = hours)
# не создают новый массив, а ссылаются на те же данные. Без копии замены
# испортили бы исходный hours. .copy() создаёт независимый массив.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

# Задание 6. Изменение формы
print("\nЗадание 6")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12 — ровно столько элементов
# в numbers. reshape(5, 3) требует 5 * 3 = 15 элементов, а их только 12,
# поэтому NumPy выдаст ValueError: cannot reshape array of size 12 into shape (5,3).

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return None
    return a / b


a = int(input())
b = int(input())
d = input()
if d == "+":
    print(add(a, b))
elif d == "-":
    print(sub(a, b))
elif d == "*":
    print(mul(a, b))
elif d == "/":
    result = div(a, b)
    if result is None:
        print("Ошибка: деление на ноль")
    else:
        print(result)

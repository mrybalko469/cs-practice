def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
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
    print(div(a, b))

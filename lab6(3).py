import random
import math

def f1(x1, x2):
    return float(x1) + float(x2)


def f2(x1, x2):
    return x1 - x2


def f3(x1, x2):
    return x1 * x2


def f4(x1, x2):
    return x1 / x2


def f5(x1, x2):
    return pow(x1, x2)


def f6(x):
    return abs(x)


def f7(x1, x2):
    return random.uniform(x1, x2)


def f8(x):
    return math.factorial(x)


def f9(x):
    return math.acos(x)


print("""
    1.Сумма   
    2.Вычитание   
    3.Умножение   
    4.Деление   
    5.Степень   
    6.Модуль   
    7.Рандом   
    8.Факториал   
    9.Аркосинус   
    """)
op = input("Выберите операцию: ")
if op == '1':
    x1 = float(input("Первое число: "))
    x2 = float(input("Второе число: "))
    print(x1, " + ", x2, " = ", f1(x1, x2))
elif op == '2':
    x1 = float(input("Уменьшаемое: "))
    x2 = float(input("Вычитаемое: "))
    print(x1, " - ", x2, " = ", f2(x1, x2))
elif op == '3':
    x1 = float(input("Первый множитель: "))
    x2 = float(input("Второй множитель: "))
    print(x1, " * ", x2, " = ", f3(x1, x2))
elif op == '4':
    x1 = float(input("Делимое: "))
    x2 = float(input("Делитель: "))
    print(x1, " / ", x2, " = ", f4(x1, x2))
elif op == '5':
    x1 = float(input("Введите число: "))
    x2 = float(input("Введите степень: "))
    print(x1, "^", x2, " = ", f5(x1, x2))
elif op == '6':
    x = float(input("Введите число: "))
    print("|", x, "| "" = ", f6(x))
elif op == '7':
    x1 = float(input("Введите левую границу: "))
    x2 = float(input("Введите правую границу: "))
    print("Рандомное число [", x1, ";", x2, "] = ", f7(x1, x2))
elif op == '8':
    x = input("Введите целое число: ")
    x = int(x)
    print(x, "! = ", f8(x))
elif op == '9':
    x = input("Введите число от -1 до 1: ")
    x = float(x)
    print("Аркосинус(", x, ") = ", f9(x), "радиан")

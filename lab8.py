import lab8import


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
    print(x1, " + ", x2, " = ", lab8import.f1(x1, x2))
elif op == '2':
    x1 = float(input("Уменьшаемое: "))
    x2 = float(input("Вычитаемое: "))
    print(x1, " - ", x2, " = ", lab8import.f2(x1, x2))
elif op == '3':
    x1 = float(input("Первый множитель: "))
    x2 = float(input("Второй множитель: "))
    print(x1, " * ", x2, " = ", lab8import.f3(x1, x2))
elif op == '4':
    x1 = float(input("Делимое: "))
    x2 = float(input("Делитель: "))
    print(x1, " / ", x2, " = ", lab8import.f4(x1, x2))
elif op == '5':
    x1 = float(input("Введите число: "))
    x2 = float(input("Введите степень: "))
    print(x1, "^", x2, " = ", lab8import.f5(x1, x2))
elif op == '6':
    x = float(input("Введите число: "))
    print("|", x, "| "" = ", lab8import.f6(x))
elif op == '7':
    x1 = float(input("Введите левую границу: "))
    x2 = float(input("Введите правую границу: "))
    print("Рандомное число [", x1, ";", x2, "] = ", lab8import.f7(x1, x2))
elif op == '8':
    x = input("Введите целое число: ")
    x = int(x)
    print(x, "! = ", lab8import.f8(x))
elif op == '9':
    x = input("Введите число от -1 до 1: ")
    x = float(x)
    print("Аркосинус(", x, ") = ", lab8import.f9(x), "радиан")
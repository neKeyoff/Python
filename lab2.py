string = input("Введите текст\n")
i = int(0)
l = int(len(string))
c = 'с'
string2 = "\n"

for i in range(0, l - 1):
    if i != 2:
        string2 = string2 + string[i]
print(string2)
if c in string:
    print("В тексте есть буева С")
else:
    print("В тексте нет буквы С")
print("Длина строки: ", l)

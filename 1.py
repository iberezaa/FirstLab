a = int(input("Введите первое число число "))
b = int(input("Введите второе число"))
c = int(input ("Введите третье число"))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = int(((- b) + (D ** 0.5)) / (2 * a))
    x2 = int(((- b) - (D ** 0.5)) / (2 * a))
    print(x1)
    print(x2)
elif D == 0:
    x3 = (-b / (2 * a))
    print(x3)
else:
    print("Нет решений")
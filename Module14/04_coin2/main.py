def money():
    money_pit = (coordinat_X ** 2 + coordinat_Y ** 2) ** 0.5
    if money_pit <= radius:
        print("\nМонетка где-то рядом")
    else:
        print("\nМонетки в области нет")


coordinat_X = float(input('Введите координату Х: '))
coordinat_Y = float(input('Введите координату Y: '))
radius = float(input('Введите радиус окружности: '))

money()

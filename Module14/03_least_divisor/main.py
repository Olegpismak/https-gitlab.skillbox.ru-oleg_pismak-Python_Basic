def divider():
    number = int(input('Введите число: '))
    i = 2
    while number % i != 0:
        i += 1
    print('Наименьший делитель, отличный от единицы:', i)

divider()

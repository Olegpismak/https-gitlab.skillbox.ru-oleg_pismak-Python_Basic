def suma_number(a):
    return sum(map(int, list(a)))


def count_number(a):
    return len(a)


def differ(a, b):
    return a - b


number = input('Введите число: ')

print('Сумма чисел:', suma_number(number))

print('Количество цифр в числе:', count_number(number))

print('Разность суммы и количества цифр:', differ(suma_number(number), count_number(number)))

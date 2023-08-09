def suma_number(a):

   return sum(map(int, list(a)))

def count_number(a):

   return len(a)

def differ(a, b):

   return a - b

n = input('Введите число: ')

print('Сумма чисел:', suma_number(n))

print('Количество цифр в числе:', count_number(n))

print('Разность суммы и количества цифр:', differ(suma_number(n), count_number(n)))
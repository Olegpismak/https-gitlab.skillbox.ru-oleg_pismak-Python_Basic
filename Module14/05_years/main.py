years = int(input("Введите первый год: "))
years2 = int(input("Введите второй год: "))
print("Годы от,", years, "до", years2, " с тремя одинаковыми цифрами:")
for i in range(years, years2+1):
    first_num, second_num, third_num, four_num = i // 1000, i // 100 % 10, i // 10 % 10, i % 10
    if ((first_num == second_num == third_num)
            or (second_num == third_num == four_num)
            or (third_num == four_num == first_num)
            or (first_num == second_num == four_num)):
        print(first_num * 1000 + second_num * 100 + third_num * 10 + four_num)

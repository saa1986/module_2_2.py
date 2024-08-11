number_1 = int(input("Введите 1-е число :"))
number_2 = int(input("Введите 2-е число :"))
number_3 = int(input("Введите 3-е число :"))
if number_1 == number_2 and number_2 == number_3:
     print('3')# Если все числа равны между собой, то вывести 3
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
     print('2')# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
elif number_1 != number_2 or number_1 != number_3 or number_2 != number_3:
    print('0')
# Если равных чисел среди 3-х вообще нет, то вывести 0
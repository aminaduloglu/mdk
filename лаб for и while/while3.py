#Задание 3. Задача «Количество нулей».
#Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
a = int(input())
n = 0
i = 0
while i < a:
    x = int(input())
    if x == 0:
        n += 1
    i += 1
print (n)
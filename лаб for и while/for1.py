#Задание 1. Задача «Ряд - 2». Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания,
#если A < B, или в порядке убывания в противном случае.
a = int(input())
b = int(input())
if a<b:
    for a in range(a, b+1):
          print(a, end=' ')
else:
    for a in range(b, a+1):
          print(a, end=' ')
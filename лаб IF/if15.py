# If15. Даны три числа. Найти сумму двух наибольших из них.
a = int(input())
b = int(input())
c = int(input())
if a <= c and a <= b:
    print (c + b)
elif b <= c and b <= a:
    print (c + a)
elif c <= b and c <= a:
    print (a + b)
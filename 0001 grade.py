a = int(input('enter point 1 : '))
while a < 0 or a > 30:
    a = int(input('wrong. enter point 1 agin : '))

b = int(input('enter point 2 : '))
while b < 0 or b > 30:
    b = int(input('wrong. enter point 1 agin : '))

c = int(input('enter point 3 : '))
while c < 0 or c > 40:
    c = int(input('wrong. enter point 1 agin : '))

point = a +b + c

if point >= 80:
    print('a')
elif point >= 75:
    print('b+')
elif point >= 70:
    print('b')
elif point >= 65:
    print('c+')
elif point >= 60:
    print('c')
elif point >= 55:
    print('d+')
elif point >= 50:
    print('d')
else:
    print('f')

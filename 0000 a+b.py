a = int(input('enter number : '))

while a < 0 or a > 10 ** 9:
    a = int(input('wrong. enter number agin : '))

b = int(input('enter number : '))

while b < 0 or b > 10 ** 9:
    b = int(input('wrong. enter number agin : '))

c = a + b
print(c)
num = [int(n) for n in input('number : ').split()]
num.sort()

char = [str(n) for n in input('char : ')]
# print(num)
a = num[0]
b = num[1]
c = num[2]

for i in range(len(char)):
    print(eval(char[i]), end=' ')


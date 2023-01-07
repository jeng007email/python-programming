m = int(input('row : '))
# n = int(input('column : '))
data_1 = []
data_2 = []

for i in range(m):
    x = [int(y) for y in input(f'number : ').split()]
    data_1.append(x)
for i in range(m):
    x = [int(y) for y in input(f'number : ').split()]
    data_2.append(x)


print(f'data 1 = {data_1}')
print(f'data 2 = {data_2}')

for i in range(len(data_1)):
    for j in range(len(data_1[i])):
        result = data_1[i][j] + data_2[i][j]
        print(result, end=' ')
    print('')
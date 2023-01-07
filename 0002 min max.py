data = 1
l_data = []
while data != 0:
    data = int(input('enter number : '))
    l_data.append(data)

l_data.pop()
print(min(l_data))
print(max(l_data))

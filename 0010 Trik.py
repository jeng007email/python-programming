glass = ['ball', '', '']


def swap_ball(i, x, y):
    ball1 = i[x]
    ball2 = i[y]
    i[x] = ball2
    i[y] = ball1
    return i


text = [str(n) for n in input('text : ')]

for j in range(len(text)):
    if text[j].lower() == 'a':
        glass = swap_ball(glass, 0, 1)
    elif text[j].lower() == 'b':
        glass = swap_ball(glass, 1, 2)
    else:
        glass = swap_ball(glass, 0, 2)

print(glass)
ball = glass.index('ball')
print(ball + 1)

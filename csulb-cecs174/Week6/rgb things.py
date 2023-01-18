r = int(input())
b = int(input())
g = int(input())


def rgb(lesserVal, otherVal):
    return lesserVal - otherVal


if r < b and r < g:
    r = rgb(r, r)
    b = rgb(b, r)
    g = rgb(g, r)
    print(f'{r} {b} {g}')
elif b > g:
    r = rgb(r, b)
    b = rgb(b, b)
    g = rgb(g, b)
    print(f'{r} {b} {g}')
else:
    r = rgb(r, g)
    b = rgb(b, g)
    g = rgb(g, g)
    print(f'{r} {b} {g}')
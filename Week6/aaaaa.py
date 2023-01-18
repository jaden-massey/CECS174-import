x = int(input())
y = int(input())

for i in range(x, y, 5):
    if y > x:
        print("Second integer can't be less than the first.")
        break
    else:
        print(i, end=' ')
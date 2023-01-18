'''for h in range(24):
    for m in range (60):
        for s in range(60):
            print(f'{h}:{m}:{s}')'''

print('Done')
print(1,2,3)

#separates outputs with the string provided
print(1,2,3, sep='*')
print('At a new line')

#ends the output with the specified string
print(1,2,3, end='*')
print('At the same line')

# will show all values in range, starting at 0 unless otherwise specified
for i in range(5):
    print(i, end=' ')
print()

for i in range (9,15):
    print(i, end=' ')
print()

# will show values incremementing by 3, in the range, non-inclusive on the upper bound
for i in range (9, 25, 3):
    print(i, end=' ')
print()

# lower bound cannot be greater that upper bound unless specified
for i in range (19, 15, -1):
    print(i, end=' ')
print()

### break/continue

print()

# continue will skip the remainder of the iteration, but will keep looping afterwards
for i in range (45, 19, -1):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

# break will stop the loop entirely
for i in range (45, 19, -1):
    if i % 2 == 0:
        break
    print(i, end=' ')
print()
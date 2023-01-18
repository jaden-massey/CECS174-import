'''
i = 0
count = 0
while i < 30:
    x = input()
    if 'a' in x[1:]:
        count += 1
    i += 1

print(count)

'''
'''
f = open('mobysmall.txt')

f.close()
'''
'''
class Widget:
    def __init__(self, v = 40):
        if v >= 40:
            self.value = v
        else:
            self.value = 0
    def get(self):
        return self.value
    def bump(self):
        if self.value < 50:
            self.value += 1

def main():
    w1 = Widget()
    w2 = Widget(5)

    w1.bump()
    w2.bump()

    for i in range(40):
        w1.bump()
        w2.bump()

    print(w1.get())
    print(w2.get())

main()

def all_in_range(x, y, values):
    for i in range(x,y+1):
        if len(values) == 0:
            print('T')
            return True
        if len(values) == 1:
            if x < values[0]:
                print('F')
                return False
            else:
                print('T')
                return True
        if i < values[0]:
            print('F')
            return False
        elif i > values[1]:
            print('F')
            return False
        else:
            print('T')
            return True

all_in_range(0, 10, [])'''

print('Hello world')


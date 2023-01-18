class Monster:
    count = 0
    def __init__(self):
        print('I am the constructor')
        self.__name = 'Nothing'
        self.rank = 0
        self.__power = 5
        self.count += 1

    def setName(self, nam):
        self.__name = nam
    def getName(self):
        return self.__name

    def hit(self):
        self.__power += 1

m1 = Monster()
print(f'The rank of {m1.rank}')
print(m1.count)
m1.__name = "Casper"
print(f'The rank of {m1.__name}')
print('????', m1.getName())
m2 = Monster()
print(m2.count)




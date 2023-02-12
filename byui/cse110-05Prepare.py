numeroUno = int(input('What is the first number? '))
numeroDos = int(input('What is the second number? '))

if numeroUno > numeroDos:
    print('The first number is greater')
else:
    print('The first number is not greater')

if numeroUno == numeroDos:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if numeroUno < numeroDos:
    print('The second number is greater')
else:
    print('The second number is not greater')

myFavAnimal = 'turtle'

favAnimal = input('\nWhat is your favorite animal? ')

favAnimal = favAnimal.strip()
favAnimal = favAnimal.lower()

if favAnimal == myFavAnimal:
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')


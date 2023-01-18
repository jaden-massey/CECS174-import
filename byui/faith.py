import time


class User:
    def __init__(self):
        self.__favColor = ''

    def set_fav_color(self, color):
        self.__favColor = color

    def get_fav_color(self):
        return self.__favColor


user1 = User()
color = input('Please type your favorite color: ')
user1.set_fav_color(color)

print(f'Your favorite color is {user1.get_fav_color()}, that\'s pretty cool!')

similarColors = ['blue', 'green', 'cyan', 'teal']

if color in similarColors:
    print('\nYour favorite color is similar to the dev!')
elif color == 'dark cyan':
    print('\nYou share the same favorite color as the dev!')

time.sleep(5)

print('\n...')

time.sleep(5)

print('\nSince you\'re still here, this developer\'s favorite color is dark cyan.')


'''Though a bit informal, I have taken this class at another college, as is visible with my code, 
and was advised to ask if you could move me to the next level of this class, as the advisors 
were unable to do so when I was signing up for this class online'''
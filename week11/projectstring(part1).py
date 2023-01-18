# define functions


def calc_length(string):
    print('\nYour name is ' + str(len(string)) + ' characters long.')


def last_char(string):
    print('\nThe last character is: ' + string[len(string)-1])


def find_e(string):
    output = "\nThe first 'e' is at position "

    if string.find('e') == -1:
        output += '0.'
    else:
        output += str(string.find('e') + 1) + '.'

    print(output)


def count_words(string):
    output = string.split()
    print('\nYour name has ' + str(len(output)) + ' words.')


def first_word(string):
    output = string.split()
    print('\nYour first name is ' + output[0] + '.')


def count_vowels(string):
    count = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    print('\nYour name contains ' + str(count) + ' vowels.')


def upper_vowels(string):
    string = string.lower()

    string = string.replace('a', 'A')
    string = string.replace('e', 'E')
    string = string.replace('i', 'I')
    string = string.replace('o', 'O')
    string = string.replace('u', 'U')

    print('\nYour name with uppercase vowels is: ' + string)


def surround(string):
    string = list(string)

    string.insert(0, '+'*25 + '~'*25)
    string.append('~'*25 + '+'*25)

    print('\n' + ''.join(string))


def split(string):
    string = list(string)

    string.insert(int(len(string)/2), '*'*70)
    print('\n' + ''.join(string))


def main():
    user_string = input('Please enter your name: ')

    calc_length(user_string)
    last_char(user_string)
    find_e(user_string)
    count_words(user_string)
    first_word(user_string)
    count_vowels(user_string)
    upper_vowels(user_string)
    surround(user_string)
    split(user_string)


main()

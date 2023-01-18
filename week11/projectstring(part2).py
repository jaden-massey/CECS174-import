with open("favText.txt", 'r') as file:
    favText = file.read()

# test cases
anagram_check_1_1 = 'fried'

avoids_forbidden_1 = 'pie'
avoids_forbidden_2 = 'k'

forbidden_check_1 = 'a'
forbidden_check_2 = 'qwerty'
permitted_check_1 = 'kco'
permitted_check_2 = 'elloh'


# general functions
def find(string, char, start=0, print_func=True):
    cut_string = string[start:]  # used to chop the string when the starting point is changed
    char_loc = cut_string.find(char)
    char_loc_og = len(string) - len(cut_string) + char_loc

    if print_func:
        if cut_string == string:
            print("The first instance of the character '" + char + "' appears at: " + str(char_loc))
        else:
            print('From the specified starting point the character can be found at position: ' + str(char_loc))
            print('In reference to the original string, this character can be found at position: ' + str(char_loc_og))
    else:
        return char_loc


def find_all(string, char='e', print_func=True):
    found = 0
    count = 0
    positions = []

    for i in string:
        if i == char:
            found += 1
            positions.append(str(count))  # not necessary but used to keep track of the position of each time it's found
        count += 1

    if print_func:
        output = str(found)
        if found == 0:
            output = 'No ' + char + ' were found in the text'
        elif found == 1:
            output += ' ' + char + ' was found in the text at.'
        else:
            output += ' ' + char + "'s" + ' were found in the text.'
        print(output)
    else:
        return found

    string_alpha = []
    for i in string:
        if 97 <= ord(i) <= 122:
            string_alpha.append(i)
        elif 65 <= ord(i) <= 90:
            string_alpha.append(i)
    string_alpha = ''.join(string_alpha)
    x = (found / len(string_alpha)) * 100
    print('Your text contains ' + str(len(string_alpha)) + ' alphabetic characters, of which ' + str(found) +
          f'({x:.1f}%)' + ' were the letter ' + char)


def is_sorted(string):
    string.lower()
    split_string = string.split()
    not_sorted = 0
    count = 0
    while count + 1 < len(split_string) and not_sorted == 0:
        if split_string[count] > split_string[count + 1]:
            not_sorted += 1
        else:
            count += 1

    if not_sorted == 0:
        print("The string is sorted in ascending order")
        return True
    else:
        print("The string is not in ascending order")
        return False


def is_anagram(string1, string2):
    fstring1 = string1.lower()
    fstring2 = string2.lower()

    if len(string1) != len(string2):
        print('The strings are not anagrams')
        return False

    fstring1_list = list(fstring1)

    for i in fstring1_list:
        if i not in fstring2:
            print('The strings are not anagrams')
            return False

    print('The strings are anagrams')
    return True


def has_duplicates(string, print_func=True):
    duplicates = 0
    count = 0
    fstring = sorted(string)
    for i in fstring:
        if not (count+1 == len(fstring)):
            if i == fstring[count+1]:
                duplicates += 1
        count += 1

    if print_func:
        output = "The string contains "
        if duplicates == 0:
            output += 'no duplicate characters'
            print(output)
        else:
            output += str(duplicates) + ' duplicate character'
            if duplicates == 1:
                print(output)
            else:
                output += 's'
                print(output)
        output += '.'
    else:
        if duplicates == 0:
            return False
        else:
            return True


def remove_duplicates(string, return_func=False):
    non_duplicates = []
    for i in string:
        if i not in non_duplicates:
            non_duplicates.append(i)
    output = ''.join(non_duplicates)
    if return_func:
        return output
    else:
        print(output)


# string based functions
def mirror(string=favText):
    print(string)
    print('\nMirrored: ')
    rev_string = string[::-1]
    print('\n' + rev_string)


def remove(string=favText, char='e'):
    rem_string = string.replace(char, '')
    print(rem_string)


def no_char(string=favText, char='e'):
    if find_all(string, char, False) == 0:
        print('True, the text does not contain the character: ' + char)
        return True
    else:
        print('False, The text does contain the character: ' + char)
        return False


# word based functions
def avoids(word, forbidden):
    for i in forbidden:
        if i in word:
            print('The word is invalid as it uses a forbidden character')
            return False
    print('The word does not make use of any of the forbidden characters')
    return True


def uses_only(word, permitted):
    remove_duplicates(permitted, True)

    for i in permitted:
        if i in word:
            word = word.replace(i, '')
    if len(word) > 0:
        print('The word uses characters other than those permitted')
        return False
    else:
        print('The word only uses the permitted letters')
        return True


def uses_all(word, permitted):
    count = 0
    for i in permitted:
        if i in word:
            count += 1
        else:
            print('The word does not make use of the letter ' + permitted[count])
            return False
    print('The word makes use of all of the permitted letters at least once')
    return True


def is_abecedarian(word):
    word_formatted = remove_duplicates(word, True)
    word_lower = word_formatted.lower()
    split_word = list(word_lower)
    not_abecedarian = 0
    count = 0
    while count + 1 < len(split_word) and not_abecedarian == 0:
        if split_word[count] > split_word[count + 1]:
            not_abecedarian += 1
        else:
            count += 1

    if not_abecedarian == 0:
        print("The text is abecedarian")
        return True
    else:
        print("The text is not abecedarian")
        return False


def validate_input(check):
    try:
        int(check)
        return True
    except ValueError:
        return False


def main():
    mirror(favText)

    rem_char = input('\nPlease enter the character you would like removed form the string: ')
    remove(favText, rem_char)

    find_char = input('\nPlease enter the character you would like found: ')
    find_start = input('Please enter where you would like to start searching, press enter to skip: ')
    while True:
        if find_start == '':
            find(favText, find_char)
            break
        elif validate_input(find_start):
            find_start = int(find_start)
            find(favText, find_char, find_start)
            break
        else:
            find_start = input(
                '\nInvalid entry: [Non-Integer Value] Please enter where you would like to start searching, '
                'press enter to skip: ')

    find_all_char = input('\nPlease enter the character you would like counted: ')
    find_all(favText, find_all_char)

    no_char_char = input('\nEnter the character you would like to verify there are none of: ')
    no_char(favText, no_char_char)

    print()
    is_sorted(favText)

    print()
    is_anagram(anagram_check_1_1, favText)

    print()
    is_abecedarian(favText)

    print()
    has_duplicates(favText)

    print()
    avoids(favText, avoids_forbidden_1)

    print()
    remove_duplicates(favText)

    print()
    uses_only(favText, permitted_check_1)
    uses_only(favText, permitted_check_2)

    print()
    uses_all(favText, permitted_check_1)
    uses_all(favText, permitted_check_2)


main()

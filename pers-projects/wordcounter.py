flag = True
word_count = 0
while flag:
    text_input = input('Enter the string you want the word count for:\n')

    word_count += len(text_input.split())

    print(f'\nWord count: {word_count}')

    question = input('\nDo you need to add/sub from the total word count with a known number?\n')
    question = question.lower()
    if question == 'y' or question == 'yes':
        amt_change = int(input('How many words do you want to add/sub:\n'))
        word_count += amt_change
        print(f'Updated word count: {word_count}')

    question2 = input('\nWould you like to continue adding words to the total count with more text?\n')
    question2 = question2.lower()
    if question2 == 'n' or question2 == 'no':
        flag = False
    
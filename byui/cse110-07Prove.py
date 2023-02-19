print('\nWelcome to the word guessing game!\n')

secret_word = "mosiah"
print('Your hint is: ' + len(secret_word)*'_ ')

guess = input("What is your guess? ")

count = 1
while guess != secret_word:
    print('Your hint is:', end=' ')

    for i in range(0, len(guess)):
        if i < len(secret_word) and guess[i] == secret_word[i]:
            print(guess[i].upper(), end=' ')

        elif secret_word.find(guess[i]) != -1:
            print(guess[i], end=' ')

        else:
            print("_", end=' ')
            
    count += 1

    print()
    guess = input('What is your guess? ')

print('Congratulations! You guessed it!')
print(f'It took you {count} guesses.')
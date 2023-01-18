# extra credit
# number of quizzes is unknown --> (cant use for loop, or a count based while loop)
# quiz input must be between 0 and 10 --> while loop with if statement to check
# if input == 999, halt --> whole thing must be a sentinel loop

sum = 0
totalQuizzes = 0
enteringGrades = True

while enteringGrades:

    quizGrade = int(input("Please enter a grade: "))

    if quizGrade == 999:
        print('Done!')
        enteringGrades = False
        break
    elif quizGrade < 0 or quizGrade > 10:
        print('Invalid entry: Please enter a grade between 0 and 10')
        continue
    else:
        print(f'Grade of {quizGrade} recorded, continuing...')
        sum += quizGrade
        totalQuizzes += 1

avg = (sum / totalQuizzes) / 10
print("The average grade is {:.0%}".format(avg))

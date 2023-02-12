def get_letter(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


def get_sign(grade):
    if letterGrade == 'F':
        return ''
    
    gradeOnes = round(grade % 10, 2)
    if gradeOnes >= 7 and letterGrade != 'A':
        return '+'
    elif gradeOnes < 3 and grade != 100:
        return '-'
    else:
        return ''


grade = input('What is your grade as a percentage? ')
gradeF =  float(grade.replace('%', ''))

letterGrade = get_letter(gradeF)
finalGrade = letterGrade + get_sign(gradeF)

print(f'\nWith a grade of {grade}, your letter grade is a {finalGrade}')
if gradeF >= 70:
    print('You passed, nice work!')
else:
    print('You failed, better luck next time!')
import time


#FIXME -- create storyline, all logic is complete
#FIXME -- double check if statements and loops to ensure everything is nested properly and that there are no logical errors
#FIXME -- add all print statements


def story_game():
    flag_main = True
    while flag_main:
        print('Welcome to our little game...')
        q1 = format(input('question1'))
        wait()

        if q1 == '1option1':
            flag_main = False
            print('1response1')

            sub_flag1 = True
            while sub_flag1:
                q2_1 = format(input('2question1'))
                wait()

                if q2_1 == '2option1':
                    sub_flag1 = False
                    print('2reponse1')

                    while True:
                        q3_1 = format(input('3_1question1'))
                        wait()
                        
                        if q3_1 == '3option1':
                            print('3reponse1')
                            return '\n'*5 + 'Game Over - You Win'

                        elif q3_1 == '3option2':
                            print('3reponse2')
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_1 == '3option3':
                            print('3reponse3')
                            return '\n'*5 + 'Game Over - You Lose'
                        
                        else:
                            print('Invalid Choice, Try Again')

                elif q2_1 == '2option2':
                    sub_flag1 = False
                    print('2reponse2')
                    
                    sub_flag2 = True
                    while sub_flag2: 

                        q3_2 = format(input('3_1question2'))
                        wait()

                        if q3_2 == '3option1':
                            print('3response1')
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_2 == '3option2':
                            print('3response2')
                            return '\n'*5 + 'Game Over - You Lose'

                        else:
                            print('Invalid Choice, Try Again')

                else:
                    print('Invalid Choice, Try Again')

        elif q1 == '1option2': 
            flag_main = False
            print('1reponse2')

            sub_flag1 = True
            while sub_flag1:
                q2_2 = format(input('2question2'))
                wait()

                if q2_2 == '2option1':
                    print('2reponse2')
                    sub_flag1 = False
                    while True: 

                        q3_3 = format(input('3_2question1'))
                        wait()

                        if q3_3 == '3option1':
                            print('3reponse1')
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_3 == '3option2':
                            print('3response2')
                            return '\n'*5 + 'Game Over - You Lose'
                        
                        else:
                            print('Invalid Choice, Try Again')

                elif q2_2 == '2option2':
                    print('2reponse2')
                    sub_flag1 = False

                    sub_flag2 = True
                    while sub_flag2: 

                        q3_4 = format(input('3_2question2'))
                        wait()

                        if q3_4 == '3option1':
                            print('3response1')
                            sub_flag2 = False
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_4 == '3option2':
                            print('3reponse2')
                            sub_flag2 = False
                            return '\n'*5 + 'Game Over - You Lose'

                        
                        else:
                            print('Invalid Choice, Try Again')

                else:
                    print('Invalid Choice, Try Again')

        else:
            print('Invalid Choice, Try Again')



def format(input):
    x = str(input)
    y = x.strip()
    z = y.lower()
    return z


def wait():
    for i in range(3):
        time.sleep(1)
        print()


print(story_game())
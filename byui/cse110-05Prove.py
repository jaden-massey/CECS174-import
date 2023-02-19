import time


def story_game():
    flag_main = True
    while flag_main:
        print('Welcome to our little game...')
        q1 = format(input('''
        In a little meadow under a tree, a group of fairies were hard at work. 
        As they were working a garden gnome ran into the tree that the fairies lived in,
        and began violently shaking the tree,
        the fairies rushed in and began fighting the gnome. 
        Do you FOLLOW after the gnome or do you RUN away?\n\n'''))
        wait()

        if q1 == 'follow':
            flag_main = False
            print('''
            Upon entering the tree you quickly realize that the gnomes are
            at war with the fairies as they begin pelting the gnome with 
            acorns and zapping it with various magical spells.
            The gnome writhes in agony as the attacks tear away at its ceramic flesh\n''')

            sub_flag1 = True
            while sub_flag1:
                q2_1 = format(input('''
                Do you help the FAIRIES or the GNOME?\n\n'''))
                wait()

                if q2_1 == 'fairies':
                    sub_flag1 = False
                    print('''
                    A fairy approaches you during battle and requests your aid.
                    They inform you that the garden gnomes have been terrorizing
                    the fairies for over 5 millennia in search of their magical power
                    held within a relic long lost, even by the fairies, though it is
                    prophesized that the fairies are in possesion of it. 
                    Though it is speculated that a certain hero would eventually find
                    the weapon and put an end to the war. The lone fairy instructs you to find
                    a weapon and attack the gnome. The fairy also informs you that the
                    ley lines can be used by fairies to gain access to arcane
                    abilities, all that must be done is touch it\n''')

                    while True:
                        q3_1 = format(input('''
                        You frantically scan the room for potential weapons, you are able to locate 3, 
                        do you pickup a rubber DUCK with a frog hat, a SWORD, or 
                        touch the ley line and gain access to magical SPELLS\n\n'''))
                        wait()

                        
                        if q3_1 == 'duck':
                            print('''
                            You appraoch the rubber ducky and begin to hear voices, almost whispering, though
                            they are unintelligible, the rubber ducky begins to glow and levitate as you
                            come closer, the duck tells you that you are the chosen one as it begins growing in size.
                            After a couple moments the duck is now the size of a horse and begins quacking at a frequency
                            that pulverizes the ceramic of the gnomes, causing it to disintegrate. You and this duck with a frog hat
                            begin an offense against the gnomes with the fairies following this victory and exterminate
                            the garden gnome race. In your journies you meet a magical unicorn named Jerry
                            that eats tacos.''')

                            return '\n'*3 + 'Game Over - You Win'

                        elif q3_1 == 'sword':
                            print('''
                            You head over to a weaponrack containing a variety of weapons and pickup
                            the sword, you rush into battle but are met with a quick end as the gnome downs
                            you with one fell swoop.''')
                            return '\n'*3 + 'Game Over - You Lose'

                        elif q3_1 == 'spells':
                            print('''
                            In the chaos of battle you navigate towards the ley line, you can see a purple
                            substance ebb and flow through its opalescent surface, as you draw closer
                            you can begin to feel it pulsate within you. You reach out to grasp it and
                            you begin to glow and feel a red hot sensation emerge from within
                            as all your organs rupture and your extremites are ripped off and spewed about,
                            in these final moments you recall that this power was meant only for the fairies.''')
                            return '\n'*3 + 'Game Over - You Lose'
                        
                        else:
                            print('Invalid Choice, Try Again')

                elif q2_1 == 'gnome':
                    sub_flag1 = False
                    print('''You rush to the aid of the gnome, hoping to quell
                    its suffering, you notice a massive ley line that seems the gnome appears
                    to be after.\n''')
                    
                    sub_flag2 = True
                    while sub_flag2: 

                        q3_2 = format(input('''
                        Do you pickup ROCKS to strike the fairies that are attacking the gnomes
                        or do you RUSH towards the ley line?\n\n'''))
                        wait()

                        if q3_2 == 'rocks':
                            print('''
                            You pick up several rocks and begin throwing them at
                            the fairies, you are immedaitely struck by a spell and die.''')
                            return '\n'*3 + 'Game Over - You Lose'

                        elif q3_2 == 'rush':
                            print('''You sprint towards the ley line but are quickly stopped
                            in your tracks by a barrage of acorns and have you skin ripped apart
                            until you bleed to death.''')
                            return '\n'*3 + 'Game Over - You Lose'

                        else:
                            print('Invalid Choice, Try Again')

                else:
                    print('Invalid Choice, Try Again')

        elif q1 == 'run': 
            flag_main = False
            print('''
            You run into the magical forest and escape the battle, 
            as you emerge from the thickett you find a path that leads 
            to a fork in the road.\n''')

            sub_flag1 = True
            while sub_flag1:
                q2_2 = format(input('''
                Do you go LEFT or RIGHT on the fork\n\n'''))
                wait()

                if q2_2 == 'left':
                    print('''
                    You follow the fork to the left and begin to feel hungry,
                    you keep going as this area of the forest makes you feel uneasy,
                    as you continue on you notice some mysterious, glowing fruit on the side
                    of the path.\n''')

                    sub_flag2 = True
                    while sub_flag2: 

                        q3_3 = format(input('''
                        Do you stop and EAT the fruit or do you CONTINUE
                        walking forward in hopes of finding something better?\n\n'''))
                        wait()

                        if q3_3 == 'eat':
                            print('''
                            You approach the bush continaing the myterious vessel, you
                            notice the leaves of the plant have a blue sheen, and that it is lines with small prickles
                            and that the fruit is in a cardioid shape, you pluck the fruit from its thory host and
                            begin devouring it to replenish your hunger. Not too longer after you begin you feel
                            a sharp pain in your chest and you collapse, you undergo cardiac arrest and die.''')
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_3 == 'continue':
                            print('''
                            You continue along the path, and are unable to find food or water,
                            you collapse on the side of the pathway, you are unable to move due to 
                            exhaustion, you begin to lose consciousness as you try to scavenge for
                            food but are unable to find any. You die a slow and painful death
                            from dehydration and starvation.''')
                            return '\n'*5 + 'Game Over - You Lose'
                        
                        else:
                            print('Invalid Choice, Try Again')

                elif q2_2 == 'right':
                    print('''
                    You begin your journey on the right side of the path, you hear the sound
                    of water and your heart jumps as you run towards it, you find a small river
                    and you plunge fast first into it and gulp down water by the gallon.\n''')

                    sub_flag2 = True
                    while sub_flag2: 

                        q3_4 = format(input('''
                        Do you FOLLOW the river upstream to find its source, or do you setup a CAMP?\n\n'''))
                        wait()

                        if q3_4 == 'follow':
                            print('''
                            You follow the river upstream and locate a magical pond with massive lily pads, in the center
                            a massive frog sits atop a throne in the flower of a lily larger than a semi, the frog
                            notices you as you walk closer in curiosity, the frog percieves you as a threat
                            and decides you would make a good snack, it eats you in one gulp. ''')
                            return '\n'*5 + 'Game Over - You Lose'

                        elif q3_4 == 'camp':
                            print('''
                            You begin to setup camp, as you scavenge for materials, as you pickup a branch that
                            looked like it would make a good support you notice a sharp pain in your back that reaches
                            through your chest, you look down and see a bloodied unicorn horn has pierced
                            you from behind, clean through your chest. The unicorn pulls its horn from you chest
                            and gallops away, with the faint scent of tacos in its trail. You die from
                            blood loss.''')
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
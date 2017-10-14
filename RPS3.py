#RPS version 3
import random
print 'Welcome to my rock paper scissors game!'

while True:

    #Player choice (PC) and computer choice (CC) made
    print 'Type rock, paper or scissors in the space below'
    PC = raw_input('> ')
    CompChoices = ['r','p','s']
    CC = random.choice(CompChoices)

    def Ascii(rps):
        if rps == 'r':
            print """Computer chose Rock!
                     _______
              ------'   ____)
                       (_____)
                       (_____)
                       (____)
              ------.__(___)
                \n"""
        elif rps == 's':
                print """Computer chose Scissors!
                         _______
                  ------'   ____)____
                               ______)
                            __________)
                           (____)
                  ------.__(___)
                  \n"""
        else:
                print """Computer chose paper!
                   _______
             -----'   ____)____
                         ______)
                         _______)
                        _______)
             -----.__________)
             \n"""

    def Win():
        print "You win!"

    def Lose():
        print "You lose!"

    def Tie():
        print "You tied!" 

    if PC == 'rock':
        PC = 'r'
    elif PC == 'paper':
        PC = 'p'
    else: PC = 's'

    Ascii(CC)

    if PC == CC:
        Tie()

    elif (PC == 'r' and CC == 's') or (PC == 'p' and CC == 'r'):
        Win()

    else: Lose()

    while True:
        answer = raw_input('Keep playing? (y or n): ')
        if answer in ('y', 'n'):
            break
        print '\nInvalid input.'
    if answer == 'y':
        continue
    else:
        print "\nGoodbye"
        break

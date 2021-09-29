import random
def guessthegame():
    computerguess = random.randint(0,20)
    endgame = True
    while endgame == True:
        myguess = int(input('Enter your guess: '))
        if computerguess == myguess:
            print('You win')
            endgame = False
        else:
            print('You lose 🥺🥺🥺')


guessthegame()

import random
Derrick = []
for i in range(1,31):
    Derrick.append(i)

print(Derrick)
random.choice(Derrick)
random.shuffle(Derrick)
# Derrick.pop()
# Derrick.remove(10)
print(Derrick) 
import random
Derrick = []
for i in range(1,31):
    Derrick.append(i)

print(Derrick)
random.choice(Derrick)
random.shuffle(Derrick)
# Derrick.pop()
# Derrick.remove(10)
print(Derrick)
Derrick = []
for i in range(1,31):
    Derrick.append(i)

print(Derrick)
random.choice(Derrick)
random.shuffle(Derrick)
# Derrick.pop()
# Derrick.remove(10)
print(Derrick)


import random
def Derrick_Patrick_Asher_Kofi():
    number_of_trials_for_easy = 10
    number_of_trials_for_hard = 5
    user_input = input('Enter the level of Complexity, Easy or Hard').lower()
    computerguess = random.randint(0,20)
    endgame = True

    while endgame == True:
        my_guess = int(input('Guess the number the computer picked: '))
        if user_input == 'easy':
            if my_guess > computerguess:
                print('Your guess is too high')
            elif my_guess < computerguess:
                print('Your guess is too low')
            elif my_guess == computerguess:
                print('you win')
                endgame = False
            number_of_trials_for_easy-=1
            if number_of_trials_for_easy == 0:
                print('You lose 🥺🥺🥺')
                endgame = False
        else:
            
            if my_guess > computerguess:
                print('Your guess is too high')
            elif my_guess < computerguess:
                print('Your guess is too low')
            elif my_guess == computerguess:
                print('you win')
                endgame = False
            number_of_trials_for_hard-=1
            if number_of_trials_for_hard == 0:
                print('You lose 🥺🥺🥺')
                endgame = False
Derrick_Patrick_Asher_Kofi()
                



        




    

import random
#number = random.randint(1, len(choices))

def magic_8():
    input('What is your question? >> ')
    choices = ['No', 'Definitely not!' , 'Sure!', 'Why not?' , 'Yes' , 'Unsure' , 'Try Again' ]
    print(random.choice(choices))

    answer = input('Would you like to play again?')
    if answer == 'yes' or answer == 'Y' or answer == 'Yes':
        print('Great! What is your next question?')
        magic_8()
    else:
        print('Ok, thanks for playing')


magic_8()

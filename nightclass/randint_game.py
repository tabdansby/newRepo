import random

correct_answer = random.randint(1, 100)


game_running = True
while game_running:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
    except ValueError:
        print('This is not a valid integer')
        continue
    if guess < correct_answer:
        print("Your guess was too low.")
    elif guess > correct_answer:
        print("Your guess was too high")
    else:
        print("correct answer!".format(correct_answer))
        game_running = False

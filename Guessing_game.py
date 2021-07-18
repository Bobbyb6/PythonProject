import random


def get_user_guess():
    try:
        if is_duplicate_guess:
            user_guess = int(input('You have previously tried this guess try a new number!: '))
        else:
            user_guess = int(input(f"Guess a number from 1-10! You have {guess_count} more guesses remaining: "))
    except ValueError:
        print('Incorrect Character! Select a number 1-10')
    return user_guess


guess_count = 5
attempts = 1
past_guesses = []
computer_guess_number = random.randint(1, 10)
is_duplicate_guess = False
while attempts < 6:
    user_guess = get_user_guess()
    if user_guess == computer_guess_number:
        print('Great guess! you have won!!!')
        break
    elif user_guess in past_guesses:
        is_duplicate_guess = True
    elif attempts < 5:
        print('Sorry wrong number guess again!')
        past_guesses.append(user_guess)
        attempts = attempts + 1
        guess_count = guess_count - 1
        is_duplicate_guess = False
    else:
        print('Game over you ran out of guesses\n The correct number was', computer_guess_number)
        break

from random import randint

random_int = randint(1, 100)
guesses = 0

while True:
    guess = raw_input('Enter your guess: ')
    int_guess = int(guess)
    guesses += 1

    if int_guess > random_int:
        print 'Your guess is too high!'
    elif int_guess < random_int:
        print 'Your guess is too low!'
    else:
        print 'Your guess is correct!'
        print 'You guessed the correct number in {} attempts!'.format(guesses)
        break

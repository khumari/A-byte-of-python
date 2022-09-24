import random

number = random.randint(0,5)
coins = 3
running = True

while running and coins > 0:
    guess = int(input('Enter a number'))

    if guess == number:
        print('congratulation you guessed it right')
        running = False
    elif guess <= number:
        print('you guessed a smaller number')
    else:
        print('you guessed a large number')
    coins -= 1
    print('now you have {} coins'.format(coins))

print('Done')
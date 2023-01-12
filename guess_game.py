from random import randint

print('I am thinking of a number between 1 and 20')
secret_number = randint(1, 20)

for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())
    if guess > secret_number:
        print('guess is too high')

    elif guess < secret_number:
        print('guess is too low')

    else:
        break

if guess == secret_number:
    print(f'Good job! You guessed the secret number in {guessTaken} times')

else:
    print(f'The number I was thinking of is {str(secret_number)}')
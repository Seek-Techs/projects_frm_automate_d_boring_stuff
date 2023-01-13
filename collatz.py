def collatz(number):
    if number % 2 == 0:
       return number // 2
    elif number % 2 == 1:
        return  3 * number + 1

try:
    user = int(input('Enter a number: '))
    print(collatz(user))
except ValueError:
    print('Invalid number')


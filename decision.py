from random import randint

def make_decision(answer):

    if answer == 1:
        return 'i want sleep'

    elif answer == 2:
        return 'i want to you'

    elif answer == 3:
        return 'i want to eat'

# random = randint(1, 3)
# decision = make_decision(random)
# print(decision)
print(make_decision(randint(1, 3)))
from random import randint

def get_answer(answer):
    if answer == 1:
        return 'its certain'

    elif answer == 2:
        return 'it is decidedly so'

    elif answer == 3:
        return 'yes'

    elif answer == 4:
        return 'reply hazy try again'

    elif answer == 5:
        return 'ask again later'

    elif answer == 6:
        return 'concentrate and ask again'

    elif answer == 7:
        return 'my reply is no'

    elif answer == 8:
        return 'outlook not so good'

    elif answer == 9:
        return 'doubtful'


ran = randint(1, 9)
fortune = get_answer(ran)
print(fortune)
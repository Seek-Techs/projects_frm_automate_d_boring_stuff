myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name')
name = input()


# check if the name is in the list of myPets
if name not in myPets:
    print('I do not have a pet named: ' + name)

else:
    print(name + ' is my pet')



# Removal of value from myPets
try:
    # To know the index at which a particular element at in myPets's list
    print('At index ' + str(myPets.index(name)))
    myPets.remove(name)
except ValueError:
    print('It does not exist named: ' + name)



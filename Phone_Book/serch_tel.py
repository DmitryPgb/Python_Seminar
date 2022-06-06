from importlib.metadata import entry_points


def sderch():
    print('what do you want to find? \n\
        1 - Surname;\n\
        2 - Name;\n\
        3 - Phone number;\n\
        4 - Description.\n')
    a = int(input('Your choice: '))
    if a == 1:
        entry = input('Enter surname: ').title()
    if a == 2:
        entry = input('Enter name: ').title()
    if a == 3:
        entry = input('Enter phone number: ')
    if a == 4:
        entry = input('Enter description: ').title()

#print('You serch for: ', entry)
#return entry
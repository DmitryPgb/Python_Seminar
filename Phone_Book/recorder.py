def record():
    entry=[]
    surname = input('Enter surname: ')
    entry.append(surname)
    name = input('Enter name: ')
    entry.append(name)
    telephone = input('Enter telephone number: ')
    entry.append(telephone)
    description = input('Enter description: (personal, work, etc...): ')
    entry.append(description)
    print('You enterd: ', entry)
    return entry
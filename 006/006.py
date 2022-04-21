# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

DayOfWeek = 'Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Son'
day = int(input('Enter day of the week: '))

if(7>=day>=1):
    print(f'{day} is {DayOfWeek[day-1]}')
    if(day < 6):
        print('Working day')
    else:
        print("Weekend")

else:
    print('Enter number from 1 to 7')    
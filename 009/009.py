# Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти

QR = input('Введите номер четверти прямоугольной системы координат: ')
if (QR in ['1', 'I', 'Первая', 'Один']):
    print (f'В четверти номер {QR} допустимы значения координат: (Х>0,Y>0)')
elif (QR == '2'):
    print (f'В четверти номер {QR} допустимы значения координат: (Х<0,Y>0)')
elif (QR == '3'):
    print (f'В четверти номер {QR} допустимы значения координат: (Х<0,Y<0)')
elif (QR == '4'):
    print (f'В четверти номер {QR} допустимы значения координат: (Х>0,Y<0)')
else:
    print ('Введено некорректное значение, введите номер четверти 1-4')
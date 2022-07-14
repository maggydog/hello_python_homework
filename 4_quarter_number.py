# Найти по четверти диапазон возможных координат

q=int(input('введите номер четверти: '))

while q<=0 or q>4:
    q=int(input('попробуем снова. введите номер четверти: '))
 

def CoordinatesForQuarter (a):
    if a==1:
        print('x>0,y>0')
    elif a==2:
        print('x<0,y>0')
    elif a==3:
        print('x<0,y<0')
    else:
        print('x>0,y<0')

CoordinatesForQuarter(q)
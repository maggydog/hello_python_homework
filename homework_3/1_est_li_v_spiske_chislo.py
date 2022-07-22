#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

spisok = ['df', 'nkj', '8', 'sdf', 'dfs', '785']

n=input('что мы ищем в списке: ')

def SearchInList (a):
    b=False
    for i in spisok:
        if i == a:
            print (f'в списке есть {a}')
            b=True
    if b==False:
        print (f'в списке нет {a}')    

SearchInList(n)

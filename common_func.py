import random

def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def FillListWithFib (n):
    result = []
    for i in range(1,n+1):
        result.append(fib(i))
    return result  


def SearchInList (a, spisok):
    b=False
    for i in spisok:
        if i == a:
            print (f'в списке есть {a}')
            b=True
    if b==False:
        print (f'в списке нет {a}')   


def SearchSecondEnter (spisok,n):
    count=0
    for i in range(0,len(spisok)):
        if spisok[i] == n:
            count+=1
            if count==2:
                print(i)
    if count == 0:
        print('в списке нет такой строки')
    elif count == 1:
        print('такая строка встречается в списке один раз')


def MultInRow (a):
    mult=1
    for i in range(1,a+1):
        mult*=i
        print(mult, end = " ")


def WhichQuadrant (a,b):
    if a>0 and b>0:
        print('1 квадрант')
    elif a<0 and b>0:
        print('2 квадрант')
    elif a<0 and b<0:
        print('3 квадрант')
    else:#if a>0 and b<0:
        print('4 квадрант')


def CoordinatesForQuarter (a):
    if a==1:
        print('x>0,y>0')
    elif a==2:
        print('x<0,y>0')
    elif a==3:
        print('x<0,y<0')
    else:
        print('x>0,y<0')

        
def MakeNumWithoutPoint(num):
    num = str(num).split('.')
    num = int(num[0]+num[1])
    return num

def SumOfNumbers (num):    
    sum=0
    while num>0:
        sum+=num%10
        num=int(num/10)
    print(sum)  


def MultInRow (a):
    mult=1
    for i in range(1,a+1):
        mult*=i
        print(mult, end = " ")


def MakeAListByEnter (longitude): #странный
    spisok=[0]*longitude
    for i in range(0,len(spisok)):
        print(i)
        spisok[i] = int(input('Enter number: '))
        print(spisok[i])
        if spisok[i] == '0':
            print(spisok[i])
            break        
    return spisok  


def MakeAListByEnterWithLong (longitude): #более адекватный через ввод чисел с заданной длиной
    spisok=[]
    for i in range(0,longitude+1):
        spisok.append(int(input('enter number: ')))        
    return spisok  

def MakeAListOfRealNumsByEnterWithLong (longitude): #заполнение списка действительными числами от руки
    spisok=[]
    for i in range(0,longitude+1):
        spisok.append(float(input('enter number: ')))        
    return spisok  

def MakeAListByRandomWithLong (longitude, min, max): #заполнение списка через рэндом
    spisok=[]
    for i in range(0,longitude+1):
        spisok.append(random.randint(min,max))        
    return spisok  



def MakeAListOfRealNumsByRandomWithLong (longitude, min, max): #заполнение списка через рэндом действиетльными числами
    spisok=[]
    for i in range(0,longitude+1):
        spisok.append(round(random.uniform(min,max),3))

    return spisok  


def MakeListInRow(a,b=0): #заполнение от 0 до a или от b до a
    new_list = [i for i in range(b,a)]
    return new_list


def SumNotEvenPosition (spisok): #сумма эл-тов на нечетных позициях
    sum=0
    for i in range(0,len(spisok)):
        if i%2!=0:
            sum+=spisok[i]
    return sum

def SumNotEvenPosition (spisok): #сумма эл-тов на нечетных позициях, проще
    sum=0
    for i in range(1,len(spisok),2):
        sum+=spisok[i]
    return sum

def SumNotEvenPosition2 (spisok): #сумма эл-тов на нечетных позициях
    sum=0
    for i in range(0,len(spisok)):
        if i%2!=0:
            sum+=spisok[i]
    return sum

def SumOfEvenPosition2 (spisok): #сумма эл-тов на четных позициях, проще
    sum=0
    for i in range(0,len(spisok),2):
        sum+=spisok[i]
    return sum       


def MultOfPairs(spisok):  #произведение пар с двух концов с print
    if len(spisok)%2==0:
        for i in range(0,int(len(spisok)/2)):
            print(spisok[i]*spisok[-i-1])
    else:
        for i in range(0,int(len(spisok)/2+1)):
            print(spisok[i]*spisok[-i-1])


def FindMax (spisok):
    max = spisok[0]
    for i in spisok:
        if i>max:
            max=i
    return max  

def FindMin (spisok):
    min = spisok[0]
    for i in spisok:
        if i<min:
            min=i
    return min 

#def TakeAfterPointPart(spisok): ytdthyj неверно работает если после запятой 083 или 41, он посчитает минимумом 41, хотя есть 083(его он возьмет как 83)
    new_list=[]
    for i in spisok:
        i = str(i).split('.')
        i = int(i[1])
        new_list.append(i)
    return new_list

def TakeAfterPointPart(spisok): #арифметически находим дробную часть: i-int(i)
    new_list=[]
    for i in spisok:
        new_list.append(round(float(i-int(i)),3))
    return new_list



def From10To2 (number):
    res = ''
    r=''
    while number>=2:
        res=res+str(number%2)
        number=int(number/2)
    res=res+str(number) 
    for i in range(0,int(len(res))):
        r=r+res[-i-1]
    return r

def DecToBin(n):
    lstBin = []
    while n > 0:
        lstBin.append(str(n%2))
        n  //= 2
    return "".join(lstBin[::-1])
     
    



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n=input('Задайте натуральное число N: ')

def TestForNaturalNumber (a):
    try:
        a=int(a) 
        assert a>0
        return True
    except:
        return False

def IsItPrimeNumber (a):
    a=int(a)
    if a==1:
        return a==1
    elif a%2==0:
        return a==2
    delitel=3
    while a%delitel!=0:
        delitel+=2
    return delitel==a    

def ListOfFirst10000PrimeNumbers ():
    prime_list=[]
    prime_list.append(1)
    count=2
    while count<10000:
        if IsItPrimeNumber(count) == True:
            prime_list.append(count)
        count+=1
    return prime_list 

def MakeAListOfFactors(a):
    pl=ListOfFirst10000PrimeNumbers()
    index=1
    list_of_mult=[]
    if IsItPrimeNumber(a) == True or a==1:
        return 'вы ввели простое число, его делители - оно само и 1'
    while IsItPrimeNumber(a) == False or a!=1:
        if int(a)%int(pl[index])==0: #тут пришлось нагородить конвертаций, а то не пропускал
            a=int(int(a)/pl[index]) # и тут
            list_of_mult.append(pl[index])
        else:
            index+=1
    return list_of_mult       


while TestForNaturalNumber(n) == False:
    n=input('Это было не то. Задайте натуральное число N: ')
print(MakeAListOfFactors(n))

# вот этот код ниже почему-то странно сработал: проверка выполнялась хорошо, 
# но для следущей функции бралось первое введенное знаечние, а не последнее верное:
# если ввести выа ыап 12, то возьмет в работу все равно выа, а не 12
'''
def TestForNaturalNumber (a):
    fortest=True
    while fortest==True:
        try:
            a=int(a) 
            assert a>0
            fortest=False
        except:
            print('Это было не то. Задайте натуральное число N: ')
            a=input()
'''
   
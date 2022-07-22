#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('введите вещественное число(мы ограницены 6 знаками после ,):  '))

def MakeNumWithoutPoint (num):
    num = str(num).split('.')
    num=int(num[0]+num[1])
    return num

def SumOfNumbers (num):    
    sum=0
    while num>0:
        sum+=num%10
        num=int(num/10)
    print(sum)  

newNumber=MakeNumWithoutPoint(number)
SumOfNumbers(newNumber)     


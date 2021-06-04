import random

#Вариант 10
#Задание 4

def genMas(k, n):
    if(k <= 0 and k <= 0):
        raise Exception("Неверные аргументы")
    li = list(range(k))
    for i in range(0, k):
        li[i] = [random.randint(0, 100) for i in range(n)]
    temp = []
    s = 0
    for mas in li:
        if(sum(mas) > s):
            s = sum(mas)
            temp = mas
    return temp
    
print(genMas(10, 5))

#Задание 9

def tableCheck():
    x = input("Введите первое число: ")
    y = input("Введите второе число: ")
    answer = input("Введите результат перемножения " + x + " и " + y + " : ")
    if(int(answer) == int(x)*int(y)):
        print("Верно")
    else:
        print("Ошибка. Верный ответ " + str(int(x)*int(y)))

tableCheck()

#Задание 10
def minAndMax(length):
    if(length <= 0 ):
        raise Exception("Неверные аргументы")
    li = [random.randint(0, 100) for i in range(length)]
    return (max(li), min(li))

print(minAndMax(10))
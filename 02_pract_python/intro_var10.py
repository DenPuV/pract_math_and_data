import random

#Вариант 10
#Задание 4

def genMas(k, n):
    if(k <= 0):
        raise Exception("Неверные аргументы")
    li = list(range(k))
    for i in range(0, k):
        li[i] = [random.randint(0, 100) for i in range(n)]
    return max(li, key=lambda arr: sum(arr))
    
print(genMas(10, 5))

#Задание 9

def tableCheck():
    x = input("Введите первое число: ")
    y = input("Введите второе число: ")
    try:
        int(x)
        int(y)
    except:
        print("Не верные числа")
        return
    answer = input("Введите результат перемножения " + x + " и " + y + " : ")
    try:
        int(answer)
    except:
        print("Не верное числo")
        return
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
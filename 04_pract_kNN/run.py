import numpy as np
from kNN import k_nearest

X = np.array([[33., 21., 1],
             [41., 13., 1],
             [18., 22., 1],
             [38., 34., 1],
             [62., 118., 2],
             [59., 137., 2],
             [95., 131., 2],
             [83., 110., 2],
             [185., 155., 3],
             [193., 129., 3],
             [164., 135., 3],
             [205., 131., 3],
             [145., 55., 4],
             [168., 35., 4],
             [135., 47., 4],
             [138., 66., 4]])


while(True):
    try:
        height = float(input('Введите рост: '))
        weight = float(input('Введите вес: '))
        if(height > 0 and height < 300 and weight > 0 and weight < 300): break
        else: print("Неверные параметры")
    except:
        print("Неверные параметры")
    


obj = np.array([height, weight])

monkeys = {1: 'lemur', 2: 'chimpanze', 3: 'gorilla', 4: 'orangutan'}
print(monkeys[k_nearest(3).fit(X).predict(obj)])
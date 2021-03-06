import sys
from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

try:
    im = Image.open('image.jpg')
    data = np.array(im.getdata()).reshape([im.height, im.width, 3])
except:
    print("файл не найден")
    sys.exit()


x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

plt.plot(data[0, :, 0], 'r-')
plt.plot(data[0, :, 1], 'g-')
plt.plot(data[0, :, 2], 'b-')
plt.grid()
plt.show()

#вариант 1
#Привести графики как на рисунке 1 для всех цветовых каналов отдельной строки изображения. 
#Должно быть 3 графика на одном объекте Figure, для каждого цветового канала должна быть рассчитана и изображена кривая регрессии.

lm = linear_model.LinearRegression()
colors = ['r', 'g', 'b']

for i in range(3):
    plt.plot(data[0, :, i], colors[i] + '-')
    plt.plot(lm.fit(X, data[0, :, i]).predict(X), colors[i] + '--')

plt.grid()
plt.show()
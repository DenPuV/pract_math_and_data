import numpy as np

# import sklearnsvm as svm

# евклидово расстояние между двумя точками
def dist(A, B):
    if (isinstance(A, np.ndarray) and isinstance(B, np.ndarray)):
        return np.sqrt(np.sum((A - B) ** 2))
    else:
        raise Exception("Неверный тип массивов")


# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
  m = len(X)
  k = len(centers)

  # матрица расстояний от каждой точки до каждого центра
  distances = np.zeros((m, k))
  for i in range(m):
    for j in range(k):
      distances[i, j] = dist(centers[j], X[i])

  # поиск ближайшего центра для каждой точки
  return np.argmin(distances, axis=1)


class kmeans:
    
    def __init__(self, k):
        self.k = k
        
    def fit(self, X):
        if len(X) < 1: return
        m, n = X.shape

        curr_iteration = prev_iteration = np.zeros(m)
        _min = np.min(X, axis=0)
        _max = np.max(X, axis=0)
        centers = np.random.random((self.k, n))*(_max - _min) + _min

  # приписываем каждую точку к заданному классу
        curr_iteration = class_of_each_point(X, centers)
        while np.any(curr_iteration != prev_iteration):
            prev_iteration = curr_iteration

    # вычисляем новые центры масс
            for i in range(self.k):
                sub_X = X[curr_iteration == i,:]
                if len(sub_X) > 0:
                    centers[i,:] = np.mean(sub_X, axis=0)

    # приписываем каждую точку к заданному классу
            curr_iteration = class_of_each_point(X, centers)
        
        return centers
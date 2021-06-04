import numpy as np
import math



def k_nearest(X, k, obj):
    
    sub_X = X[:, 0:-1]
    av = np.mean(sub_X, axis = 0)
    dev = np.std(sub_X, axis = 0)
    
    
    for i in range(len(obj)):
        obj[i] = (obj[i]-av[i])/dev[i]
        
    for i in range(sub_X.shape[1]):
        sub_X[:, i] = (sub_X[:, i] - av[i])/dev[i]
    
    _dist = [dist(i, obj) for i in sub_X]
    
    sort = np.argsort(_dist)
    
    sortMas = sort[0:k]
    
    nearest_classes = X[[sortMas], -1]
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]

    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))

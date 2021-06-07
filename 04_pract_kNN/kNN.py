import numpy as np
import math

class k_nearest:
    
    def __init__(self, k):
        self.k = k
    
    def fit(self, X):
        self.X = X
        self.sub_X = X[:, 0:-1]
        self.av = np.mean(self.sub_X, axis = 0)
        self.dev = np.std(self.sub_X, axis = 0)
        self.sub_X = (self.sub_X - self.av) / self.dev
        return self
        
    def predict(self, obj):
        obj = (obj - self.av) / self.dev
        _dist = [dist(i, obj) for i in self.sub_X]
        sort = np.argsort(_dist)
        sortMas = sort[0:self.k]
        nearest_classes = self.X[[sortMas], -1]
        unique, counts = np.unique(nearest_classes, return_counts=True)
        return unique[np.argmax(counts)]
    
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))

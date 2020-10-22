from algorithms.algorithm import Algorithm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class KNN(Algorithm):

    def __init__(self, X_train, Y_train, k_val):
        super(KNN, self).__init__(X_train, Y_train)
        self._model = KNeighborsClassifier(n_neighbors=3)
        self.k_val = k_val

    def train(self):
        self._model.fit(self.X_train, self.Y_train)

    def predict(self, point):
        inp = np.array([list(point)])
        class_val = self._model.predict(inp)
        return int(class_val) + 2

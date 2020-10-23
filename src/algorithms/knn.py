from algorithms.algorithm import Algorithm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from utils.popup_message import show_popup


class KNN(Algorithm):

    def __init__(self, X_train, Y_train, event_vals):
        super(KNN, self).__init__(X_train, Y_train)

        try:
            self._k_val = int(event_vals["knn_k_val"])
        except ValueError:
            show_popup(1, "Invalid K Value", "The inputted value for K is not an integer.\n\nPlease input an integer.")
            return

        if self._k_val > X_train.shape[0]:
            show_popup(1, "Invalid K Value", "The inputted value for K is greater than the size of the "
                                             "dataset.\n\nAdd more data points, or reduce the value of k")
            return

        self._model = KNeighborsClassifier(n_neighbors=self._k_val)
        print(f"KNN: K={self._k_val}")

    def train(self):
        self._model.fit(self.X_train, self.Y_train)

    def predict(self, point):
        inp = np.array([list(point)])
        class_val = self._model.predict(inp)
        return int(class_val) + 2

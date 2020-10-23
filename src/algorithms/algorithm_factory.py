from algorithms.knn import KNN
from algorithms.logreg import LogisticRegression
from utils.popup_message import show_popup

class AlgorithmFactory:

    @staticmethod
    def get_algorithm(algorithm_i, event_vals, X_train, Y_train):
        if algorithm_i == 0:
            return KNN(X_train, Y_train, event_vals)
        elif algorithm_i == 1:
            return LogisticRegression(X_train, Y_train, event_vals)
        else:
            show_popup(1, "Fatal Error", "Chosen algorithm is not defined")
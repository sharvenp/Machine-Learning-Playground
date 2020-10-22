from algorithms.knn import KNN


class AlgorithmFactory:

    @staticmethod
    def get_algorithm(algorithm_i, X_train, Y_train):
        if algorithm_i == 0:
            return KNN(X_train, Y_train, 5)
        else:
            print("Algorithm not defined")
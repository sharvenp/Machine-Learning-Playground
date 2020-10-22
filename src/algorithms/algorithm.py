
class Algorithm:

    def __init__(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        self._model = None

    def train(self, *args):
        raise NotImplementedError;

    def predict_point(self, point):
        if self._model:
            self.predict(point)
        else:
            print("No model trained!")

    def predict(self, point):
        raise NotImplementedError;


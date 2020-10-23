from utils.popup_message import show_popup


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
            show_popup(0, "No Model Trained", "Please train the model before predicting")

    def predict(self, point):
        raise NotImplementedError;

    def is_model_initialized(self):
        return self._model is not None

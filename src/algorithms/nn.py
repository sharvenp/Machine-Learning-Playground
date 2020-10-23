from algorithms.algorithm import Algorithm
from sklearn.neural_network import MLPClassifier
import numpy as np
from utils.popup_message import show_popup


def _parse_hidden_layer_string(formatted_string):
    splits = formatted_string.split(",")
    hidden_layers = []
    for val in splits:
        try:
            num_val = int(val)
        except ValueError:
            return None
        hidden_layers.append(num_val)

    return hidden_layers


class NeuralNet(Algorithm):

    def __init__(self, X_train, Y_train, event_vals):
        super(NeuralNet, self).__init__(X_train, Y_train)

        self._hidden_layers = _parse_hidden_layer_string(event_vals["nn_nhl"])

        if self._hidden_layers is None:
            show_popup(1, "Invalid Format for Hidden Layers", "The format for hidden layers is incorrect.\n\nPlease "
                                                              "input hidden layer sequence seperated by commas.\n\nE.g."
                                                              " Format for three hidden layers: '100,50,20'")
            return

        try:
            self._lr = float(event_vals["nn_lr"])
        except ValueError:
            show_popup(1, "Invalid Learning Rate", "The inputted value for learning rate is not a "
                                                   "float.\n\nPlease input an float.")
            return

        try:
            self._reg = float(event_vals["nn_reg"])
        except ValueError:
            show_popup(1, "Invalid L2 Regularization Penalty", "The inputted value for L2 regularization penalty is "
                                                               "not a float.\n\nPlease input an float.")
            return

        try:
            self._epochs = int(event_vals["nn_epochs"])
        except ValueError:
            show_popup(1, "Invalid Number of Epochs", "The inputted value for number of epochs is not an "
                                                      "integer.\n\nPlease input an integer.")
            return

        self._model = MLPClassifier(solver='lbfgs', alpha=self._reg, learning_rate_init=self._lr,
                                    hidden_layer_sizes=tuple(self._hidden_layers), random_state=1,
                                    max_iter=self._epochs)

        # print(f"KNN: K={self._k_val}")

    def train(self):
        self._model.fit(self.X_train, self.Y_train)

    def predict(self, point):
        inp = np.array([list(point)])
        class_val = self._model.predict(inp)
        return int(class_val) + 2

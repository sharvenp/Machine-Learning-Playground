from algorithms.algorithm import Algorithm
from sklearn.linear_model import LogisticRegression as LogReg
import numpy as np
from utils.popup_message import show_popup


class LogisticRegression(Algorithm):

    def __init__(self, X_train, Y_train, event_vals):
        super(LogisticRegression, self).__init__(X_train, Y_train)

        penalty_str = ""
        if event_vals['logreg_reg_l1']:
            penalty_str = 'l1'
            self._model = LogReg(penalty=penalty_str, solver='liblinear')
        elif event_vals['logreg_reg_l2']:
            penalty_str = 'l2'
            self._model = LogReg(penalty=penalty_str, solver='lbfgs')
        elif event_vals['logreg_reg_none']:
            penalty_str = 'none'
            self._model = LogReg()

        print(f"Logistic Regression: Penalty = {penalty_str}")

    def train(self):
        self._model.fit(self.X_train, self.Y_train)

    def predict(self, point):
        inp = np.array([list(point)])
        class_val = self._model.predict(inp)
        return int(class_val) + 2

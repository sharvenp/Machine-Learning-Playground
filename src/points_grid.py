from algorithms.algorithm_factory import AlgorithmFactory
from observable import Observable
from settings import Settings
from commands import Commands
import numpy as np
import random
import json
from utils.popup_message import show_popup


def _check_in_bounds(point):
    row, col = point
    return (0 <= row < Settings.GRID_WIDTH) and (0 <= col < Settings.GRID_WIDTH)


class PointGrid(Observable):

    def __init__(self):
        Observable.__init__(self)
        self._grid = {}
        self._algorithm = None

    def add_point(self, new_point, class_val):
        if not _check_in_bounds(new_point):
            return

        if new_point not in self._grid:
            self._grid[new_point] = class_val
            self.notify_observers((Commands.ADD_POINT, new_point, class_val))
        elif new_point in self._grid:
            val = self._grid[new_point]
            if val != class_val:
                self._grid[new_point] = class_val
                self.notify_observers((Commands.REPLACE_POINT, new_point, class_val))

    def remove_point(self, point):
        if point in self._grid:
            self._grid.pop(point)
            self.notify_observers((Commands.REMOVE_POINT, point))

    def clear_grid(self):
        self._grid = {}
        self.notify_observers((Commands.CLEAR_ALL,))

    def _get_data(self):
        X_train = np.zeros((len(self._grid), 2))
        T_train = np.zeros(len(self._grid))

        i = 0
        keys = list(self._grid.keys())
        random.shuffle(keys)
        for train_example in keys:
            row, col = train_example
            class_val = self._grid[train_example]
            X_train[i][0] = row
            X_train[i][1] = col
            T_train[i] = class_val
            i += 1

        return X_train, T_train

    def predict(self, algorithm_i, event_vals):

        X_train, Y_train = self._get_data()

        self._algorithm = AlgorithmFactory.get_algorithm(algorithm_i, event_vals, X_train, Y_train)

        if not self._algorithm.is_model_initialized():
            return

        self._algorithm.train()

        self.notify_observers((Commands.CLEAR_ALL,))

        for row in range(Settings.GRID_WIDTH):
            for col in range(Settings.GRID_WIDTH):
                point = (row, col)
                if point not in self._grid:
                    class_val = self._algorithm.predict(point)
                else:
                    class_val = self._grid[point]

                self.notify_observers((Commands.ADD_POINT, (row, col), class_val))

    def get_grid(self):
        return self._grid

    def save_grid(self, path):
        try:
            with open(path, 'w') as f:
                for point in self._grid:
                    row, col = point
                    class_val = self._grid[point]
                    f.write(f"{row},{col},{class_val}\n")
                print(f"Saved to: {path}")
        except Exception as e:
            show_popup(1, "Save Error", "Encountered error while saving data:\n\n" + str(e))

    def load_grid(self, path):
        temp_grid = {}
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    vals = line.split(",")
                    if len(vals) != 3:
                        raise ValueError(f"Encountered invalid line formatting:\n{line}")

                    try:
                        row = int(vals[0])
                        col = int(vals[1])
                        class_val = int(vals[2])
                    except ValueError:
                        raise ValueError(f"Encountered non-integer values in line:\n{line}")

                    if class_val != 1 and class_val != 2:
                        raise ValueError(f"Encountered invlaid class value:\n{class_val}")

                    if not _check_in_bounds((row, col)):
                        raise ValueError(f"Encountered out-of-bound point coordinates:\n{(row, col)}")

                    temp_grid[(row, col)] = class_val

                self._grid = temp_grid
                self.notify_observers((Commands.DRAW_ALL, list(self._grid.items())))

        except Exception as e:
            show_popup(1, "Load Error", "Encountered error while loading data:\n\n" + str(e))

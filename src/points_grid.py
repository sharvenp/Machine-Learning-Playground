from observable import Observable
from settings import Settings
from commands import Commands


def _check_in_bounds(point):
    row, col = point
    return (0 <= row < Settings.GRID_WIDTH) and (0 <= col < Settings.GRID_WIDTH)


class PointGrid(Observable):

    def __init__(self):
        Observable.__init__(self)
        self._grid = {}

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

        print(f"Grid: {self._grid}")

    def remove_point(self, point):
        if point in self._grid:
            self._grid.pop(point)
            self.notify_observers((Commands.REMOVE_POINT, point))

    def clear_grid(self):
        self._grid = {}
        self.notify_observers((Commands.CLEAR_ALL,))

    def get_grid(self):
        return self._grid

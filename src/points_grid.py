
from observable import Observable

class PointGrid(Observable):

    def __init__(self):
        Observable.__init__(self)
        self._points = []

    def add_point(self, new_point):
        if new_point not in self._points:
            self._points.append(new_point)
            self.notify_observers()

    def clear_points(self):
        self._points = []
        self.notify_observers()

    def get_points(self):
        return self._points

class PointGridController:

    def __init__(self, new_point_grid):
        self._point_grid = new_point_grid

    def add_point(self, added_point):
        self._point_grid.add_point(added_point)
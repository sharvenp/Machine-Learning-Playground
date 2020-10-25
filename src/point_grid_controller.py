from settings import Settings


class PointGridController:

    def __init__(self, new_point_grid):
        self._point_grid = new_point_grid
        self._grid_resolution = Settings.GRAPH_WIDTH // Settings.GRID_WIDTH

    def add_point(self, added_point, class_val):
        x, y = added_point
        row = y // self._grid_resolution
        col = x // self._grid_resolution

        self._point_grid.add_point((row, col), class_val)

    def remove_point(self, point):
        x, y = point
        row = y // self._grid_resolution
        col = x // self._grid_resolution

        self._point_grid.remove_point((row, col))

    def clear_grid(self):
        self._point_grid.clear_grid()

    def predict(self, algorithm, event_vals):
        self._point_grid.predict(algorithm, event_vals)

    def save(self, path):
        self._point_grid.save_grid(path)

    def load(self, path):
        self._point_grid.load_grid(path)


from view import View
from point_grid_controller import PointGridController
from points_grid import PointGrid

if __name__ == "__main__":

    # Set up MVC
    m = PointGrid()
    c = PointGridController(m)
    v = View(c)
    m.add_observer(v)
    v.launch()

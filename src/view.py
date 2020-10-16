
import PySimpleGUI as sg

from settings import Settings
from observer import Observer

class View(Observer):

    def __init__(self, attached_controller):
        sg.theme(Settings.APP_THEME)

        app_layout = [  [sg.Graph(
                            canvas_size=(400, 400),
                            graph_bottom_left=(0, 0),
                            graph_top_right=(400, 400),
                            key="graph",
                            enable_events=True)],
                        [sg.Text('Enter something on Row 2'), sg.InputText()],
                        [sg.Button('Ok'), sg.Button('Cancel')]
                    ]

        self.window = sg.Window(title="Machine Learning Playground", layout=app_layout)
        self.window.Finalize()

        self.graph = self.window.Element("graph")
        
        self.controller = attached_controller

        self.drawn_figures = []

    def update(self, point_grid):
        
        if point_grid.get_points() == []:
            self._clear_graph()

        for x, y in point_grid.get_points():
            rect = self.graph.DrawRectangle((x, y), (x+3, y+3), fill_color="red")
            self.drawn_figures.append(rect)

    def _clear_graph(self):
        for figure in self.drawn_figures:
            self.graph.DeleteFigure(figure)

    def launch(self):
        
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break

            if values['graph']:
                self.controller.add_point(values['graph'])

        self.window.close()
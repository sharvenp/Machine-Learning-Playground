import PySimpleGUI as sg

from settings import Settings
from observer import Observer
from commands import Commands


class View(Observer):

    def __init__(self, attached_controller):

        self.point_width = Settings.GRAPH_WIDTH // Settings.GRID_WIDTH

        sg.theme(Settings.APP_THEME)

        app_layout = [[sg.Graph(
            canvas_size=(Settings.GRAPH_WIDTH, Settings.GRAPH_WIDTH),
            graph_bottom_left=(0, 0),
            graph_top_right=(Settings.GRAPH_WIDTH, Settings.GRAPH_WIDTH),
            key="graph",
            enable_events=True,
            background_color="lightgray")],
            [sg.Radio('■', 'class', default=True, size=(3, 1), text_color="red", font=("Consolas", 15), key="0_radio"),
             sg.Radio('■', 'class', size=(3, 1), text_color="blue", font=("Consolas", 15), key="1_radio"),
             sg.Radio('⌫', 'class', size=(3, 1), text_color="black", font=("Consolas", 15), key="erase_radio")],
            [sg.Button('Predict', key='predict'), sg.Button('Clear All', key='clear')]
        ]

        self.window = sg.Window(title="Machine Learning Playground", layout=app_layout)
        self.window.Finalize()

        self.graph = self.window.Element("graph")

        self.controller = attached_controller

        self._drawn_figures = {}

    def update(self, point_grid, command):

        command_id = command[0]

        if command_id == Commands.ADD_POINT:
            point, class_val = command[1], command[2]
            self._draw_point(point, class_val)

        elif command_id == Commands.REPLACE_POINT:

            point, class_val = command[1], command[2]
            self.graph.DeleteFigure(self._drawn_figures[point])
            self._draw_point(point, class_val)

        elif command_id == Commands.REMOVE_POINT:

            point = command[1]
            if point in self._drawn_figures:
                self.graph.DeleteFigure(self._drawn_figures[point])
                self._drawn_figures.pop(point)

        elif command_id == Commands.CLEAR_ALL:
            self._clear_graph()

    def _draw_point(self, point, class_val):
        row, col = point
        x = col * self.point_width
        y = row * self.point_width

        rect = self.graph.DrawRectangle((x, y), (x + self.point_width, y + self.point_width),
                                        fill_color=Settings.COLOR_MAP[class_val], line_width=0)

        self._drawn_figures[point] = rect

    def _clear_graph(self):
        self.graph.Erase()
        self._drawn_figures = {}

    def launch(self):

        while True:
            event, values = self.window.read()

            # print(event, values)

            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break
            elif event == 'graph' and values['graph']:
                if values['0_radio']:
                    self.controller.add_point(values['graph'], 1)
                elif values['1_radio']:
                    self.controller.add_point(values['graph'], 2)
                elif values['erase_radio']:
                    self.controller.remove_point(values['graph'])

            elif event == 'predict':
                self.controller.predict(0)
            elif event == 'clear':
                self.controller.clear_grid()

        self.window.close()

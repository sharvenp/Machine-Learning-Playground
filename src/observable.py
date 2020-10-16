
class Observable:

    def __init__(self):
        self.observers = []

    def add_observer(self, o):
        if o not in self.observers:
            self.observers.append(o)

    def notify_observers(self, command):
        for o in self.observers:
            o.update(self, command)
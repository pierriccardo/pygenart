from abc import abstractmethod

class Sketch:

    def __init__(self, canvas):
        self.c = canvas

    @abstractmethod
    def draw(self):
        pass
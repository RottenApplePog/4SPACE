import random

from primitives.shapes.cube import Cube
from primitives.shapes.plane import Plane


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Cube(app,
                 pos=(0, -0.025, 0),
                 scale=(1000, 0.05, 1000),
                 rot=(0, 0, 0),
                 tex_id=(1)
                 ))
        '''
        n, s = 80, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
        '''

    def render(self):
        for obj in self.objects:
            obj.render()

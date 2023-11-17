import random
import pygame as pg

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

        # Translate

        add(Cube(app,
                pos=(0, 0, 0),
                rot=(0, 0, 0),
                scale=(1, 1, 1),
                tex_id=(0),
                movement=[(0, 0, 0), (random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5)), (0, 0, 0)]
                ))

    def render(self):
        for obj in self.objects:
            obj.render()

    def update(self):
        self.scene_events()
        self.render()

    def scene_events(self):
        keys = pg.key.get_pressed()

        app = self.app
        add = self.add_object

        if keys[pg.K_0]:
            for i in range(100):
                add(Cube(app,
                         pos=(0, 0, 0),
                         rot=(0, 0, 0),
                         scale=(1, 1, 1),
                         tex_id=(0),
                         movement=[(0, 0, 0), (random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5)),
                                   (0, 0, 0)]
                         ))

        print(len(self.objects))
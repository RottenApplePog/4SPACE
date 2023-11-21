import random
import pygame as pg

from primitives.shapes.cube import Cube
from primitives.shapes.plane import Plane


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

        self.texture_id = 0

    def add_object(self, obj):
        self.objects.append(obj)

    def destroy_object(self, obj):
        self.objects.remove(obj)

    def load(self):
        app = self.app
        add = self.add_object

        self.texture_id = 0
        self.ready_to_press = True

        # Translate

        add(Cube(app,
                 pos=(0, 0, 0),
                 rot=(0, 0, 0),
                 scale=(1, 1, 1),
                 tex_id=self.texture_id,
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
        destroy = self.destroy_object

        texture_id = self.texture_id
        rtp = self.ready_to_press

        if keys[pg.K_1]:
            if rtp:
                for i in range(1):
                    add(Cube(app,
                             pos=(0, 0, 0),
                             rot=(0, 0, 0),
                             scale=(1, 1, 1),
                             tex_id=texture_id,
                             movement=[(0, 0, 0), (random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5)),
                                       (0, 0, 0)]
                             ))
            self.ready_to_press = False

        elif keys[pg.K_2] and len(self.objects) > 0:
            if rtp:
                destroy(self.objects[0])
                self.ready_to_press = False

        elif keys[pg.K_3]:
            if rtp:
                self.texture_id += 1
                if self.texture_id > 3:
                    self.texture_id = 0
                self.ready_to_press = False

        else:
            self.ready_to_press = True

        print(len(self.objects))
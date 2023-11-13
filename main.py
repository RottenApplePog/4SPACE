import sys

import moderngl as mgl
import pygame as pg

from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from settings import *


class GraphicsEngine:
    def __init__(self):
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.DEPTH_TEST)

        self.clock = pg.time.Clock()
        self.is_running = True

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.light = Light()

        self.camera = Camera(self)

        self.mesh = Mesh(self)

        self.scene = Scene(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def update(self):
        if FPS_CAP == 0:
            self.delta_time = self.clock.tick()
        else:
            self.delta_time = self.clock.tick(FPS_CAP)
        pg.display.set_caption(f"FPS: {self.clock.get_fps() :.0f}")

    def render(self):
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while self.is_running:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.update()


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()

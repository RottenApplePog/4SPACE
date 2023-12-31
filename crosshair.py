import moderngl as mgl

from shader_program import ShaderProgram
from settings import *

import numpy as np
import pygame as pg


class Crosshair:
    def __init__(self, ctx):
        self.ctx = ctx
        self.on_init()
        self.program = ShaderProgram(ctx)

        self.display = pg.Surface(WIN_RES)
        self.display.set_clip(pg.Rect(SCREEN_MID.x, SCREEN_MID.y, 36, 36))

        self.render_object = self.get_render_object(self.program.programs['image'])

    def on_init(self):
        self.quad_buffer = self.ctx.buffer(data=np.array([
            # position (x,y), uv coords (x,y)
            -1.0, 1.0, 0.0, 0.0,   # top left
            1.0, 1.0, 1.0, 0.0,    # top right
            -1.0, -1.0, 0.0, 1.0,  # bottom left
            1.0, -1.0, 1.0, 1.0    # bottom right
        ], 'f'))

        self.cross_1 = pg.image.load('assets/crosshairs/crosshair_0.png')
        self.cross_2 = pg.image.load('assets/crosshairs/crosshair_1.png')
        self.cross_3 = pg.image.load('assets/crosshairs/crosshair_2.png')
        self.cross_4 = pg.image.load('assets/crosshairs/crosshair_3.png')

    def get_render_object(self, program):
        render_object = self.ctx.vertex_array(program, [(self.quad_buffer, '2f 2f', 'vert', 'texcoord')])
        return render_object

    def surface_to_texture(self, surface):
        texture = self.ctx.texture(surface.get_size(), 4)
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        texture.swizzle = 'BGRA'
        texture.write(surface.get_view('1'))

        return texture

    def render(self):
        program = self.program.programs['image']

        self.display.blit(self.cross_4, SCREEN_MID)

        self.texture = self.surface_to_texture(self.display)
        program['tex'] = 0
        self.texture.use()

        self.render_object.render(mode=mgl.TRIANGLE_STRIP)

        self.texture.release()

    def destroy(self):
        self.program.destroy()
        pg.quit()

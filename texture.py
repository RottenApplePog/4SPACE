import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {0: self.get_texture(path='assets/textures/orb.png'),
                         1: self.get_texture(path='assets/textures/test.png'),
                         2: self.get_texture(path='assets/textures/derp.png'),
                         3: self.get_texture(path='assets/textures/orb_32.png'),
                         4: self.get_texture(path='assets/textures/demon.png')}

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
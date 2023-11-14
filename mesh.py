from texture import Texture
from vao import VAO
# from crosshair import Crosshair


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app.ctx)
        # self.crosshair = Crosshair(app.ctx)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()
        self.crosshair.destroy()
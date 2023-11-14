from primitives.vbos.cube import CubeVBO
from primitives.vbos.plane import PlaneVBO


class VBO:
    def __init__(self, ctx):
        self.vbos = {'cube': CubeVBO(ctx),
                     'plane': PlaneVBO(ctx)}

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

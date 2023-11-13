import numpy as np

from primitives.vbos.base import BaseVBO


class PlaneVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, 0, 1), (1, 0, 1), (1, 0, 1), (-1, 0, 1)]

        indices = [(0, 2, 3), (0, 1, 2)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2)]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [(0, 0, 1) * 6]
        normals = np.array(normals, dtype='f4').reshape(6, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

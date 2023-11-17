from model import BaseModel
import glm
from random import randint


class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), movement=None):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        if movement is None:
            self.movement = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        else:
            self.movement = movement
        self.on_init()

    def update(self):
        m_model = self.m_model
        if self.movement[0] != (0, 0, 0):
            m_model = glm.translate(self.m_model, glm.vec3(*self.movement[0]) * self.app.time)  # move cube
        if self.movement[1] != (0, 0, 0):
            m_model = glm.rotate(self.m_model, self.app.time, glm.vec3(*self.movement[1]))  # rotate cube
        if self.movement[2] != (0, 0, 0):
            m_model = glm.scale(self.m_model, glm.vec3(*self.movement[2]) * self.app.time)  # scale cube

        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


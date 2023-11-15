import math

import glm

# screen
WIN_RES = glm.vec2(1000, 563)
SCREEN_MID = glm.vec2(WIN_RES/2-18)
FPS_CAP = 0

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = 0.05

# colors
# BG_COLOR = glm.vec3(0.1, 0.16, 0.25)
BG_COLOR = glm.vec3(0.08, 0.16, 0.18)

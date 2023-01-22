from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

oyna = Ursina()

arm_texture = load_texture("arm_texture")
ovoz_effekt = Audio("punch_sound.wav", loop = False, autoplay = False)

block_check = 1

def update():
    global block_check

    if held_keys["right mouse"] or held_keys["left mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]: block_check = 1
    if held_keys["2"]: block_check = 2
    if held_keys["3"]: block_check = 3
    if held_keys["4"]: block_check = 4


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = "grassblock"):
        super().__init__(
        parent = scene,
        position = position,
        model = "block",
        origin_y = 0.5,
        texture = texture,
        color = color.color(0, 0, random.uniform(0.9, 1)),
        scale = 0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                ovoz_effekt.play()
                if block_check == 1: voxel = Voxel(position = self.position + mouse.normal, texture="grassblock")
                if block_check == 2: voxel = Voxel(position = self.position + mouse.normal, texture="stone_block")
                if block_check == 3: voxel = Voxel(position = self.position + mouse.normal, texture="dirt_block")
                if block_check == 4: voxel = Voxel(position = self.position + mouse.normal, texture="brick_block")

            elif key == "right mouse down":
                ovoz_effekt.play()
                destroy(self)

class Osmon(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = "sky.png",
            scale = 10000,
            double_sided = True,
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
            )
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)

        

for x in range(40):
    for z in range(40):
        voxel = Voxel(position = (x,0,z))

oyinchi = FirstPersonController()
osmon = Osmon()
hand = Hand()

oyna.run()

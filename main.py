from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture("assets/grass.png")
soil_texture = load_texture("assets/soil.png")
stone_texture = load_texture("assets/stone.png")
wood_texture = load_texture("assets/wood.png")

sky_texture = load_texture("assets/sky.png")

current_texture = grass_texture

def update():
    global current_texture
    if held_keys['1']: current_texture = grass_texture
    if held_keys['2']: current_texture = soil_texture
    if held_keys['3']: current_texture = stone_texture
    if held_keys['4']: current_texture = wood_texture

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()



class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            scale=150,
            texture=sky_texture,
            double_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2,0.3),
            color = color.white,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4)
        )

    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.4, -0.4)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            model='cube',
            color=color.white,
            highlight_color=color.lime,
            texture=texture,
            position=position,
            origin_y=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal , texture=current_texture)
            if key == 'right mouse down':
                destroy(self)


for z in range(15):
    for x in range(15):
        voxel = Voxel((x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()

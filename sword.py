import random
from PIL import Image

mask = [
    [2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 0],
    [2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 0],
    [2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2],
    [2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2]
]

default_sword_image = Image.open("sword_without_background.png")


class Sword:
    def __init__(self):
        self.damage = random.randint(0, 9)
        self._fire = random.randint(0, 9)
        self._ground = random.randint(0, 9)
        self._water = random.randint(0, 9)
        self.color = (self._fire * 28, self._ground * 28, self._water * 28, 255)
        self.temp_image = default_sword_image

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] == 1:
                    self.temp_image.putpixel((j, i), self.color)
                if mask[i][j] == 2:
                    self.temp_image.putpixel((j, i), (255, 255, 255, 0))



    def save(self, path):
        self.temp_image.save(path, "png")

    def debug(self):
        self.temp_image.show("debug")
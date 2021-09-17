from PPlay import sprite
from PPlay.gameimage import *

class Tiro(sprite.Sprite):
    vel = 20
    dire = 0
    def init(self, image_file):
        super().init(image_file,frames=1)

    def atualiza_tiro(self,scroll):
        print(self.x)
        self.x += (self.vel * self.dire)

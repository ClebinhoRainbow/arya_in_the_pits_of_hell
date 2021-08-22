from PPlay import sprite

class Tiro(sprite.Sprite):
    vel = 20
    dire = 0
    def init(self, image_file):
        super().init(image_file,frames=1)

    def atualiza_tiro(self):
        self.x += self.vel 

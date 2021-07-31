from PPlay import sprite

class Tiro(sprite.Sprite):
    vel = 170

    def init(self, image_file, position_x, position_y, frames=1):
        super().init(image_file,frames=1)
        self.x = 400
        self.y = 400
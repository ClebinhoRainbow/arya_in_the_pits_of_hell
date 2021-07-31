from PPlay import sprite
from PPlay.window import *

class Plataforma(sprite.Sprite):

    def __init__(self, image_file, position_x, position_y, scale, frames=1 ):
        super().__init__(image_file, frames=1)
        self.image = pygame.transform.scale(self.image ,(int(self.width*scale),int(self.height*scale)) )
        self.x = position_x
        self.y = position_y
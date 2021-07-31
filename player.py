from PPlay import sprite
from PPlay.window import *

class Player(sprite.Sprite):
    vel = 150
    ammo = True
    number_lifes = 3
    item = False
    looking_right = True



    def init(self, image_file, frames=1):
        super().init(image_file,frames=1)

    def move_player(self,teclado,janela):
        keyLeftPressed = teclado.key_pressed("LEFT") and self.x > 0
        if (keyLeftPressed):
            self.x = self.x - self.vel * janela.delta_time()
            self.looking_right = False
            self.flip_player()
        keyRightPressed = teclado.key_pressed("RIGHT") and self.x < janela.width - self.width
        if (keyRightPressed):
            self.x = self.x + self.vel * janela.delta_time()
            self.looking_right = True
            self.flip_player()

    def flip_player(self):
        #TODO
        if(self.looking_right == True):

        else:
            pass

    def jump(self,teclado):
        keyLeftPressed = teclado.key_pressed("SPACE")


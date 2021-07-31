from PPlay import sprite
from PPlay.window import *

class Player(sprite.Sprite):
    vel = 150
    ammo = True
    number_lifes = 3
    item = False
    looking_right = True
    is_jumping = False
    relogio = 0

    def init(self, image_file, frames=1):
        super().init(image_file,frames=1)

    def move_player(self,teclado,janela,plataforma):

        keyPressed = teclado.key_pressed("SPACE")
        if (keyPressed and self.is_jumping == False):
            self.is_jumping = True
        if (self.relogio <= 0.5 and self.is_jumping):
            self.relogio += janela.delta_time()
            self.y -= 200 * janela.delta_time()
        elif (self.collided(plataforma) == False):
            self.relogio += janela.delta_time()
            self.y += 200 * janela.delta_time()
        elif(self.collided(plataforma) == True):
            self.is_jumping = False
            self.relogio = 0





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
            pass
        else:
            pass




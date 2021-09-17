import time
from PPlay import sprite
from tiro import *
from PPlay.window import *


class InimigoVoador(sprite.Sprite):
    # vel = 150
    vida = 1
    # direcao == -1 o inimigo esta indo para cima
    direcao = 1
    looking_up = 1
    # is_jumping = False
    relogio = 0
    died = False

    def init(self, image_file):
        super().init(image_file, frames=1)

    def move_inimigo(self, posInimigoInicialX, posInimigoInicialY,player, janela,scroll):

        for tiro in player.lista_tiros:
            if(self.collided(tiro)):
                self.died = True
                self.hide()
        if(self.died == False):
            if (self.collided(player)):
                player.number_lifes -= .5
            chao = posInimigoInicialY+self.height
            if (self.y + self.height +10 <= chao):

                self.looking_up = False
                self.direcao = 1
            elif (self.y + self.height  >= posInimigoInicialY + 100):
                self.looking_up = True
                self.direcao = -1
            # self.x += (100*self.direcao) * janela.delta_time()
            self.move_y(100 * self.direcao * janela.delta_time())
            self.x += scroll


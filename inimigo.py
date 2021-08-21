import time
from PPlay import sprite
from tiro import *
from PPlay.window import *

class Inimigo(sprite.Sprite):
    #vel = 150
    #ammo = True
    number_lifes = 3
    looking_right = True
    #direcao == 1 o inimigo esta indo para direita
    direcao = 1
    #is_jumping = False
    relogio = 0

    def init(self, image_file, frames=1):
        super().init(image_file, frames=1)

    def move_inimigo(self, playerX, posInimigoInicialX, janela, plataforma):

        if(abs(self.x - playerX) > 80):
            if(posInimigoInicialX + 200 <= self.x):
                if self.looking_right == True:
                    self.flip_inimigo()
                self.looking_right = False
                self.direcao = -1
            elif(self.x  <= posInimigoInicialX):
                if self.looking_right == False:
                    self.flip_inimigo()
                self.looking_right = True
                self.direcao = 1
            # self.x += (100*self.direcao) * janela.delta_time()
            self.move_x(100*self.direcao * janela.delta_time())
        else:
            self.move_x(100)



    def flip_inimigo(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/enemy.png")
            self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/flip-enemy.png")
            self.x += self.width/2

    # def shoot(self,janela,teclado):
    #     lista_tiro = []
    #     cooldown = 0
    #     delta_0 = 0
    #     delta_1 = 0
    #
    #     cooldown = delta_1 - delta_0
    #     delta_1 = time.time()
    #     if (teclado.key_pressed("SPACE")   ):
    #         delta_0 = time.time()
    #         #Instancia tiro
    #
    #         novo_tiro = Tiro("tiro.png")
    #         lista_tiro.append(novo_tiro)



        # for tiro in lista_tiro:
        #     tiro.set_position(tiro.x + tiro.vel, tiro.y)
        #     if (tiro.x > janela.width):
        #         lista_tiro.pop(0)
        #     tiro.draw()
        #
        #
        #
        #
        # print(lista_tiro)




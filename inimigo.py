import time
from PPlay import sprite
from tiro import *
from PPlay.window import *

class Inimigo(sprite.Sprite):
    #vel = 150
    vida = 3
    ammo = True
    lista_tiro = []
    number_lifes = 3
    looking_right = True
    #direcao == 1 o inimigo esta indo para direita
    direcao = 1
    #is_jumping = False
    relogio = 0
 
    def init(self, image_file):
        super().init(image_file, frames=1)

    def move_inimigo(self, playerX, posInimigoInicialX, janela):

        
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
        



    def flip_inimigo(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/enemy.png")
            self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/flip-enemy.png")
            self.x += self.width/2

    def shoot(self,janela,player,scroll):

        if self.ammo:
            tiro = Tiro("assets/fire-ball-big.png",2)
            tiro.set_sequence_time(0,2,300)
            tiro.y = self.y + 10
            tiro.vel = 2
            if player.x < self.x:
                tiro.x = self.x - tiro.width
                tiro.dire = -1
            else:
                tiro.x = self.x + self.width
                tiro.dire = 1
            self.lista_tiro.append(tiro)
            self.ammo = False
        for t in self.lista_tiro:
            t.atualiza_tiro(scroll)
            if player.y < t.y and player.y + player.height > t.y:
                if t.collided(player):
                    print("colidiu")
                    self.lista_tiro.pop(0)
                    player.number_lifes -= 1
                    self.ammo = True
            if t.x < 0 :
                self.lista_tiro.pop(0)
                self.ammo = True
            t.update()
            t.draw()
        
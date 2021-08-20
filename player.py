import time
from PPlay import sprite
from tiro import *
from PPlay.window import *
from PPlay import gameimage
class Player(sprite.Sprite):
    vel = 150
    vel_y = 0
    ammo = True
    number_lifes = 3
    item = False
    looking_right = True
    is_jumping = False
    relogio = 0

    def init(self, image_file):
        super().init(image_file, frames=1)
        self = pygame.transform.scale(self, (int(self.width * 3), int(self.height * 3)))
        
        # self.width = self.image.get_rect().width
        # self.height = self.image.get_rect().height

    def move_player(self,teclado,janela,plataforma):
        #fisica do salto
        keyPressed = teclado.key_pressed("UP")
        if (keyPressed and self.is_jumping == False):
            self.is_jumping = True
            self.vel_y = -11

        
        self.vel_y += 30 * janela.delta_time()
        print(self.vel_y)
        if self.y + self.vel_y + self.height +10 >= plataforma.y:
            self.y = plataforma.y - self.height
            self.is_jumping = False
        else: 
            self.y += self.vel_y


        # fisica de movimento
        keyLeftPressed = teclado.key_pressed("LEFT") and self.x > 0
        if (keyLeftPressed):
            self.x = self.x - self.vel * janela.delta_time()
            if self.looking_right == True:
                self.flip_player()
            self.looking_right = False

        keyRightPressed = teclado.key_pressed("RIGHT") and self.x < janela.width - self.width
        if (keyRightPressed):
            self.x = self.x + self.vel * janela.delta_time()
            if self.looking_right == False:
                self.flip_player()
            self.looking_right = True




    def flip_player(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/flip-arya.png")
            self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/arya.png")
            self.x += self.width/2
            pass

    def shoot(self,janela,teclado):
        lista_tiro = []
        cooldown = 0
        delta_0 = 0
        delta_1 = 0

        cooldown = delta_1 - delta_0
        delta_1 = time.time()
        if (teclado.key_pressed("SPACE")   ):
            delta_0 = time.time()
            #Instancia tiro

            novo_tiro = Tiro("assets/tiro.png")
            lista_tiro.append(novo_tiro)



        for tiro in lista_tiro:
            tiro.set_position(tiro.x + tiro.vel, tiro.y)
            if (tiro.x > janela.width):
                lista_tiro.pop(0)
            tiro.draw()


    def show_hud(self):
        if(self.item):
            #drawItem
            pass
        if(self.ammo):
            #subtract the number of bullets
            pass
        #Pegar codigo do Space Invaders, matriz
        hud = gameimage.GameImage("./assets/hud.png")
        hud.set_position(25, 25)
        hud.draw()






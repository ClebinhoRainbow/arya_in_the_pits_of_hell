import time
from PPlay import sprite
from tiro import *
from PPlay.window import *
from PPlay import gameimage
class Player(sprite.Sprite):
    vel = 150
    ammo = True
    number_lifes = 3
    item = False
    looking_right = True
    is_jumping = False
    relogio = 0

    def init(self, image_file):
        super().init(image_file, frames=1)
        self.image = pygame.transform.scale(image_file, (int(image_file.get_width()*2), int(image_file.get_height()*2)))
        # self.width = self.image.get_rect().width
        # self.height = self.image.get_rect().height

    def move_player(self,teclado,janela,plataforma):
        #fisica do salto
        keyPressed = teclado.key_pressed("UP")
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




        # fisica de movimento
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






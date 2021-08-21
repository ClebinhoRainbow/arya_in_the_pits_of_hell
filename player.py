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
    lista_tiros = []
    delta_1 = time.time()
    delta_0 = time.time()
    shoot_rate = 0.75

    def init(self, image_file):
        super().init(image_file, frames=1)
        self = pygame.transform.scale(self, (int(self.width * 3), int(self.height * 3)))
        
        # self.width = self.image.get_rect().width
        # self.height = self.image.get_rect().height
    def altera_stripe_de_movimento(self):
        print("oi")
    def move_player(self,teclado,janela,plataforma):

        #fisica do salto
        keyPressed = teclado.key_pressed("UP")
        if (keyPressed and self.is_jumping == False):
            self.is_jumping = True
            self.vel_y = -11

        
        self.vel_y += 30 * janela.delta_time()
        if self.y + self.vel_y + self.height +10 >= plataforma.y:
            self.y = plataforma.y - self.height
            self.is_jumping = False
        else: 
            self.y += self.vel_y


        # fisica de movimento
        keyLeftPressed = teclado.key_pressed("LEFT") and self.x > 0
        if (keyLeftPressed):

            self.set_initial_frame(2)
            self.set_final_frame(5)
            #self.update()
            self.x = self.x - self.vel * janela.delta_time()
            if self.looking_right == True:
                self.flip_player()
            self.looking_right = False

        keyRightPressed = teclado.key_pressed("RIGHT") and self.x < janela.width - self.width
        #tecla = teclado.show_key_pressed()
        if (keyRightPressed):
            #print(tecla)
            self.set_initial_frame(2)
            self.set_final_frame(5)
            #self.update()
            self.x = self.x + self.vel * janela.delta_time()
            if self.looking_right == False:
                self.flip_player()
            self.looking_right = True


    def flip_player(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/idle2.png")
            self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/idle.png")
            self.x += self.width/2
            pass

    def shoot(self,janela,teclado):

        altura_arma = self.y + 15
        distancia_inicial_tiro = self.x + 100
        self.delta_1 = time.time()
        cooldown = self.delta_1 - self.delta_0
        print(cooldown)
        if (teclado.key_pressed("SPACE")   and cooldown > self.shoot_rate ):
            self.delta_0 = time.time()
            #Instancia tiro
            novo_tiro = Tiro("assets/tiro.png")
            novo_tiro.set_position(distancia_inicial_tiro, altura_arma)
            self.lista_tiros.append(novo_tiro)



        for tiro in self.lista_tiros:
            if (tiro.x > janela.width):
                self.lista_tiros.pop(0)
                continue
            tiro.set_position(tiro.x+10,tiro.y)
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
    def decrease_life(self):
        self.number_lifes -= 1

    def colidiu(self, list_of_monsters, list_of_enemy_fire):
        for monster in list_of_monsters:
            if(self.colidiu(monster)):
                self.decrease_life()

        # for fire in list_of_enemy_fire:
        #     if(self.colidiu(fire)):
        #         self.decrease_life()






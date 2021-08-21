import time
from pygame.transform import set_smoothscale_backend
from PPlay import sprite
from tiro import *
from PPlay.window import *
from PPlay.sound import *
from PPlay import gameimage
efx = Sound("assets/shoot.ogg")
class Player(sprite.Sprite):
    vel = 150
    vel_y = 0
    ammo = True
    number_lifes = 3
    item = False
    looking_right = True
    is_jumping = False
    relogio = 0
<<<<<<< HEAD
    action = 0
=======
>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904
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
<<<<<<< HEAD
        
=======
>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904
        if self.y + self.vel_y + self.height +10 >= plataforma.y:
            self.y = plataforma.y - self.height
            self.is_jumping = False
        else: 
            self.y += self.vel_y

        #print(self.get_curr_frame())
        if not self.is_looping():
            print('parou')
        if not self.is_playing():
            print('stoped')
        # fisica de movimento
        keyLeftPressed = teclado.key_pressed("LEFT") and self.x > 0
<<<<<<< HEAD
        keyRightPressed = teclado.key_pressed("RIGHT") and self.x < janela.width - self.width
        if (keyLeftPressed or keyRightPressed):
            
            if (keyLeftPressed):
                self.x = self.x - self.vel * janela.delta_time()
                self.looking_right = False
                self.flip_player()
            if (keyRightPressed):
                self.x = self.x + self.vel * janela.delta_time()
                self.looking_right = True
                self.flip_player()
            self.upd_action(1)
        else:
            self.upd_action(0)
        
          
    def upd_action(self, new_action):
        if self.action != new_action:
            if new_action == 1:
                self.set_sequence_time(2,6,160)
            if new_action == 0:
                print("passou")
                self.set_sequence_time(0,2,400)
            self.action = new_action
=======
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

>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904

    def flip_player(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/sprite.png")
            #self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/sprite1.png")
            #self.x += self.width/2
            pass

    def shoot(self,janela,teclado):
<<<<<<< HEAD
        lista_tiro = []
        cooldown = 0
        altura_arma = self.y + 15
        if self.looking_right:
            distancia_inicial_tiro = self.x + 50
        else:
            distancia_inicial_tiro = self.x

        self.delta_1 = time.time()
        cooldown = self.delta_1 - self.delta_0
        if (teclado.key_pressed("SPACE")   and cooldown > self.shoot_rate ):
            efx.play()
            self.delta_0 = time.time()
            #Instancia tiro
            novo_tiro = Tiro("assets/tiro.png")
            if self.looking_right:
                novo_tiro.dire = 1
            else:
                novo_tiro.dire = -1
            novo_tiro.set_position(distancia_inicial_tiro, altura_arma)
            
=======

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
>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904
            self.lista_tiros.append(novo_tiro)



        for tiro in self.lista_tiros:
<<<<<<< HEAD
            tiro.x = tiro.x + (tiro.vel * tiro.dire)
            if (tiro.x > janela.width or tiro.x < 0):
                self.lista_tiros.pop(0)
                continue
            #tiro.set_position(tiro.x+5,tiro.y)
=======
            if (tiro.x > janela.width):
                self.lista_tiros.pop(0)
                continue
            tiro.set_position(tiro.x+10,tiro.y)
>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904
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






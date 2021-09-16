import time
from pygame.transform import set_smoothscale_backend
from PPlay import sprite
from tiro import *
from PPlay.window import *
from PPlay.sound import *
from PPlay import gameimage
efx = Sound("assets/audio/shoot.ogg")
SCROLL_THRESH = 200
class Player(sprite.Sprite):
    vel = 5
    vel_y = 0
    ammo = True
    muni = 10
    total_life = 50
    number_lifes = 50
    item = True
    looking_right = True
    is_jumping = False
    relogio = 0
    action = 0
    lista_tiros = []
    delta_1 = time.time()
    delta_0 = time.time()
    shoot_rate = 0.75
    falling = False
    def init(self, image_file):
        super().init(image_file, frames=1)
        self = pygame.transform.scale(self, (int(self.width * 3), int(self.height * 3)))
        
        # self.width = self.image.get_rect().width
        # self.height = self.image.get_rect().height
    def altera_stripe_de_movimento(self):
        print("oi")

    def move_player(self,teclado,janela,plataforma):
        screen_scroll = 0
        #fisica do salto
        keyPressed = teclado.key_pressed("UP")
        if (keyPressed and self.is_jumping == False):
            self.is_jumping = True
            self.vel_y = -20

        
        self.vel_y += 30 * janela.delta_time()
        
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
        keyRightPressed = teclado.key_pressed("RIGHT") and self.x < janela.width - self.width
        if (keyLeftPressed or keyRightPressed):
            if (keyLeftPressed):
                self.x = self.x - self.vel
                self.looking_right = False
                self.flip_player()
            if (keyRightPressed):
                self.x = self.x + self.vel
                self.looking_right = True
                self.flip_player()
            self.upd_action(1)
        else:
            self.upd_action(0)

        if self.x + self.width > 800 - SCROLL_THRESH:
            self.x -= self.vel
            screen_scroll = -self.vel 
        elif self.x < 100:
            self.x += self.vel
            screen_scroll = self.vel 
        return screen_scroll
          
    def upd_action(self, new_action):
        if self.action != new_action:
            if new_action == 1:
                self.set_sequence_time(2,6,160)
            if new_action == 0:
                print("passou")
                self.set_sequence_time(0,2,400)
            self.action = new_action

    def flip_player(self):
        #TODO
        if(self.looking_right == True):
            self.image = pygame.image.load("assets/sprite.png")
            #self.x -= self.width/2
        else:
            self.image = pygame.image.load("assets/sprite1.png")
            #self.x += self.width/2
            pass

    def shoot(self,janela,teclado,lInimigos):
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
            self.muni -= 1
            self.delta_0 = time.time()
            #Instancia tiro
            novo_tiro = Tiro("assets/tiro.png")
            if self.looking_right:
                novo_tiro.dire = 1
            else:
                novo_tiro.dire = -1
            novo_tiro.set_position(distancia_inicial_tiro, altura_arma)
            
            self.lista_tiros.append(novo_tiro)



        for tiro in self.lista_tiros:
            tiro.x = tiro.x + (tiro.vel * tiro.dire)
            for x in lInimigos:
                if tiro.collided(x):
                    self.lista_tiros.pop(0)
                    lInimigos.remove(x)
            if (tiro.x > janela.width or tiro.x < 0):
                self.lista_tiros.pop(0)
                continue
            #tiro.set_position(tiro.x+5,tiro.y)
            tiro.draw()


    def show_hud(self, screen):
        hud = GameImage("assets/Hudd.png")
        hud.set_position(25, 25)
        hud.draw()
        ratio = self.number_lifes / self.total_life
        pygame.draw.rect(screen, (0,255,0), (29, 33, 115*ratio, 8))
        if(self.item):
            #drawItem
            item = GameImage("assets/item.png")
            item.set_position(178,33)
            item.draw()
        if(self.ammo):
            #subtract the number of bullets
            for x in range(self.muni):
                bullet = GameImage("assets/ammo.png")
                bullet.set_position(29 +( bullet.width * (x*1.5)) , 50 )
                bullet.draw()
        
    def decrease_life(self):
        self.number_lifes -= 1

    def colidiu(self, list_of_monsters, list_of_enemy_fire):
        for monster in list_of_monsters:
            if(self.colidiu(monster)):
                self.decrease_life()

        # for fire in list_of_enemy_fire:
        #     if(self.colidiu(fire)):
        #         self.decrease_life()



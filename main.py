from world import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from plataforma import *
from inimigo import *
from PPlay.sound import *
import csv

#inicializacao

janela = Window(800, 600)
janela.set_title("Arya in the pits of hell")
teclado = Window.get_keyboard()
musica = Sound("assets/audio/hellOST.ogg")
#efx = Sound()
clock = pygame.time.Clock()
FPS = 60
mouse = Window.get_mouse()
#musica.play()

# enemy_1 = Sprite("inimigo.png",1)


# player = Player("arya.png", 50, 401)
world_data = []
for row in range(20):
    r = [0] * 60
    world_data.append(r)

with open("assets/fase.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
world.processa_dado(world_data)

player = Player("assets/sprite.png",6)
player.set_sequence_time(0,2,400)
inimigo1 = Inimigo("assets/flip-enemy.png")
inimigo2 = Inimigo("assets/flip-enemy.png")
player.set_position(110,401)
inimigo1.set_position(400, 401)
inimigo2.set_position(700,251)
plataforma = Plataforma("assets/plataforma.png", 45, 480, 1)
plataforma2 = Plataforma("assets/plataforma.png", 245, 480, 1)
plataforma3 = Plataforma("assets/plataforma.png", 445, 480, 1)
plataforma4 = Plataforma("assets/plataforma.png", 600, inimigo2.y + inimigo2.height, 1)
lista_de_inimigos = []
lista_de_inimigos.append(inimigo1)
lista_de_inimigos.append(inimigo2)

def game():
    musica.play()
    while (True):
        clock.tick(FPS)
        # Update dos Game Objects

        #Games Physics
        scroll = player.move_player(teclado, janela,plataforma)
        inimigo1.move_inimigo(player.x,400, janela,plataforma)
        inimigo2.move_inimigo(player.x,700,janela,plataforma)

        #Desenho dos Game Objects
        janela.set_background_color([43, 16, 41])
        world.desenha(janela, scroll)
        player.show_hud(janela.screen)
        for inimigo in lista_de_inimigos:
            inimigo.draw()
            inimigo.shoot(janela, player)
        player.update()
        player.draw()
        player.shoot(janela, teclado, lista_de_inimigos)
        janela.draw_text("Life: " + str(player.number_lifes), 580, 20, size=16, color=(255, 255, 255),
                            font_name="Arial",
                            bold=False, italic=False)
        plataforma.draw()
        plataforma2.draw()
        plataforma3.draw()
        plataforma4.draw()
        print(mouse.get_position())
        janela.update()
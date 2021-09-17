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
player.set_position(80,401)
inimigo1.set_position(400, 401)
inimigo2.set_position(700,251)

lista_de_inimigos = []


lista_de_obstaculos = world.get_lista_de_obstaculos()

lista_de_inimigos = world.get_lista_de_inimigos()


def game():
    musica.play()
    while (True):
        clock.tick(FPS)
        # Update dos Game Objects

        #Games Physics

        scroll,scrollY = player.move_player(teclado, janela,lista_de_obstaculos)

        # inimigo1.move_inimigo(lista_de_obstaculos[0][0],375, janela)
        # inimigo2.move_inimigo(lista_de_obstaculos[0][1],700,janela)

        #Desenho dos Game Objects
        janela.set_background_color([43, 16, 41])
        world.desenha(janela, scroll,scrollY)
        player.show_hud(janela.screen)
        player.colisao_com_plataforma(lista_de_obstaculos)
        print(len(lista_de_inimigos))
        for inimigo in lista_de_inimigos:
            # #inimigo.move_inimigo()
            inimigo.draw()
            inimigo.shoot(janela, player)
        player.update()
        player.draw()
        player.shoot(janela, teclado, lista_de_inimigos)
        janela.draw_text("Life: " + str(player.number_lifes), 580, 20, size=16, color=(255, 255, 255),
                            font_name="Arial",
                            bold=False, italic=False)

        player.save_ultima_posicao_segura(janela)
        #print(mouse.get_position())
        janela.update()




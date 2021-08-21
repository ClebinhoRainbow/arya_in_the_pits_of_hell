from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from plataforma import *
from inimigo import *
from  PPlay.sound import *
#inicializacao

janela = Window(800, 600)
janela.set_title("Arya in the pits of hell")
teclado = Window.get_keyboard()
#musica = Sound("assets/hellOST.ogg")
clock = pygame.time.Clock()
FPS = 60


#musica.play()

# enemy_1 = Sprite("inimigo.png",1)


# player = Player("arya.png", 50, 401)
player = Player("assets/sprite.png",6)
player.set_sequence_time(0,2,400)
inimigo = Inimigo("assets/flip-enemy.png")
inimigo2 = Inimigo("assets/flip-enemy.png")
player.set_position(50,401)
inimigo.set_position(400, 401)
inimigo2.set_position(700,251)
plataforma = Plataforma("assets/plataforma.png", 45, 480, 1)
plataforma2 = Plataforma("assets/plataforma.png", 245, 480, 1)
plataforma3 = Plataforma("assets/plataforma.png", 445, 480, 1)
plataforma4 = Plataforma("assets/plataforma.png", 600, inimigo2.y + inimigo2.height, 1)
lista_de_inimigos = []
lista_de_inimigos.append(inimigo)
lista_de_inimigos.append(inimigo2)


while (True):
    clock.tick(FPS)
    #entrad de dados

    # Update dos Game Objects

    # janela.draw_text("OI", 200, 200, size=32, color=(255, 255, 255))
  
    #Games Physics
    
    player.move_player(teclado, janela,plataforma)
    inimigo.move_inimigo(player.x,400, janela,plataforma)
    inimigo2.move_inimigo(player.x,700,janela,plataforma)

    #Placar

    #Desenho dos Game Objects

    janela.set_background_color([43, 16, 41])
    player.show_hud()
    inimigo.draw()
    inimigo2.draw()
    player.update()
    player.draw()
    player.shoot(janela, teclado)
    janela.draw_text("Life: " + str(player.number_lifes), 580, 20, size=16, color=(255, 255, 255),
                          font_name="Arial",
                          bold=False, italic=False)
    plataforma.draw()
    plataforma2.draw()
    plataforma3.draw()
    plataforma4.draw()
    janela.update()
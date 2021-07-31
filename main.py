from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from plataforma import  *
#inicializacao

janela = Window(800, 600)
janela.set_title("Arya in the pits of hell")
teclado = Window.get_keyboard()


background = GameImage("background.png")

# enemy_1 = Sprite("enemy.png",1)

plataforma = Plataforma("plataforma.png", 45, 480, 1)
player = Player("arya.png")


player.set_position(50, 401)
while (True):

    #entrad de dados

    # Update dos Game Objects

    # janela.draw_text("OI", 200, 200, size=32, color=(255, 255, 255))
  
    #Games Physics
    
    player.move_player(teclado, janela,plataforma)
    #Placar

    #Desenho dos Game Objects



    background.draw()
    player.draw()
    plataforma.draw()
    janela.update()
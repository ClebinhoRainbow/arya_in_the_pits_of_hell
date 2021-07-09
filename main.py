from PPlay.window import *
from PPlay.gameimage import*
from PPlay.sprite import*
#inicializacao

janela = Window(800,600)
janela.set_title("Arya in the pits of hell")
teclado = Window.get_keyboard()

player = Sprite("Arya.png",1)
background = GameImage("bg-image.png")
# bola = Sprite('bola de fogo.png',1)
# padE = Sprite ("pad.png",1)
# padD = Sprite ("pad.png",1)

enemy_1 = Sprite("enemy.png",1)
# posicao_x_bola = janela.width/2 -bola.width/2
# posicao_y_bola = janela.height/2 - bola.height/2
# bola.set_position(posicao_x_bola,posicao_y_bola)

# pontuacaoE = 0
# pontuacaoD = 0

# padE.x = 5
# padE.y = janela.height/2 - padE.height/2
# padD.x = janela.width - padD.width - 5
# padD.y = janela.height/2 - padD.height/2

# velPad = 200
# velocidadeX = 200
# velocidadeY = 200
#Game Loop
while (True):
    #entrad de dados

    # Update dos Game Objects

    # janela.draw_text("OI", 200, 200, size=32, color=(255, 255, 255))
  
    #Games Physics
    

    #Placar

    #Desenho dos Game Objects
 
   
    janela.update()
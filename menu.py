from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *
import main
holder = Sound("assets/audio/holder.ogg")
select = Sound("assets/audio/select.ogg")
windows = Window(800, 600)
mouse = Window.get_mouse()
fundo = GameImage("assets/placeHolder.jpg")
cur = 0
while True:
    if mouse.is_over_area([80,210],[200, 235]):
        if cur != 1:
            holder.play()
            cur = 1
        if mouse.is_button_pressed(1):
            holder.stop()
            select.play()
            main.game()
    elif mouse.is_over_area([110,325],[170, 355]):
        if cur != 2:
            holder.play()
            cur = 2
        if mouse.is_button_pressed(1):
            windows.close()
    else:
        cur = 0
    fundo.draw()
    windows.update()

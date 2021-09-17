import PPlay
from PPlay.gameimage import *
import pygame
from pygame.locals import *
from inimigo import  *

TILE_SIZE = 64

img_list = []
for x in range(19):
    img = pygame.image.load(f'assets/tiles/{x}.png')
    img_list.append(img)
    
class World():
    def __init__(self):
        self.obstacle_list = []
        self.decoration_list = []
        self.lista_inimigos = []
    
    def processa_dado(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                if tile == 1 or tile == 2  or tile == 5  or tile == 6  or tile == 14 or tile == 17:
                    self.obstacle_list.append(tile_data)
                elif tile == 4:
                    novo_inimigo = Inimigo("./assets/inimigo.png")
                    print(f'tile {tile_data}')
                    novo_inimigo.set_position(tile_data[1][0],tile_data[1][1]-64+novo_inimigo.height/2)
                    #novo_inimigo.set_position(400, 401)

                    self.decoration_list.append(tile_data)
                    self.lista_inimigos.append(novo_inimigo)
                else:
                    self.decoration_list.append(tile_data)

                #1,2,5,6,14

    def desenha(self, janela, scroll,scroll_Y):
        for tile in self.obstacle_list:
            tile[1][0] += scroll
            tile[1][1]+= scroll_Y
            janela.screen.blit(tile[0],tile[1])

        for tile in self.decoration_list:

            tile[1][0] += scroll
            tile[1][1] += scroll_Y
            janela.screen.blit(tile[0],tile[1])



    def get_lista_de_obstaculos(self):
        return self.obstacle_list

    def get_lista_de_inimigos(self):
        return self.lista_inimigos
    def get_decoration_list(self):
        return self.decoration_list
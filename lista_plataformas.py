from PPlay import sprite
class ListaPlataforma(sprite.Sprite):
    def __init__(self):
        self.lista_plataformas = []
    def add_plataforma(self,plataforma):
        self.lista_plataformas.append(plataforma)
    def remove_plataforma(self):
        self.lista_plataformas.pop(0)
    def move_plataformas_esquerda(self):
        for plataforma in range(self.lista_plataformas):

    def move_plataformas_direita(self):
        pass
    def desenha_plataformas(self):
        pass


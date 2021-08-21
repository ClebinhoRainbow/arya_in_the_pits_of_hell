from PPlay import sprite

class Tiro(sprite.Sprite):
    vel = 20
    dire = 0
    def init(self, image_file):
        super().init(image_file,frames=1)
<<<<<<< HEAD

    def atualiza_tiro(self):
        self.x += self.vel 
=======
        self.x = 400
        self.y = 400
    def atualiza_tiro(self):
        self.x += self.vel
>>>>>>> dfcdf68ee67e27675ea48cea0f684879feb02904

from PPlay import sprite


class HealthPack(sprite.Sprite):
    def init(self, image_file):
        super().init(image_file, frames=1)
        self.usado = False
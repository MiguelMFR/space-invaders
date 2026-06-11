import config
import sprites as sprite

class Bala:

    def __init__(self, x, y, velocidade, imagem, frames=1, animar=False):
        self.sprite = sprite.Sprite(imagem, frames)
        self.sprite.set_position(x, y)
        self.velocidade = velocidade
        self.animar = animar

        if animar:
            self.sprite.set_total_duration(800)
            self.sprite.set_loop(True)
            self.sprite.set_sequence(0, frames-1, True)

    def atualizar(self, dt):
        self.sprite.move_y(self.velocidade * dt)
            
        if self.animar:
            self.sprite.update()

        self.sprite.draw()

    def fora_da_tela(self):
        return (
            self.sprite.y < -self.sprite.height or
            self.sprite.y > config.window.height
        )

    def colide(self, outro_sprite):
        return (
            self.sprite.x < outro_sprite.x + outro_sprite.width and
            self.sprite.x + self.sprite.width > outro_sprite.x and
            self.sprite.y < outro_sprite.y + outro_sprite.height and
            self.sprite.y + self.sprite.height > outro_sprite.y
        )
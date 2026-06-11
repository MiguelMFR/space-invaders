import sprites as sprite
from classes.Bala import Bala

class Monstro:

    def __init__(self, x, y, imagem_monstro, imagem_tiro):
        self.imagem_tiro = imagem_tiro
        self.sprite = sprite.Sprite(imagem_monstro, 4)
        self.sprite.set_total_duration(800)
        self.sprite.set_loop(True)
        self.sprite.set_sequence(0, 3, True)
        self.sprite.set_position(x, y)

    def atualizar(self, velocidade):
        self.sprite.move_x(velocidade)
        self.sprite.update()  
        self.sprite.draw()
    
    def atirar(self):
            return Bala(
                self.sprite.x + self.sprite.width/2,
                self.sprite.y + self.sprite.height,
                300,
                self.imagem_tiro,
                frames=5,
                animar=True
            )

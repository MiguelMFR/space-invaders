import config
import sprites as sprite
import sound
from classes.Bala import Bala

class Nave:
    def __init__(self):
        self.sprite = sprite.nave
        self.sprite.set_position(
            config.window.width/2 - self.sprite.width/2,
            config.window.height - self.sprite.height
        )
        self.vida = config.vida
        self.balas: list[Bala] = []
        self.tempo_tiro = 0
        self.intervalo_tiro = config.tiro_nave[config.modo_dificuldade]
        self.velocidade = config.velocidade_nave[config.modo_dificuldade]
        self.imunidade = False
        self.tempo_imunidade = 0

    def posicionar(self):
        self.sprite.set_position(
            config.window.width/2 - self.sprite.width/2,
            config.window.height - self.sprite.height
        )

    def atualizar(self, dt):
        self.movimento()
        self.atirar(dt)
        self.atualizar_balas(dt)
        if self.imunidade:
            self.tempo_imunidade += dt

            if int(self.tempo_imunidade * 10) % 2 == 0:
                self.sprite.draw()

            if self.tempo_imunidade > 3:
                self.imunidade = False
                self.tempo_imunidade = 0
        else:
            self.sprite.draw()

    def movimento(self):
        if config.keyboard.key_pressed("LEFT") and self.sprite.x > 0:
            self.sprite.move_x(-self.velocidade * config.window.delta_time())

        if config.keyboard.key_pressed("RIGHT") and self.sprite.x < config.window.width - self.sprite.width:
            self.sprite.move_x(self.velocidade * config.window.delta_time())

    def atirar(self, dt):
        self.tempo_tiro += dt

        if config.keyboard.key_pressed("SPACE") and self.tempo_tiro >= self.intervalo_tiro:
            sound.som_tiro.play()
            bala = Bala(
                self.sprite.x + self.sprite.width/2,
                self.sprite.y,
                -500,  
                "images/nave_tiro.png",
                frames=1,
                animar=False
            )
            
            self.balas.append(bala)
            self.tempo_tiro = 0

    def atualizar_balas(self, dt):
        for bala in self.balas[:]:
            bala.atualizar(dt)
            if bala.fora_da_tela():
                self.balas.remove(bala)
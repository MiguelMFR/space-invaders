import config
from classes.Bala import Bala
from classes.Monstro import Monstro
import random
import sprites as sprite

class GrupoMonstros:
    def __init__(self):
        self.monstros: list[Monstro] = []
        self.altura_monstro = sprite.polvo.height if sprite.polvo.height > sprite.caranguejo.height else sprite.caranguejo.height
        self.largura_monstro = sprite.polvo.width/4 if sprite.polvo.width > sprite.caranguejo.width else sprite.caranguejo.width/4
        self.balas: list[Bala] = []
        self.velocidade = config.velocidade_monstros[config.modo_dificuldade]
        self.cronometro = 0

    def criar_linhas(self, linha, coluna, imagens):
        self.monstros.clear()
        self.balas.clear()
        self.velocidade = config.velocidade_monstros[config.modo_dificuldade]
        self.cronometro = 0

        for linha in range(linha):
            for i in range(coluna):
                monstro_largura = self.largura_monstro
                x = i * (monstro_largura + monstro_largura/2)
                y = linha * (self.altura_monstro + self.altura_monstro/2)

                if linha % 2 == 0:
                    monstro = Monstro(x, y, imagens[0], "images/tiro_caranguejo.png")
                else:
                    monstro = Monstro(x, y, imagens[1], "images/tiro_caranguejo.png")

                self.monstros.append(monstro)
                
    def atualizar(self, dt):
        self.movimento(dt)
        self.atirar(dt)
        self.atualizar_balas(dt)

    def movimento(self, dt):
        inverter = False

        for monstro in self.monstros:
            monstro.atualizar(self.velocidade * dt )

            if monstro.sprite.x <= 0 or monstro.sprite.x + monstro.sprite.width >= config.window.width:
                inverter = True

        if inverter:
            monstro.sprite.x = max(0, min(monstro.sprite.x, config.window.width - monstro.sprite.width))
            self.velocidade *= -1

            for monstro in self.monstros:
                monstro.sprite.move_y(monstro.sprite.height/2)

    def atirar(self, dt):
        self.cronometro += dt

        if self.cronometro >= config.tiro_monstro[config.modo_dificuldade] and self.monstros:
            monstro = random.choice(self.monstros)

            bala = monstro.atirar()  
            self.balas.append(bala)

            self.cronometro = 0

    def atualizar_balas(self, dt):
        for bala in self.balas[:]:
            bala.atualizar(dt)
            if bala.fora_da_tela():
                self.balas.remove(bala)

import sprites as sprite
import config
from classes.Nave import Nave
from classes.GrupoMonstros import GrupoMonstros

class Game:
    def __init__(self):
        self.nave = Nave()
        self.monstros = GrupoMonstros()
        self.linhas = 3
        self.colunas = 5
        self.fps_cnt = 0
        self.fps_tempo = 0
        self.fps = 0
        self.combo = 0
        self.cnt_monstros_mortos = 0
        self.pontos = 0
        self.game_over = False

    def iniciar(self):
        self.monstros.criar_linhas(self.linhas, self.colunas, ["images/polvo.png", "images/caranguejo.png"])

    def atualizar(self):
        dt = config.window.delta_time()
        self.cnt_monstros_mortos += dt
        self.fps_cnt += 1
        self.fps_tempo += dt

        if self.fps_tempo >= 1:
            self.fps = self.fps_cnt / self.fps_tempo
            self.fps_cnt = 0
            self.fps_tempo = 0

        sprite.background_jogo.draw()

        if self.game_over:
            return

        self.nave.atualizar(dt)
        self.monstros.atualizar(dt)
        self.mostrar_vida()
        self.verificar_colisoes()

        self.verificar_fim_jogo()

        config.window.draw_text(f"FPS: {self.fps:.2f}", 10, 10, 20, color="white")    
        config.window.draw_text(f"Pontos: {self.pontos}", 10, 40, 20, color="white")

    def mostrar_vida(self):
        for i in range(self.nave.vida):
            sprite.vida.set_position(config.window.width - (sprite.vida.width+10)* (i+1), 10)
            sprite.vida.draw()

    def verificar_fim_jogo(self):
        if not self.monstros.monstros:
            self.linhas += 1
            self.colunas += 2  
            self.iniciar()
            return

        if self.nave.vida <= 0 or any(monstro.sprite.y + monstro.sprite.height/2 >= self.nave.sprite.y for monstro in self.monstros.monstros):
            self.monstros.monstros.clear()
            self.monstros.balas.clear()
            self.nave.balas.clear()
            self.game_over = True

    def verificar_colisoes(self):
  
        for bala in self.nave.balas[:]:
            for monstro in self.monstros.monstros[:]:
                if bala.colide(monstro.sprite):

                    self.nave.balas.remove(bala)
                    self.monstros.monstros.remove(monstro)

                    # Se matou rápido, aumenta o combo
                    if self.cnt_monstros_mortos < 2:
                        self.combo += 1
                    else:
                        self.combo = 1

                    # Limita o combo para não ficar absurdo
                    self.combo = min(self.combo, 10)

                    # Pontuação
                    self.pontos += 10 * self.combo

                    # Reinicia o contador de tempo
                    self.cnt_monstros_mortos = 0

                    break

        if not self.monstros.monstros:
            self.monstros.balas.clear()
            return

        if self.nave.imunidade:
            return
        
        for bala in self.monstros.balas[:]:

            if bala.colide(self.nave.sprite):
                self.nave.imunidade = True
                self.nave.posicionar()
                self.nave.vida -= 1
                config.vida -= 1
                self.monstros.balas.remove(bala)
                print("Vida restante:", self.nave.vida)
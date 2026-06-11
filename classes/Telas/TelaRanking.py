import sound
from classes.Telas.Tela import Tela
import sprites as sprite
import config


class TelaRanking(Tela):
    def __init__(self):
        super().__init__()

    def atualizar(self):
        super().atualizar()

    def desenhar(self):
        super().desenhar([sprite.background_rank])
        config.window.set_background_color("black")
        ranking = self.melhores_ranking()
        for i, (nome, pontos, data) in enumerate(ranking):
            config.window.draw_text(f"{i+1}. {nome} - {pontos:.2f} pontos - {data}", 50, 50 + i * 30, color="white", size=20)

    def melhores_ranking(self):
        with open("rank.txt", "r") as f:
            arr = []
            for linha in f:
                nome, pontos, data = linha.strip().split(" / ")
                pontos = float(pontos)
                arr.append((nome, pontos, data))
            arr.sort(key=lambda x: x[1], reverse=True)
            return arr[:5]


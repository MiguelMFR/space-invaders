import sound
from classes.Telas.Tela import Tela
import sprites as sprite
import config


class TelaMenu(Tela):
    def __init__(self):
        super().__init__()

    def atualizar(self):
        super().atualizar()

    def desenhar(self, lista_sprites):
        return super().desenhar(lista_sprites)

    def verificar_click_botao(self):
        botao_clicado = super().verificar_click_botao([
            sprite.botao_jogar,
            sprite.botao_dificuldade,
            sprite.botao_rank,
            sprite.botao_sair,
            sprite.volume_on if config.volume == 1 else sprite.volume_off
        ])

        if botao_clicado == sprite.botao_jogar:
            config.control = config.jogo

        elif botao_clicado == sprite.botao_dificuldade:
            config.control = config.dificuldade

        elif botao_clicado == sprite.botao_rank:
            config.control = config.ranking

        elif botao_clicado == sprite.botao_sair:
            config.running = False
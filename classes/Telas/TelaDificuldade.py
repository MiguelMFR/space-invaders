from classes.Telas.Tela import Tela
import sprites as sprite
import config

class TelaDificuldade(Tela):
    def __init__(self):
        super().__init__()

    def atualizar(self):
        super().atualizar()

    def desenhar(self, lista_sprites):
        return super().desenhar(lista_sprites)  

    def verificar_click_botao(self):
        botao_clicado = super().verificar_click_botao([sprite.botao_dificuldade_facil, sprite.botao_dificuldade_medio, sprite.botao_dificuldade_hard])
        
        if botao_clicado == sprite.botao_dificuldade_facil:
            config.modo_dificuldade = "facil"
            config.control = config.menu
        elif botao_clicado == sprite.botao_dificuldade_medio:
            config.modo_dificuldade = "medio"
            config.control = config.menu
        elif botao_clicado == sprite.botao_dificuldade_hard:
            config.modo_dificuldade = "dificil"
            config.control = config.menu
        elif config.keyboard.key_pressed("ESC"):
            config.control = config.menu

import sprites as sprite
import config
import classes.Telas.TelaDificuldade as TelaDificuldade

def dificuldade():
    tela = TelaDificuldade.TelaDificuldade()

    tela.atualizar()
    tela.desenhar([
        sprite.background_dif, 
        sprite.botao_dificuldade_facil, 
        sprite.botao_dificuldade_medio, 
        sprite.botao_dificuldade_hard
    ])
    tela.verificar_volume() 
    tela.verificar_click_botao()
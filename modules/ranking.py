import config
import classes.Telas.TelaRanking as TelaRanking

def ranking():
    tela_ranking = TelaRanking.TelaRanking()

    while True:
        tela_ranking.desenhar()

        tela_ranking.atualizar()


        if config.keyboard.key_pressed("ESC"):
            config.control = config.menu
            return 0
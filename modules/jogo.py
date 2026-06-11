import sprites as sprite
import config
import sound
from classes.Game import Game
import config
import datetime

def jogar():

    game = Game()
    game.iniciar()
    sound.som_menu.stop()
    sound.som_jogo.play()
    
    nome_salvo = False

    while True:
        game.atualizar()

        if game.game_over:

            if not nome_salvo:
                jogador = input("Digite seu nome para o ranking: ")

                with open("rank.txt", "a+") as f:
                    f.write(f"{jogador} / {game.pontos:.2f} / {datetime.datetime.now()}\n")

                nome_salvo = True

            sprite.game_over.draw()
            sprite.press_enter_or_esc.draw()
            sound.som_game_over.play()
            if config.keyboard.key_pressed("ESC"):
                sound.som_jogo.stop()
                config.control = config.menu
                return 0

        config.window.update()
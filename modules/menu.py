import sprites as sprite
import config


def menu():
    while True:
        

        config.window.set_background_color((20,20,20))
        sprite.background_menu.draw()
        sprite.botao_jogar.draw()
        sprite.botao_dificuldade.draw()
        sprite.botao_rank.draw()
        sprite.botao_sair.draw()

        if config.mouse.is_over_object(sprite.botao_sair) and config.mouse.is_button_pressed(1):
            config.running = False
            break

        if config.mouse.is_over_object(sprite.botao_dificuldade) and config.mouse.is_button_pressed(1):
            config.control = config.dificuldade
            return 0

        if config.mouse.is_over_object(sprite.botao_jogar) and config.mouse.is_button_pressed(1):
            config.control = config.jogo
            return 0


        if config.mouse.is_over_object(sprite.botao_rank) and config.mouse.is_button_pressed(1):
            config.control = config.ranking
            return 0

        config.window.update()
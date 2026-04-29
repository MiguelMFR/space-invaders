import sprites as sprite
import config

def dificuldade():

    while True:
        config.window.set_background_color((20, 20, 20))
        sprite.background_dif.draw()
        sprite.botao_dificuldade_facil.draw()    
        sprite.botao_dificuldade_medio.draw()
        sprite.botao_dificuldade_hard.draw()    

        config.window.update()


        if config.mouse.is_over_object(sprite.botao_dificuldade_facil) and config.mouse.is_button_pressed(1):
            config.control = config.jogo
            return 0

        if config.mouse.is_over_object(sprite.botao_dificuldade_medio) and config.mouse.is_button_pressed(1):
            config.control = config.jogo
            return 0
        
        if config.mouse.is_over_object(sprite.botao_dificuldade_hard) and config.mouse.is_button_pressed(1):
            config.control = config.jogo
            return 0

        if config.keyboard.key_pressed("ESC"):
            config.control = config.menu
            return 0
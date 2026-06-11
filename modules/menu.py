import sprites as sprite
import config
import sound
import classes.Telas.TelaMenu as TelaMenu



def menu():
    sound.som_jogo.stop()
    sound.som_menu.play()
    config.mouse_pressed_anterior = config.mouse.is_button_pressed(1)
    tela = TelaMenu.TelaMenu()

    tela.atualizar()

    tela.desenhar([
        sprite.background_menu,
        sprite.botao_jogar,
        sprite.botao_dificuldade,
        sprite.botao_rank,
        sprite.botao_sair,
        sprite.volume_on if config.volume == 1 else sprite.volume_off
    ])

    tela.verificar_volume()
    tela.verificar_click_botao()
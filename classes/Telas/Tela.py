import config
import sound
import sprites as sprite

mouse_pressed_anterior = False

class Tela:
    def __init__(self):
        self.estado = "menu"

    def desenhar(self, lista_sprites: list[sprite.Sprite]):
        if config.volume == 0:
            sprite.volume_off.draw()
        else:
            sprite.volume_on.draw()

        for s in lista_sprites:
            s.draw()

    def verificar_volume(self):
        if config.volume == 0:
            sound.som_click.set_volume(0)
            sound.som_game_over.set_volume(0)
            sound.som_tiro.set_volume(0)
            sound.som_menu.set_volume(0)
            sound.som_jogo.set_volume(0)

        else:
            sound.som_click.set_volume(10)
            sound.som_game_over.set_volume(10)
            sound.som_tiro.set_volume(5)
            sound.som_menu.set_volume(10)
            sound.som_jogo.set_volume(20)
    
    def clique_unico(self):
        pressionado = config.mouse.is_button_pressed(1)

        clicou_agora = pressionado and not config.mouse_pressed_anterior

        config.mouse_pressed_anterior = pressionado

        return clicou_agora

    def verificar_click_botao(self, lista_botao: list[sprite.Sprite]):

        if not self.clique_unico():
            return None

        for botao in lista_botao:

            if config.mouse.is_over_object(botao):

                if botao in (sprite.volume_on, sprite.volume_off):
                    config.volume = 0 if config.volume == 1 else 1
                    self.verificar_volume()
                    sound.som_click.play()
                    return None

                return botao

        return None

    def atualizar(self):
        config.window.update()
import random
from PPlay.sprite import Sprite
import config

# MENU
espaco = 100 
y_inicial = config.window.height/2 - (3 * espaco)/2

botao_jogar = Sprite("images/jogar.png", 1)
botao_jogar.set_position(
    config.window.width/2 - botao_jogar.width/2,
    y_inicial
)

botao_dificuldade = Sprite("images/dificuldade.png", 1)
botao_dificuldade.set_position(
    config.window.width/2 - botao_dificuldade.width/2,
    y_inicial + espaco
)

botao_rank = Sprite("images/ranking.png", 1)
botao_rank.set_position(
    config.window.width/2 - botao_rank.width/2,
    y_inicial + espaco*2
)

botao_sair = Sprite("images/sair.png", 1)
botao_sair.set_position(
    config.window.width/2 - botao_sair.width/2,
    y_inicial + espaco*3
)

#DIFICULDADE
espaco_dif = 100

y_inicial_dif = config.window.height/2 - (2 * espaco_dif)/2

botao_dificuldade_facil = Sprite("images/facil.png", 1)
botao_dificuldade_facil.set_position(
    config.window.width/2 - botao_dificuldade_facil.width/2,
    y_inicial_dif
)

botao_dificuldade_medio = Sprite("images/medio.png", 1)
botao_dificuldade_medio.set_position(
    config.window.width/2 - botao_dificuldade_medio.width/2,
    y_inicial_dif + espaco_dif
)

botao_dificuldade_hard = Sprite("images/dificil.png", 1)
botao_dificuldade_hard.set_position(
    config.window.width/2 - botao_dificuldade_hard.width/2,
    y_inicial_dif + espaco_dif*2
)

# BACKGROUND
background_menu = Sprite("images/background-menu.png", 1)
background_menu.set_position(0, 0)
background_dif = Sprite("images/background-dif.png", 1)
background_dif.set_position(0, 0)
background_jogo = Sprite("images/background-jogo.png", 1)
background_jogo.set_position(0, 0)
background_rank = Sprite("images/background-dif.png", 1)
background_rank.set_position(0, 0)
# NAVE

nave = Sprite("images/nave.png", 1)
tiro_nave = Sprite("images/nave_tiro.png", 1)
nave.set_position(config.window.width/2 - nave.width/2, config.window.height - nave.height)
vida = Sprite("images/vida.png", 1)

# MONSTROS

polvo = Sprite("images/polvo.png", 1)
caranguejo = Sprite("images/caranguejo.png", 1)

# GAME OVER
game_over = Sprite("images/game-over.png", 1)
game_over.set_position(config.window.width/2 - game_over.width/2, config.window.height/2 - game_over.height/2)
press_enter_or_esc = Sprite("images/game-over-comp.png", 1)
press_enter_or_esc.set_position(config.window.width/2 - press_enter_or_esc.width/2, config.window.height/2 + game_over.height/2)

# VOLUME 
volume_on = Sprite("images/som-ligado.png", 1)
volume_on.set_position(config.window.width - volume_on.width - 10, 10)
volume_off = Sprite("images/som-desligado.png", 1)
volume_off.set_position(config.window.width - volume_off.width - 10, 10)
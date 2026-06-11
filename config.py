from PPlay.window import *
window = Window(1240, 619)
window.set_title('Space Invaders')

keyboard = window.get_keyboard()

mouse = window.get_mouse()

menu = 0
ranking = 1
dificuldade = 2
jogo = 3

modo_dificuldade = "facil"

tiro_monstro = {
    "facil": 0.8,
    "medio": 0.6,
    "dificil": 0.4
}

tiro_nave = {
    "facil": 0.5,
    "medio": 0.4,
    "dificil": 0.3
}

velocidade_nave = {
    "facil": 360,
    "medio": 260,
    "dificil": 200
}

velocidade_monstros = {
    "facil": 60,
    "medio": 90,
    "dificil": 120
}

control = menu 

volume = 1  

vida = 5

mouse_pressed_anterior = False

running = True
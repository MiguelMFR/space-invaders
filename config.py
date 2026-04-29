from PPlay.window import *
window = Window(1240, 620)
window.set_title('Space Invaders')

keyboard = window.get_keyboard()

mouse = window.get_mouse()

menu = 0
ranking = 1
dificuldade = 2
jogo = 3

control = menu    

running = True
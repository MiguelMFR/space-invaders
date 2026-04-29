import config
import modules.jogo as jogo
import modules.menu as menu 
import modules.ranking as ranking 
import modules.dificuldade as dificuldade 

config.control = config.menu

while config.running:
    
    match config.control:

        case config.menu:
            menu.menu()
        case config.jogo:
            jogo.jogar()
        case config.ranking:
            ranking.ranking()
        case config.dificuldade:
            dificuldade.dificuldade()
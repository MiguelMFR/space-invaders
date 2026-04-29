import config

def ranking():
    
    while True:
        config.window.set_background_color((20, 20, 20))
        config.window.update()

        if config.keyboard.key_pressed("ESC"):
            config.control = config.menu
            return 0
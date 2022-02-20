import pygame as pg


pg.init()


class Winodw:
    def __init__(self):
        self.scale = (700, 500)
        self.background = pg.transform.scale(
            pg.image.load('background.jpg'),
            self.scale
        )
        self.win = pg.display.set_mode(self.scale)
        self.clock = pg.time.Clock()
        self.FPS = 60

        pg.display.set_caption('Maze')
        pg.mixer.music.load('jungles.ogg')
        pg.mixer.music.play()

        # labels
    
    def update(self):
        """Updates window"""
        pg.display.update()
        self.clock.tick(self.FPS)
    
    def blit_bg(self):
        self.win.blit(self.background, (0, 0))
        # self.win.fill((255, 255, 255))
    
    def lose(self):
        # self.win.blit(self.lose, (600, 400))
        pass

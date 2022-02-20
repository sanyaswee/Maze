import pygame as pg


pg.init()


class Winodw:
    def __init__(self):
        self.width = 700
        self.height = 500
        self.name = 'Maze'
        self.background = pg.transform.scale(
            pg.image.load('background.jpg'),
            (self.width, self.height)
        )
        self.rect = self.background.get_rect()
        pg.mixer.music.load('jungles.ogg')
        self.clock = pg.time.Clock()
        self.FPS = 60

        self.win = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.name)
        pg.mixer.music.play()

        self.font = pg.font.SysFont('arial', 30)
        self.lose = self.font.render('ПРОИГРЫШ', True, pg.Color('red'))
        self.win = self.font.render('ПОБЕДА', True, pg.Color('red'))
    
    def update(self):
        """Updates window"""
        pg.display.update()
        self.clock.tick(self.FPS)
    
    def blit_bg(self):
        # self.win.blit(self.background, (0, 0))
        self.win.fill((255, 255, 255))
    
    def lose(self):
        self.win.blit(self.lose, (600, 400))

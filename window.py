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
        pg.display.set_icon(pg.image.load('hero.png'))

        # labels
        font = pg.font.SysFont('bookmanoldstyle', 60)
        self.lose = font.render('ПРОИГРЫШ', True, pg.Color('red'))
        self.win_ = font.render('ВЫ ВЫИГРАЛИ', True, pg.Color('red'))
        font = pg.font.SysFont('bookmanoldstyle', 20)
        self.end_descript = font.render('Нажмите пробел для повтора, "esc" для выхода', True, pg.Color('red'))

        # sounds
        self.kick = pg.mixer.Sound('kick.ogg')
        self.money = pg.mixer.Sound('money.ogg')
    
    def update(self):
        """Updates window"""
        pg.display.update()
        self.clock.tick(self.FPS)
    
    def blit_bg(self):
        """Blits background"""
        self.win.blit(self.background, (0, 0))
    
    def lose_(self):
        """Shows "lose" label"""
        self.win.blit(self.lose, (200, 100))
        self.describe()

    def win__(self):
        self.win.blit(self.win_, (200, 100))
        self.describe()

    def describe(self):
        """Shows end_description"""
        self.win.blit(self.end_descript, (100, 200))

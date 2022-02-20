import pygame as pg


pg.init()


class GameSprite(pg.sprite.Sprite):
    def __init__(self, image='hero.png', x=0, y=0, scale=(100, 100)):
        super().__init__()
        self.image = pg.transform.scale(
            pg.image.load(image),
            scale
        )
        self.scale = scale
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def blit(self, win):
        """Blits the sprite"""
        win.blit(self.image, (self.rect.x, self.rect.y))
    
    def tp(self, x, y):
        """Updates coordinates"""
        self.rect.x = x
        self.rect.y = y


class Movable(GameSprite):
    def __init__(self, image='hero.png', x=0, y=0, scale=(100, 100), speed=10):
        super().__init__(image, x, y, scale)
        self.speed = speed
    
    def move(self, direction):
        """Moves an object"""
        # self.rect = self.image.get_rect()
        if direction == 'u':
            self.rect.y -= self.speed
        elif direction == 'd':
            self.rect.y += self.speed
        elif direction == 'r':
            self.rect.x += self.speed
        elif direction == 'l':
            self.rect.x -= self.speed


class Enemy(Movable):
    direction = 'r'

    def go_round(self):
        #self.rect = self.image.get_rect()
        """Goes left and right"""
        if self.rect.x > 600:
            self.direction = 'l'
        if self.rect.x < 500:
            self.direction = 'r'
        
        self.move(self.direction)


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, scale=(15, 350), color=pg.Color('green')):
        super().__init__()
        self.rect = pg.Rect((x, y), scale)
        self.scale = scale
        self.color = color

    def show(self, win):
        pg.draw.rect(win, self.color, self.rect)

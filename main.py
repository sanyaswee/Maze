import pygame as pg
from window import Winodw
from sprites import GameSprite, Movable, Enemy, Wall


pg.init()


win = Winodw()


hero = Movable()
hero.tp(25, 400)


enemy = Enemy('cyborg.png', scale=(80, 80), speed=3)
enemy.tp(500, 250)


treasure = GameSprite('treasure.png', scale=(50, 50))
treasure.tp(600, 400)


walls = Wall(150, 150), Wall(315, 0), Wall(480, 150)


def collide_wall():
    """Checks if hero collides wall"""
    global hero, walls
    for wall in walls:
        if pg.sprite.collide_rect(hero, wall):
            return True
    else:
        return False


finish = False
game = True
while game:
    if not finish:
        # bliting background
        win.blit_bg()
        # bliting sprites
        hero.blit(win.win)
        enemy.blit(win.win)
        treasure.blit(win.win)
        # bliting walls
        for wall in walls:
            wall.show(win.win)
        # checking events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        # moving
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            if hero.rect.y >= 0:
                hero.move('u')
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            if hero.rect.y <= win.scale[1] - hero.scale[1]:
                hero.move('d')
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            if hero.rect.x <= win.scale[0] - hero.scale[0]:
                hero.move('r')
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            if hero.rect.x >= 0:
                hero.move('l')

        enemy.go_round()
        # checking collision
        if pg.sprite.collide_rect(hero, enemy)  or collide_wall():
            finish = True
    else:
        pass
    # updating
    win.update()

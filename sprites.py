import pygame as pg
from settings import *
import random


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Worker(pg.sprite.Sprite):
    def __init__(self, game, x, y, job, location):
        self.groups = game.all_sprites, game.workers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.job = job
        self.location = location

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def random_move(self):
        direction = random.randint(0, 3)
        if direction == 0:
            if not self.collide_with_walls(dx=-1):
                self.x = self.x - 1
        elif direction == 1:
            if not self.collide_with_walls(dx=1):
                self.x = self.x + 1
        elif direction == 2:
            if not self.collide_with_walls(dy=-1):
                self.y = self.y - 1
        elif direction == 3:
            if not self.collide_with_walls(dy=1):
                self.y = self.y + 1

        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def update(self):
        self.random_move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)




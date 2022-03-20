import pygame as pg

import calculation
import settings
from settings import *
import random


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, location):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        self.location = location

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Worker(pg.sprite.Sprite):
    def __init__(self, game, x, y, job, location):
        self.groups = game.all_sprites, game.workers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if job == "lumber":
            self.image = pg.image.load("red-dino16.png")
            self.pic = "red-dino"
            self.working_days = calculation.lumber_days
            self.working_hours = calculation.lumber_hours
        elif job == "nuclear":
            self.image = pg.image.load("green-dino16.png")
            self.pic = "green-dino"
            self.working_days = calculation.nuclear_days
            self.working_hours = calculation.nuclear_hours
        elif job == "agriculture":
            self.image = pg.image.load("blue-dino16.png")
            self.pic = "blue-dino"
            self.working_days = calculation.agriculture_days
            self.working_hours = calculation.agriculture_hours
        elif job == "chemical":
            self.image = pg.image.load("yellow-dino16.png")
            self.pic = "yellow-dino"
            self.working_days = calculation.chemical_days
            self.working_hours = calculation.chemical_hours
        else:
            self.image = pg.image.load("black-dino16.png")
            self.pic = "black-dino"
            self.working_days = calculation.mining_days
            self.working_hours = calculation.mining_hours
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.x_goal = 0
        self.y_goal = 0
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.job = job
        self.location = location
        self.commuting_to_work = False
        self.commuting_home = False
        self.working = False

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy and wall.location == self.location:
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

        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE

    def update(self):
        # If workers finish their commute, take them to their workplace.
        if self.x == 59 and self.y == 43 and self.commuting_to_work:
            self.location = self.job
            self.x = 16
            self.y = 12
            self.commuting_to_work = False
            self.working = True
        # If workers finish their work, take them home.
        if self.x == 29 and self.y == 21 and self.commuting_home:
            self.location = "neighborhood"
            self.x = 32
            self.y = 24
            self.commuting_home = False
            self.working = False
        # If it's time to commute to work, give workers a path.
        if self.game.hour == 2 and self.game.minute == 0 and self.location == "neighborhood":
            if self.game.day in self.working_days:
                self.x_goal = 59
                self.y_goal = 43
                self.commuting_to_work = True
        # If it's time to to commute back home, give workers a path.
        if self.game.hour == (3 + self.working_hours) and self.game.minute == 0 and self.working:
            self.x_goal = 29
            self.y_goal = 21
            self.commuting_home = True
        if self.commuting_home or self.commuting_to_work:
            if self.y < self.y_goal:
                self.y = self.y + 1
            elif self.x < self.x_goal:
                self.x = self.x + 1
            self.rect.x = self.x * settings.TILESIZE
            self.rect.y = self.y * settings.TILESIZE
        else:
            self.random_move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)




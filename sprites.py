import pygame as pg

import settings
import util
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
        self.image = pg.Surface((TILESIZE, TILESIZE))
        if job == "lumber":
            self.color = CHOCOLATE
        elif job == "nuclear":
            self.color = GREEN
        elif job == "agriculture":
            self.color = BLUE
        elif job == "chemical":
            self.color = YELLOW
        else:
            self.color = MAROON
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.job = job
        self.location = location
        self.hasSearched = False
        self.path = []
        self.commuting = False
        self.history = []

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy and wall.location == self.location:
                return True
        return False

    def bfs(self, goalx, goaly):
        visited = []
        bfs_queue = util.Queue()
        bfs_queue.push([self.x, self.y, []])
        while not bfs_queue.isEmpty():
            node = bfs_queue.pop()
            if node[0] != goalx or node[1] != goaly:
                if (node[0], node[1]) not in visited:
                    visited.append((node[0], node[1]))
                    successors = []
                    up = True
                    down = True
                    left = True
                    right = True
                    for wall in self.game.walls:
                        if wall.x == node[0] + 1 and wall.y == node[1]:
                            right = False
                        if wall.x == node[0] - 1 and wall.y == node[1]:
                            left = False
                        if wall.y == node[1] + 1 and wall.x == node[0]:
                            down = False
                        if wall.y == node[1] - 1 and wall.x == node[0]:
                            up = False
                    if up:
                        successors.append((node[0], node[1] - 1))
                    if down:
                        successors.append((node[0], node[1] + 1))
                    if left:
                        successors.append((node[0] - 1, node[1]))
                    if right:
                        successors.append((node[0] + 1, node[1]))
                    for s in successors:
                        if s not in visited:
                            path_history = []
                            path_history.extend(node[2])
                            path_history.append(s)
                            bfs_queue.push((s[0], s[1], path_history))
            else:
                path = []
                if self.x + 1 == node[2][0][0] and self.y == node[2][0][1]:
                    path.append('E')
                elif self.x - 1 == node[2][0][0] and self.y == node[2][0][1]:
                    path.append('W')
                elif self.x == node[2][0][0] and self.y + 1 == node[2][0][1]:
                    path.append('S')
                elif self.x == node[2][0][0] and self.y - 1 == node[2][0][1]:
                    path.append('N')
                for i in range(len(node[2]) - 1):
                    if node[2][i][0] + 1 == node[2][i + 1][0] and node[2][i][1] == node[2][i + 1][1]:
                        path.append('E')
                    elif node[2][i][0] - 1 == node[2][i + 1][0] and node[2][i][1] == node[2][i + 1][1]:
                        path.append('W')
                    elif node[2][i][0] == node[2][i + 1][0] and node[2][i][1] + 1 == node[2][i + 1][1]:
                        path.append('S')
                    elif node[2][i][0] == node[2][i + 1][0] and node[2][i][1] - 1 == node[2][i + 1][1]:
                        path.append('N')

                return path

    def go_to_work_path(self, goalx, goaly):
        path = []
        y = goaly - self.y
        x = goalx - self.x
        for i in range(y):
            path.append('S')
        for i in range(x):
            path.append('E')
        return path

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

        if self.x >= 60:
            print("WE GOT THERE X 60")
            print(self.history)
        if self.y >= 44:
            print("WE GOT THERE Y 44")
            print(self.history)


        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE

    def update(self):
        #print(self.x, self.y)
        #print(self.commuting)
        # If workers finish their commute, take them to their workplace.
        if self.x == 59 and self.y == 43 and self.commuting:
            self.location = self.job
            self.x = 16
            self.y = 12
            self.history.append((self.x, self.y))
            self.commuting = False
        # If workers finish their work, take them home.
        if self.x == 29 and self.y == 21 and self.commuting:
            self.location = "neighborhood"
            self.x = 32
            self.y = 24
            self.history.append((self.x, self.y))
            self.commuting = False
        # If it's time to commute to work, give workers a path.
        if self.game.hour == 2 and self.game.minute == 0 and self.location == "neighborhood":
            self.path = self.go_to_work_path(59, 43)
            self.commuting = True
        # If it's time to to commute back home, give workers a path.
        if self.game.hour == 11 and self.game.minute == 0:
            self.path = self.go_to_work_path(29, 21)
            self.commuting = True
        if self.path: # TRY REWRITING THE COMMUTE ALGORITHM
            move = self.path.pop(0)
            if move == 'N':
                self.y = self.y - 1
            elif move == 'S':
                self.y = self.y + 1
            elif move == 'E':
                self.x = self.x + 1
            elif move == 'W':
                self.x = self.x - 1
            self.history.append((self.x, self.y))
            self.rect.x = self.x * settings.TILESIZE
            self.rect.y = self.y * settings.TILESIZE
        else:
            self.random_move()
            self.history.append((self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)




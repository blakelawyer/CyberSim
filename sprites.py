import pygame as pg

import settings
import util
from settings import *
import random

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
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
        self.hasSearched = False
        self.path = []

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
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
        if not self.hasSearched:
            self.path = self.bfs(59, 43)
            self.hasSearched = True
        if self.path:
            move = self.path.pop(0)
            if move == 'N':
                self.y = self.y - 1
            elif move == 'S':
                self.y = self.y + 1
            elif move == 'E':
                self.x = self.x + 1
            elif move == 'W':
                self.x = self.x - 1
            self.rect.x = self.x * settings.TILESIZE
            self.rect.y = self.y * settings.TILESIZE

        else:
            self.random_move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)




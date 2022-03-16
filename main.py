import pygame as pg
import sys
from os import path

import pygame.mouse

import calculation
import settings
from settings import *
from sprites import *

FPS = 60

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

        self.speed_up_button = Button(15, 65, "up-arrow.png")
        self.speed_down_button = Button(15, 125, "down-arrow.png")
        self.pause_button = Button(15, 185, "pause-button.png")

        self.lumber_button = Button(15, 245, "lumber.png")
        self.nuclear_button = Button(15, 305, "nuclear.png")
        self.agriculture_button = Button(15, 365, "agriculture.png")
        self.chemical_button = Button(15, 425, "chemical.png")
        self.mining_button = Button(15, 485, "mining.png")

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.workers = pg.sprite.Group()

        self.paused = False
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.city_map_data = []
        with open(path.join(game_folder, 'city-map.txt'), 'rt') as f:
            for line in f:
                self.city_map_data.append(line)
        self.lumber_map_data = []
        with open(path.join(game_folder, 'lumber-map.txt'), 'rt') as f:
            for line in f:
                self.lumber_map_data.append(line)
        self.nuclear_map_data = []
        with open(path.join(game_folder, 'nuclear-map.txt'), 'rt') as f:
            for line in f:
                self.nuclear_map_data.append(line)
        self.agriculture_map_data = []
        with open(path.join(game_folder, 'agriculture-map.txt'), 'rt') as f:
            for line in f:
                self.agriculture_map_data.append(line)
        self.chemical_map_data = []
        with open(path.join(game_folder, 'chemical-map.txt'), 'rt') as f:
            for line in f:
                self.chemical_map_data.append(line)
        self.mining_map_data = []
        with open(path.join(game_folder, 'mining-map.txt'), 'rt') as f:
            for line in f:
                self.mining_map_data.append(line)

    def city_view(self):
        for row, tiles in enumerate(self.city_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'W':
                    Worker(self, col, row)

    def lumber_view(self):
        for wall in self.walls:
            wall.kill()
        for row, tiles in enumerate(self.lumber_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

    def nuclear_view(self):
        for wall in self.walls:
            wall.kill()
        for row, tiles in enumerate(self.nuclear_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

    def agriculture_view(self):
        for wall in self.walls:
            wall.kill()
        for row, tiles in enumerate(self.agriculture_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

    def chemical_view(self):
        for wall in self.walls:
            wall.kill()
        for row, tiles in enumerate(self.chemical_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

    def mining_view(self):
        for wall in self.walls:
            wall.kill()
        for row, tiles in enumerate(self.mining_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        tick = 0
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()
            tick += 1
            self.minute += 1
            if tick % 60 == 0:
                calculation.lumber_hour()
                calculation.nuclear_hour()
                calculation.agriculture_hour()
                calculation.chemical_hour()
                calculation.mining_hour()
            if self.minute % 60 == 0 and self.minute > 0:
                self.minute = 0
                self.hour += 1
            if self.hour % 16 == 0 and self.hour > 0:
                self.hour = 0
                self.day += 1
            if self.day % 28 == 0 and self.day > 0:
                self.day = 0
                self.month += 1

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)

        if self.speed_up_button.draw(self.screen):
            if settings.FPS < 1000:
                settings.FPS = settings.FPS + 15
        if self.speed_down_button.draw(self.screen):
            if settings.FPS > 15:
                settings.FPS = settings.FPS - 15
        if self.pause_button.draw(self.screen):
            if self.paused:
                self.paused = False
            else:
                self.paused = True
                while(self.paused):
                    self.events()
                    self.draw()

        if self.lumber_button.draw(self.screen):
            self.lumber_view()
        if self.nuclear_button.draw(self.screen):
            self.nuclear_view()
        if self.agriculture_button.draw(self.screen):
            self.agriculture_view()
        if self.chemical_button.draw(self.screen):
            self.chemical_view()
        if self.mining_button.draw(self.screen):
            self.mining_view()


        show_resources(self.screen)
        show_time(self, self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


class Button:
    def __init__(self, x, y, image):
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):

        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


def show_resources(screen):

    font = pg.font.SysFont('Arial', 24)

    text = font.render("Lumber: " + str(calculation.lumber), True, WHITE, BLACK)
    screen.blit(text, (70, 20))

    text = font.render("Nuclear: " + str(calculation.nuclear), True, WHITE, BLACK)
    screen.blit(text, (270, 20))

    text = font.render("Agriculture: " + str(calculation.agriculture), True, WHITE, BLACK)
    screen.blit(text, (470, 20))

    text = font.render("Chemical: " + str(calculation.chemical), True, WHITE, BLACK)
    screen.blit(text, (670, 20))

    text = font.render("Mining: " + str(calculation.mining), True, WHITE, BLACK)
    screen.blit(text, (870, 20))


def show_time(game, screen):
    font = pg.font.SysFont('Arial', 24)

    text = font.render("Month: " + str(game.month), True, WHITE, BLACK)
    screen.blit(text, (70, 720))

    text = font.render("Day: " + str(game.day), True, WHITE, BLACK)
    screen.blit(text, (270, 720))

    text = font.render("Hour: " + str(game.hour), True, WHITE, BLACK)
    screen.blit(text, (470, 720))

    text = font.render("Minute: " + str(game.minute), True, WHITE, BLACK)
    screen.blit(text, (670, 720))


# create the game object
g = Game()
while True:
    g.city_view()
    g.run()
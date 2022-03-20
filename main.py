import pygame as pg
import sys
from os import path
import pygame.mouse
import button
import calculation
import settings
from settings import *
from sprites import *


class Game:
    def __init__(self):
        self.neighborhood_map_data = []
        self.city_map_data = []
        self.lumber_map_data = []
        self.nuclear_map_data = []
        self.agriculture_map_data = []
        self.chemical_map_data = []
        self.mining_map_data = []
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

        self.speed_up_button = button.Button(15, 65, "up-arrow.png")
        self.speed_down_button = button.Button(15, 125, "down-arrow.png")
        self.pause_button = button.Button(15, 185, "pause-button.png")

        self.neighborhood_button = button.Button(15, 245, "neighborhood.png")
        self.city_button = button.Button(15, 305, "city.png")
        self.lumber_button = button.Button(15, 365, "lumber.png")
        self.nuclear_button = button.Button(15, 425, "nuclear.png")
        self.agriculture_button = button.Button(15, 485, "agriculture.png")
        self.chemical_button = button.Button(15, 545, "chemical.png")
        self.mining_button = button.Button(15, 605, "mining.png")

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.workers = pg.sprite.Group()

        self.paused = False
        self.view = 'neighborhood'

        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

    def load_data(self):
        game_folder = path.dirname(__file__)
        with open(path.join(game_folder, 'neighborhood-map.txt'), 'rt') as f:
            for line in f:
                self.neighborhood_map_data.append(line)
        with open(path.join(game_folder, 'city-map.txt'), 'rt') as f:
            for line in f:
                self.city_map_data.append(line)
        with open(path.join(game_folder, 'lumber-map.txt'), 'rt') as f:
            for line in f:
                self.lumber_map_data.append(line)
        with open(path.join(game_folder, 'nuclear-map.txt'), 'rt') as f:
            for line in f:
                self.nuclear_map_data.append(line)
        with open(path.join(game_folder, 'agriculture-map.txt'), 'rt') as f:
            for line in f:
                self.agriculture_map_data.append(line)
        with open(path.join(game_folder, 'chemical-map.txt'), 'rt') as f:
            for line in f:
                self.chemical_map_data.append(line)
        with open(path.join(game_folder, 'mining-map.txt'), 'rt') as f:
            for line in f:
                self.mining_map_data.append(line)

    def setup(self):

        for worker in range(calculation.lumber_workers):
            Worker(self, 32, 24, 'lumber', 'neighborhood')
        for worker in range(calculation.nuclear_workers):
            Worker(self, 32, 24, 'nuclear', 'neighborhood')
        for worker in range(calculation.agriculture_workers):
            Worker(self, 32, 24, 'agriculture', 'neighborhood')
        for worker in range(calculation.chemical_workers):
            Worker(self, 32, 24, 'chemical', 'neighborhood')
        for worker in range(calculation.mining_workers):
            Worker(self, 32, 24, 'mining', 'neighborhood')

        settings.TILESIZE = 16
        for row, tiles in enumerate(self.neighborhood_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "neighborhood")

        settings.TILESIZE = 16
        for row, tiles in enumerate(self.city_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "city")

        settings.TILESIZE = 32
        for row, tiles in enumerate(self.lumber_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "lumber")

        settings.TILESIZE = 32
        for row, tiles in enumerate(self.nuclear_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "nuclear")

        settings.TILESIZE = 32
        for row, tiles in enumerate(self.agriculture_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "agriculture")

        settings.TILESIZE = 32
        for row, tiles in enumerate(self.chemical_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "chemical")

        settings.TILESIZE = 32
        for row, tiles in enumerate(self.mining_map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "mining")

        settings.TILESIZE = 16

    def neighborhood_view(self):
        settings.TILESIZE = 16
        for worker in self.workers:
            if worker.location == "neighborhood":
                worker.image = pg.image.load(worker.pic + "16.png")
                worker.rect = worker.image.get_rect()
        self.view = 'neighborhood'

    def city_view(self):
        settings.TILESIZE = 16
        self.view = 'city'

    def lumber_view(self):
        settings.TILESIZE = 32
        for worker in self.workers:
            if worker.location == "lumber":
                worker.image = pg.image.load(worker.pic + "32.png")
                worker.rect = worker.image.get_rect()
                worker.rect.x = worker.x * settings.TILESIZE
                worker.rect.y = worker.y * settings.TILESIZE
        self.view = 'lumber'

    def nuclear_view(self):
        settings.TILESIZE = 32
        for worker in self.workers:
            if worker.location == "nuclear":
                worker.image = pg.image.load(worker.pic + "32.png")
                worker.rect = worker.image.get_rect()
                worker.rect.x = worker.x * settings.TILESIZE
                worker.rect.y = worker.y * settings.TILESIZE
        self.view = 'nuclear'

    def agriculture_view(self):
        settings.TILESIZE = 32
        for worker in self.workers:
            if worker.location == "agriculture":
                worker.image = pg.image.load(worker.pic + "32.png")
                worker.rect = worker.image.get_rect()
                worker.rect.x = worker.x * settings.TILESIZE
                worker.rect.y = worker.y * settings.TILESIZE
        self.view = 'agriculture'

    def chemical_view(self):
        settings.TILESIZE = 32
        for worker in self.workers:
            if worker.location == "chemical":
                worker.image = pg.image.load(worker.pic + "32.png")
                worker.rect = worker.image.get_rect()
                worker.rect.x = worker.x * settings.TILESIZE
                worker.rect.y = worker.y * settings.TILESIZE
        self.view = 'chemical'

    def mining_view(self):
        settings.TILESIZE = 32
        for worker in self.workers:
            if worker.location == "mining":
                worker.image = pg.image.load(worker.pic + "32.png")
                worker.rect = worker.image.get_rect()
                worker.rect.x = worker.x * settings.TILESIZE
                worker.rect.y = worker.y * settings.TILESIZE
        self.view = 'mining'

    def run(self):
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
                for worker in self.workers:
                    if worker.job == "lumber" and worker.working:
                        calculation.lumber_hour()
                    elif worker.job == "nuclear" and worker.working:
                        calculation.nuclear_hour()
                    elif worker.job == "agriculture" and worker.working:
                        calculation.agriculture_hour()
                    elif worker.job == "chemical" and worker.working:
                        calculation.chemical_hour()
                    elif worker.job == "mining" and worker.working:
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
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Worker):
                if self.view == sprite.location:
                    sprite.draw(self.screen)
            elif isinstance(sprite, Wall):
                if self.view == sprite.location:
                    sprite.draw(self.screen)

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
                while (self.paused):
                    self.events()
                    self.draw()

        if self.neighborhood_button.draw(self.screen):
            self.neighborhood_view()
        if self.city_button.draw(self.screen):
            self.city_view()
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

        button.show_resources(self.screen)
        button.show_time(self, self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


g = Game()
while True:
    g.setup()
    g.neighborhood_view()
    g.run()

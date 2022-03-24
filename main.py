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
        self.editing = "N/A"
        self.value = 0
        self.view = 'neighborhood'

        self.month = 0
        self.week = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

        self.neighborhood_background = pg.image.load("neighborhood-background.png")
        self.lumber_background = pg.image.load("lumber-background.png")
        self.nuclear_background = pg.image.load("nuclear-background.png")
        self.chemical_background = pg.image.load("chemical-background.png")
        self.agriculture_background = pg.image.load("agriculture-background.png")
        self.mining_background = pg.image.load("mining-background.png")
        self.city_background = pg.image.load("city-planning.png")

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
                    if worker.job == "lumber" and worker.working and self.hour > 2:
                        calculation.lumber_hour()
                    elif worker.job == "nuclear" and worker.working and self.hour > 2:
                        calculation.nuclear_hour()
                    elif worker.job == "agriculture" and worker.working and self.hour > 2:
                        calculation.agriculture_hour()
                    elif worker.job == "chemical" and worker.working and self.hour > 2:
                        calculation.chemical_hour()
                    elif worker.job == "mining" and worker.working and self.hour > 2:
                        calculation.mining_hour()
            if self.minute % 60 == 0 and self.minute > 0:
                self.minute = 0
                self.hour += 1
            if self.hour % 16 == 0 and self.hour > 0:
                for i in range(100):
                    if calculation.energy_drinks < calculation.energy_drinks_to_make:
                        if calculation.nuclear >= 10 and calculation.chemical >= 50 and calculation.mining >= 20:
                            calculation.make_energy_drink()
                            calculation.energy_drinks_to_make -= 1
                    if calculation.corn_flakes < calculation.corn_flakes_to_make:
                        if calculation.lumber >= 10 and calculation.agriculture >= 50 and calculation.mining >= 10:
                            calculation.make_corn_flakes()
                            calculation.corn_flakes_to_make -= 1
                    if calculation.TVs < calculation.TVs_to_make:
                        if calculation.lumber >= 10 and calculation.nuclear >= 20 and calculation.chemical >= 10 and calculation.mining >= 30:
                            calculation.make_TV()
                            calculation.TVs_to_make -= 1
                    if calculation.computers < calculation.computers_to_make:
                        if calculation.nuclear >= 30 and calculation.chemical >= 20 and calculation.mining >= 40:
                            calculation.make_computer()
                            calculation.computers_to_make -= 1
                    if calculation.bicycles < calculation.bicycles_to_make:
                        if calculation.lumber >= 20 and calculation.mining >= 40:
                            calculation.make_bicycle()
                            calculation.bicycles_to_make -= 1
                    if calculation.roller_skates < calculation.roller_skates_to_make:
                        if calculation.lumber >= 10 and calculation.mining >= 20:
                            calculation.make_roller_skates()
                            calculation.roller_skates_to_make -= 1
                    if calculation.vitamins < calculation.vitamins_to_make:
                        if calculation.agriculture >= 10 and calculation.chemical >= 30:
                            calculation.make_vitamins()
                            calculation.vitamins_to_make -= 1
                    if calculation.pet_food < calculation.pet_food_to_make:
                        if calculation.agriculture >= 30 and calculation.chemical >= 10:
                            calculation.make_pet_food()
                            calculation.pet_food_to_make -= 1
                    if calculation.mattresses < calculation.mattresses_to_make:
                        if calculation.lumber >= 30 and calculation.agriculture >= 30 and calculation.mining >= 10:
                            calculation.make_mattress()
                            calculation.mattresses_to_make -= 1
                    if calculation.yo_yos < calculation.yo_yos_to_make:
                        if calculation.lumber >= 10 and calculation.agriculture >= 10:
                            calculation.make_yo_yo()
                            calculation.yo_yos_to_make -= 1
                print(calculation.energy_drinks, calculation.corn_flakes, calculation.TVs, calculation.computers, calculation.bicycles, calculation.roller_skates, calculation.vitamins, calculation.pet_food, calculation.mattresses, calculation.yo_yos)
                self.hour = 0
                self.day += 1
            if self.day % 7 == 0 and self.day > 0:
                self.day = 0
                self.week += 1
            if self.week % 4 == 0 and self.month > 0:
                self.week = 0
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
        if self.view == "neighborhood":
            self.screen.blit(self.neighborhood_background, (64, 64))
        if self.view == "lumber":
            self.screen.blit(self.lumber_background, (64, 64))
        elif self.view == "nuclear":
            self.screen.blit(self.nuclear_background, (64, 64))
        elif self.view == "chemical":
            self.screen.blit(self.chemical_background, (64, 64))
        elif self.view == "agriculture":
            self.screen.blit(self.agriculture_background, (64, 64))
        elif self.view == "mining":
            self.screen.blit(self.mining_background, (64, 64))
        elif self.view == "city":
            self.screen.blit(self.city_background, (64, 64))
        #self.draw_grid()
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
        if self.view == "city":
            button.show_settings(self, self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_a:
                    self.editing = "Lumber"
                if event.key == pg.K_b:
                    self.editing = "Nuclear"
                if event.key == pg.K_c:
                    self.editing = "Agriculture"
                if event.key == pg.K_d:
                    self.editing = "Chemical"
                if event.key == pg.K_e:
                    self.editing = "Mining"
                if event.key == pg.K_1:
                    self.editing = "Energy Drinks"
                if event.key == pg.K_2:
                    self.editing = "Corn Flakes"
                if event.key == pg.K_3:
                    self.editing = "TVs"
                if event.key == pg.K_4:
                    self.editing = "Computers"
                if event.key == pg.K_5:
                    self.editing = "Bicycles"
                if event.key == pg.K_6:
                    self.editing = "Roller Skates"
                if event.key == pg.K_7:
                    self.editing = "Vitamins"
                if event.key == pg.K_8:
                    self.editing = "Pet Food"
                if event.key == pg.K_9:
                    self.editing = "Mattresses"
                if event.key == pg.K_0:
                    self.editing = "Yo-yos"

                if event.key == pg.K_UP:
                    if self.editing == "Lumber":
                        if self.value == 0:
                            calculation.lumber_hours += 1
                        elif self.value == 1:
                            if len(calculation.lumber_days) < 7:
                                calculation.lumber_days.append(len(calculation.lumber_days))
                    if self.editing == "Nuclear":
                        if self.value == 0:
                            calculation.nuclear_hours += 1
                        elif self.value == 1:
                            if len(calculation.nuclear_days) < 7:
                                calculation.nuclear_days.append(len(calculation.nuclear_days))
                    if self.editing == "Agriculture":
                        if self.value == 0:
                            calculation.agriculture_hours += 1
                        elif self.value == 1:
                            if len(calculation.agriculture_days) < 7:
                                calculation.agriculture_days.append(len(calculation.agriculture_days))
                    if self.editing == "Chemical":
                        if self.value == 0:
                            calculation.chemical_hours += 1
                        elif self.value == 1:
                            if len(calculation.chemical_days) < 7:
                                calculation.chemical_days.append(len(calculation.chemical_days))
                    if self.editing == "Mining":
                        if self.value == 0:
                            calculation.mining_hours += 1
                        elif self.value == 1:
                            if len(calculation.mining_days) < 7:
                                calculation.mining_days.append(len(calculation.mining_days))
                    if self.editing == "Energy Drinks":
                        if self.value == 0:
                            calculation.energy_drinks_min += 1
                        elif self.value == 1:
                            calculation.energy_drinks_max += 50
                    if self.editing == "Corn Flakes":
                        if self.value == 0:
                            calculation.corn_flakes_min += 1
                        elif self.value == 1:
                            calculation.corn_flakes_max += 50
                    if self.editing == "TVs":
                        if self.value == 0:
                            calculation.TVs_min += 1
                        elif self.value == 1:
                            calculation.TVs_max += 50
                    if self.editing == "Computers":
                        if self.value == 0:
                            calculation.computers_min += 1
                        elif self.value == 1:
                            calculation.computers_max += 50
                    if self.editing == "Bicycles":
                        if self.value == 0:
                            calculation.bicycles_min += 1
                        elif self.value == 1:
                            calculation.bicycles_max += 50
                    if self.editing == "Roller Skates":
                        if self.value == 0:
                            calculation.roller_skates_min += 1
                        elif self.value == 1:
                            calculation.roller_skates_max += 50
                    if self.editing == "Vitamins":
                        if self.value == 0:
                            calculation.vitamins_min += 1
                        elif self.value == 1:
                            calculation.vitamins_max += 50
                    if self.editing == "Pet Food":
                        if self.value == 0:
                            calculation.pet_food_min += 1
                        elif self.value == 1:
                            calculation.pet_food_max += 50
                    if self.editing == "Mattresses":
                        if self.value == 0:
                            calculation.mattresses_min += 1
                        elif self.value == 1:
                            calculation.mattresses_max += 50
                    if self.editing == "Yo-yos":
                        if self.value == 0:
                            calculation.yo_yos_min += 1
                        elif self.value == 1:
                            calculation.yo_yos_max += 50
                if event.key == pg.K_DOWN:
                    if self.editing == "Lumber":
                        if self.value == 0:
                            calculation.lumber_hours -= 1
                        elif self.value == 1:
                            if len(calculation.lumber_days) > 0:
                                del calculation.lumber_days[-1]
                    if self.editing == "Nuclear":
                        if self.value == 0:
                            calculation.nuclear_hours -= 1
                        elif self.value == 1:
                            if len(calculation.nuclear_days) > 0:
                                del calculation.nuclear_days[-1]
                    if self.editing == "Agriculture":
                        if self.value == 0:
                            calculation.agriculture_hours -= 1
                        elif self.value == 1:
                            if len(calculation.agriculture_days) > 0:
                                del calculation.agriculture_days[-1]
                    if self.editing == "Chemical":
                        if self.value == 0:
                            calculation.chemical_hours -= 1
                        elif self.value == 1:
                            if len(calculation.chemical_days) > 0:
                                del calculation.chemical_days[-1]
                    if self.editing == "Mining":
                        if self.value == 0:
                            calculation.mining_hours -= 1
                        elif self.value == 1:
                            if len(calculation.mining_days) > 0:
                                del calculation.mining_days[-1]
                    if self.editing == "Energy Drinks":
                        if self.value == 0:
                            calculation.energy_drinks_min -= 1
                        elif self.value == 1:
                            calculation.energy_drinks_max -= 1
                    if self.editing == "Corn Flakes":
                        if self.value == 0:
                            calculation.corn_flakes_min -= 1
                        elif self.value == 1:
                            calculation.corn_flakes_max -= 1
                    if self.editing == "TVs":
                        if self.value == 0:
                            calculation.TVs_min -= 1
                        elif self.value == 1:
                            calculation.TVs_max -= 1
                    if self.editing == "Computers":
                        if self.value == 0:
                            calculation.computers_min -= 1
                        elif self.value == 1:
                            calculation.computers_max -= 1
                    if self.editing == "Bicycles":
                        if self.value == 0:
                            calculation.bicycles_min -= 1
                        elif self.value == 1:
                            calculation.bicycles_max -= 1
                    if self.editing == "Roller Skates":
                        if self.value == 0:
                            calculation.roller_skates_min -= 1
                        elif self.value == 1:
                            calculation.roller_skates_max -= 1
                    if self.editing == "Vitamins":
                        if self.value == 0:
                            calculation.vitamins_min -= 1
                        elif self.value == 1:
                            calculation.vitamins_max -= 1
                    if self.editing == "Pet Food":
                        if self.value == 0:
                            calculation.pet_food_min -= 1
                        elif self.value == 1:
                            calculation.pet_food_max -= 1
                    if self.editing == "Mattresses":
                        if self.value == 0:
                            calculation.mattresses_min -= 1
                        elif self.value == 1:
                            calculation.mattresses_max -= 1
                    if self.editing == "Yo-yos":
                        if self.value == 0:
                            calculation.yo_yos_min -= 1
                        elif self.value == 1:
                            calculation.yo_yos_max -= 1

                if event.key == pg.K_SPACE:
                    if self.value >= 1:
                        self.value = 0
                    else:
                        self.value += 1

                if event.key == pg.K_RETURN:
                    calculation.linear_programming()


g = Game()
while True:
    g.setup()
    g.neighborhood_view()
    g.run()

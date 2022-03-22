import pygame as pg
import pygame.mouse
from settings import *
import calculation


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
    text = font.render("Week: " + str(game.week), True, WHITE, BLACK)
    screen.blit(text, (270, 720))
    text = font.render("Day: " + str(game.day), True, WHITE, BLACK)
    screen.blit(text, (470, 720))
    text = font.render("Hour: " + str(game.hour), True, WHITE, BLACK)
    screen.blit(text, (670, 720))
    text = font.render("Minute: " + str(game.minute), True, WHITE, BLACK)
    screen.blit(text, (870, 720))


def show_settings(self, screen):
    font = pg.font.SysFont('Arial', 24)
    text = font.render("Hours/Days/Net Output", True, BLACK,
                       WHITE)
    screen.blit(text, (230, 210))
    font = pg.font.SysFont('Arial', 24)
    text = font.render("A. Lumber: " + str(calculation.lumber_hours) + " " + str(calculation.lumber_days) + " " + str(
        calculation.net_lumber_calc()), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 260))
    font = pg.font.SysFont('Arial', 24)
    text = font.render("B. Nuclear: " + str(calculation.nuclear_hours) + " " + str(calculation.nuclear_days) + " " + str(
        calculation.net_nuclear_calc()), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 310))
    font = pg.font.SysFont('Arial', 24)
    text = font.render("C. Agriculture: " + str(calculation.agriculture_hours) + " " + str(calculation.agriculture_days) + " " + str(
        calculation.net_agriculture_calc()), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 360))
    font = pg.font.SysFont('Arial', 24)
    text = font.render("D. Chemical: " + str(calculation.chemical_hours) + " " + str(calculation.chemical_days) + " " + str(
        calculation.net_chemical_calc()), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 410))
    font = pg.font.SysFont('Arial', 24)
    text = font.render("E. Mining: " + str(calculation.mining_hours) + " " + str(calculation.mining_days) + " " + str(
        calculation.net_mining_calc()), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 460))

    font = pg.font.SysFont('Arial', 24)
    text = font.render("Minimum/Maximum", True, BLACK,
                       WHITE)
    screen.blit(text, (580, 210))

    font = pg.font.SysFont('Arial', 16)
    text = font.render("1. Energy Drinks: " + str((calculation.energy_drinks_min, calculation.energy_drinks_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 250))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("2. Corn Flakes: " + str((calculation.corn_flakes_min, calculation.corn_flakes_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 275))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("3. TVs: " + str((calculation.TVs_min, calculation.TVs_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 300))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("4. Computers: " + str((calculation.computers_min, calculation.computers_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 325))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("5. Bicycles: " + str((calculation.bicycles_min, calculation.bicycles_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 350))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("6. Roller Skates: " + str((calculation.roller_skates_min, calculation.roller_skates_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 375))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("7. Vitamins: " + str((calculation.vitamins_min, calculation.vitamins_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 400))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("8. Pet Food: " + str((calculation.pet_food_min, calculation.pet_food_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 425))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("9. Mattresses: " + str((calculation.mattresses_min, calculation.mattresses_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 450))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("10. Yo-yos: " + str((calculation.yo_yos_min, calculation.yo_yos_max)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 475))


    font = pg.font.SysFont('Arial', 16)
    text = font.render("Editing: " + self.editing + " " + str(self.value), True, BLACK,
                       WHITE)
    screen.blit(text, (230, 540))

    font = pg.font.SysFont('Arial', 16)
    text = font.render(str([calculation.energy_drinks_to_make, calculation.corn_flakes_to_make, calculation.TVs_to_make, calculation.computers_to_make, calculation.bicycles_to_make, calculation.roller_skates_to_make, calculation.vitamins_to_make, calculation.pet_food_to_make, calculation.mattresses_to_make, calculation.yo_yos_to_make]), True, BLACK,
                       WHITE)
    screen.blit(text, (430, 540))


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


def show_settings(screen):
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
    text = font.render("1. Energy Drinks: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 250))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("2. Corn Flakes: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 275))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("3. TVs: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 300))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("4. Computers: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 325))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("5. Bicycles: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 350))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("6. Roller Skates: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 375))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("7. Vitamins: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 400))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("8. Pet Food: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 425))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("9. Mattresses: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 450))
    font = pg.font.SysFont('Arial', 16)
    text = font.render("10. Yo-yos: " + str((0, 999)), True, BLACK,
                       WHITE)
    screen.blit(text, (580, 475))

    bnd = [(0, float("inf")),  # Energy Drinks
           (0, float("inf")),  # Corn Flakes
           (0, float("inf")),  # TV
           (0, float("inf")),  # Computer
           (0, float("inf")),  # Bicycle
           (0, float("inf")),  # Roller Skates
           (0, float("inf")),  # Vitamins
           (0, float("inf")),  # Pet Food
           (0, float("inf")),  # Mattresses
           (0, float("inf"))  # Yo-yos
           ]

    # lumber_hours len(lumber_days)
    # nuclear_hours len(nuclear_days)
    # agriculture_hours len(agriculture_days)
    # chemical_hours len(chemical_days)
    # mining_hours len(mining_days)
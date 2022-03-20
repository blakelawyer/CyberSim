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
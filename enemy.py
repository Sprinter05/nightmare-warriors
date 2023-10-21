import pygame
import random


class enemy():
    def __init__(self, screen, delayTime,color, width, height):
        self.screen = screen
        self.delayTime = delayTime

        enemy = pygame.image.load("enemy.png")

    def display(self):
        pygame.draw.rect(rect,(0,0,255))

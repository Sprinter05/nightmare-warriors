import pygame
import random

class enemy():
    def __init__(self, screen, delayTime):
        self.screen = screen
        self.delayTime = delayTime
    def display(self):
        pygame.draw.rect(rect,(0,0,255))

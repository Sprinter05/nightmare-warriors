import pygame

gColor = pygame.Color(255,255,100)
gRect = 50
gWidth = 2

class Pointer():
    def __init__(self,screen,color,rect,width):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.width = width
    def display(self):
        return pygame.draw.ellipse(self.screen,self.color,self.rect,self.width)
import pygame

class Pointer():
    def __init__(self,screen,color,rect,width):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.width = width
    def display(self):
        return pygame.draw.ellipse(self.screen,self.color,self.rect,self.width)
gColor = pygame.Color(255,100,0)
gRect = pygame.Rect(0,0,100,100)
gWidth = 3
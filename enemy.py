import pygame
import random

class enemy:
    def __init__(self, screen,color, width, height):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height

        self.image = pygame.image.load("enemy.png")
        
        spawn = random.randrange(0,2)
        if spawn == 0:    
            self.x = -self.width
        else:
            self.x = screen.get_width()
        self.y = random.randrange(0,screen.get_height())

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
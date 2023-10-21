# Example file showing a circle moving on screen
import pygame

ppos = [640,360]
psize = [50,150]
pcolor="blue"
pvel = 500

# player class setup
class Player():
    def __init__(self,screen,pos,size,color):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color = color
    def show(self):
        return pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))

import pygame

gColor = pygame.Color(255,255,255)
gSize = 25
gWidth = 3

class Pointer():
    def __init__(self,screen,color,x,y,size,width):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.radius = 100
    def display(self):
        return pygame.draw.ellipse(self.screen,self.color,pygame.Rect(self.x,self.y,self.size,self.size),self.width)
    def getpos(self):
        return self.rect
    
class Bullet():
    def __init__(self,screen,x,y,ogx,ogy,vel,size):
        self.screen = screen
        self.x = x
        self.y = y
        self.ogx = ogx
        self.ogy = ogy
        self.vel = vel
        self.size = size
        self.vector = [self.x-self.ogx, self.y-self.ogy]
    def exist(self):
        if (self.x >= 1280 or self.y >= 720 or self.x < 0 or self.y < 0):
            return False
        else:
            return True
    def show(self):
        return pygame.draw.rect(self.screen, "red", pygame.Rect(self.x, self.y, self.size, self.size))
    def move(self):
        self.x -= self.vector[0] / self.vel
        self.y -= self.vector[1] / self.vel
import pygame
from vars import screen
from player import manolo

class Vida:
    def __init__(self,screen,life):
        self.screen = screen
        self.life= life
        self.x = 10
        self.y = 10
        self.image = pygame.image.load("./media/heart_1.png")
    def draw(self):
        offsetX = 0
        for i in range (0, self.life):
            self.screen.blit(self.image,(self.x + offsetX,self.y))
            offsetX += 70
    def hit(self):
        self.life -= 1
# Define object
vidas = Vida(screen,manolo.lifes)
        
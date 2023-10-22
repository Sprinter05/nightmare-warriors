import pygame

class Vida:
    def __init__(self,screen):
        self.screen = screen
        self.life=5
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
        
import pygame
import random

class enemy:
    def __init__(self, screen,color, width, height):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.velocidad_x = 5
        self.velocidad_y = 5
        self.speed = [3, 3]

        self.image = pygame.image.load("enemy.png")
        
        spawn = random.randrange(0,2)
        if spawn == 0:
            self.x = -self.width
        else:
            self.x = screen.get_width()
        self.y = random.randrange(0,screen.get_height())

    def draw(self,playerX,playerY,screen):
        screen.blit(self.image,(self.x,self.y))

        if (self.x > playerX):
            self.x -= 1
        if (self.x < playerX):
            self.x += 1
        if (self.y > playerY):
            self.y -= 1
        if (self.y < playerX):
            self.y += 1
        #update
        rect = self.image.get_rect()
        if rect.left < 0 or rect.right > 1280:
            self.speed[0] = -self.speed[0]
        if rect.top < 0 or rect.bottom > 720:
            self.speed[1] = -self.speed[1]
        rect.move_ip((self.speed[0], self.speed[1]))
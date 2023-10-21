# Example file showing a circle moving on screen
import pygame

ppos = [640,650]
psize = [32,32]
pcolor="blue"
pvel = 500

# player class setup
class Player():
    def __init__(self,screen,pos,size,color):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color = color
        self.isJump = False
        self.jumpCount = 10
    def show(self):
        return pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], 1))
    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.pos[1] -= self.jumpCount**2 * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
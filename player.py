import pygame
from vars import screen
from gun import Bullet

# player class setup
class Player():
    def __init__(self,screen,pos,size,color):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color = color
        self.vel = 500
        self.isJump = False
        self.jumpCount = 10
        self.lastShot = 0
        self.shootDelay = 100
        self.manoloImg = pygame.image.load("./media/manolo64.png")
    def show(self):
        screen.blit(self.manoloImg,(self.pos[0]-self.size[0]/2,self.pos[1]-self.size[1]/2))
        return pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], 1))
    def move(self,k,dt):
        if k[pygame.K_a]:
            self.pos[0] -= self.vel * dt
        if k[pygame.K_d]:
            self.pos[0] += self.vel * dt
        if k[pygame.K_SPACE]:
            self.isJump = True
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
    def shoot(self,buls,mira,mouses):
        if (mouses[0] and (pygame.time.get_ticks() - self.lastShot > self.shootDelay)):
            buls.append(Bullet(screen,self.pos[0]+self.size[0]/2, self.pos[1]+self.size[1]/2, mira.x, mira.y, 20 , 10))
            self.lastShot = pygame.time.get_ticks()
    def checkcol(self,fel):
        hitbox = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        enemy = pygame.Rect(fel.x,fel.y,32,32)
        damage = hitbox.colliderect(enemy)
        if damage:
            return True
        else:
            return False
# Define manolo
manolo = Player(screen, [640,650], [32,32], "blue")
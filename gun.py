import pygame
import math
import vars

class Pointer():
    def __init__(self,screen,color,x,y,size,width):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.radius = 200
    def display(self,man):
        mPosX, mPosY = pygame.mouse.get_pos()
        playx = man.pos[0]
        playy = man.pos[1]
        deltaX = mPosX - playx
        deltaY = mPosY - playy
        mAng = math.atan2(deltaY, deltaX)
        mVect = pygame.Vector2(self.radius*math.cos(mAng), self.radius*math.sin(mAng))
        playerP = pygame.Vector2(playx, playy)
        self.x = playerP.x + mVect.x + man.size[0]/2
        self.y = playerP.y + mVect.y + man.size[1]/2
        return pygame.draw.ellipse(self.screen,self.color,pygame.Rect(self.x,self.y,self.size,self.size),self.width)
    
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
    def checkhit(self,fel):
        enemy = pygame.Rect(fel.x,fel.y,32,32)
        bullet = pygame.Rect(self.x,self.y,self.size,self.size)
        hit = bullet.colliderect(enemy)
        if hit:
            return True
        else:
            return False
# Define crosshair object
mira = Pointer(vars.screen, pygame.Color(255,255,255), 0, 0, 25 , 3)
bullets = []
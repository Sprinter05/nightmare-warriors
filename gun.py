# Imports
import pygame
import math
import vars

# Class for the crosshair
class Pointer():
    # Define class variables
    def __init__(self,screen,color,x,y,size,width):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.radius = 200
    # Display crosshair on the screen
    def display(self,man):
        mPosX, mPosY = pygame.mouse.get_pos()
        playx = man.x
        playy = man.y
        # Vector math to make the crosshair always be in a circumference around the player
        deltaX = mPosX - playx
        deltaY = mPosY - playy
        mAng = math.atan2(deltaY, deltaX)
        mVect = pygame.Vector2(self.radius*math.cos(mAng), self.radius*math.sin(mAng))
        playerP = pygame.Vector2(playx, playy)
        # Modify crosshair position according to the calculated vector
        self.x = playerP.x + mVect.x + man.size/2
        self.y = playerP.y + mVect.y + man.size/2
        # Draw the crosshair on the screen
        return pygame.draw.ellipse(self.screen,self.color,pygame.Rect(self.x,self.y,self.size,self.size),self.width)
# Class for the bullet that the player shoots
class Bullet():
    # Define class variables
    def __init__(self,screen,x,y,ogx,ogy,vel,size):
        self.screen = screen
        self.x = x
        self.y = y
        self.ogx = ogx # Crosshair x
        self.ogy = ogy # Crosshair y
        self.vel = vel
        self.size = size
        self.vector = [self.x-self.ogx, self.y-self.ogy]
    # Check if the bullet goes out of the screen
    def exist(self):
        if (self.x >= 1280 or self.y >= 720 or self.x < 0 or self.y < 0):
            return False
        else:
            return True
    # Draw the bullet on the screen
    def show(self):
        return pygame.draw.rect(self.screen, "red", pygame.Rect(self.x, self.y, self.size, self.size))
    # Move towards the vector between the character and the crosshair
    def move(self):
        self.x -= self.vector[0] / self.vel
        self.y -= self.vector[1] / self.vel
    # Check collisions between bullet and enemies
    def checkEnemyHit(self,fel):
        enemy = pygame.Rect(fel.x,fel.y,32,32)
        bullet = pygame.Rect(self.x,self.y,self.size,self.size)
        hit = bullet.colliderect(enemy)
        if hit:
            return True
        else:
            return False
# Define objects
mira = Pointer(vars.screen, pygame.Color(255,255,255), 0, 0, 25 , 3) # Crosshair
bullets = [] # Bullets array
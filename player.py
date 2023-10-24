# Imports
import pygame
import vars

# Class for the player
class Player():
    # Define class variables
    def __init__(self,screen,x,y,size,color):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vel = 500
        self.isJump = False
        self.jumpCount = 10
        self.lastShot = 0
        self.shootDelay = 100
        self.lifes = 5
        self.kills = 0
        self.manoloImg = pygame.image.load("./media/manolo64.png")
    # Display player on the screen
    def show(self):
        # "Fake" square behind the sprite for collisions
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        self.screen.blit(self.manoloImg,(self.x-self.size/2,self.y-self.size/2)) # Actual sprite
    # Handle movement and jump with keys
    def move(self,k,dt):
        # Movement from left to right
        if k[pygame.K_a]:
            self.x -= self.vel * dt
        if k[pygame.K_d]:
            self.x += self.vel * dt
        # Make the player able to jump if the Space key is being pressed
        if k[pygame.K_SPACE]:
            self.isJump = True
    # Function that handles jumps
    def jump(self):
        # This is some "very complicated" math that I grabbed from somewhere but does the job
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
    # Handles shooting and adding bullets to the array
    def shoot(self,buls,mira,mouses,BullObj):
        # Check Left mouse click and delay between bullets
        if (mouses[0] and (pygame.time.get_ticks() - self.lastShot > self.shootDelay)):
            buls.append(BullObj(self.screen,self.x+self.size/2, self.y+self.size/2, mira.x, mira.y, 20 , 10)) # Add bullet to array
            self.lastShot = pygame.time.get_ticks() # Set latest shot
    # Check collisions between player and enemy
    def checkPlayerHit(self,fel):
        hitbox = pygame.Rect(self.x,self.y,self.size,self.size)
        enemy = pygame.Rect(fel.x,fel.y,32,32)
        damage = hitbox.colliderect(enemy)
        if damage:
            return True
        else:
            return False
# Define objets
manolo = Player(vars.screen, 640, 650, 32, "blue") # Player
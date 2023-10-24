# Imports
import pygame
import random
import vars

# Class for the enemy Felipe
class Felipe():
    # Define class variables
    def __init__(self, screen, color, width, height):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.wait = random.randrange(0, 100) * 20
        self.image = pygame.image.load("./media/enemy.png")
    # Spawn in a random part of the screen through "random" library
        spawn = random.randrange(0,3)
        if spawn == 0:
            self.x = -10
            self.y = random.randrange(0,self.screen.get_height())
        elif spawn == 1:
            self.x = self.screen.get_width()
            self.y = random.randrange(0,self.screen.get_height())
        else:
            self.y = 0
            self.x = random.randrange(0, self.screen.get_width())
    # Draw the enemy on the screen and move towards character
    def draw(self,playerX,playerY):
        # Wait between objects to spawn
        if (self.wait > 0):
            self.wait -= 1
            return
        # Move towards player in a random movement pattern
        if (self.x > playerX):
            self.x -= random.randrange(1,5)
        if (self.x < playerX):
            self.x += random.randrange(1,5)
        if (self.y > playerY):
            self.y -= random.randrange(1,5)
        if (self.y < playerY):
            self.y += random.randrange(1,5)
        # Show sprite on the screen
        self.screen.blit(self.image,(self.x,self.y))
# Define objects
felipes = [] # Felipes array
for f in range(0,20):
  felipes.append(Felipe(vars.screen,(0,0,255),500,500)) # Add felipes to the array
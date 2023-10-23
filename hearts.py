# Imports
import pygame
import player
import vars

# Class for the hearts drawn on the screen
class Vida:
    # Define class variables
    def __init__(self,screen,life):
        self.screen = screen
        self.life= life
        self.x = 10
        self.y = 10
        self.image = pygame.image.load("./media/heart_1.png")
    # Draw the heart image on the screen
    def draw(self):
        offsetX = 0 # Make hearts appear to the right of each other
        for i in range (0, self.life):
            self.screen.blit(self.image,(self.x + offsetX,self.y))
            offsetX += 70
    # Make a heart disappear if the character gets hit
    def hit(self):
        self.life -= 1
# Define objects
vidas = Vida(vars.screen,player.manolo.lifes) # Hearts on the screen        
        
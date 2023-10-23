import pygame
import hearts

# Define screen
screen = pygame.display.set_mode((1280, 720))
# Define objects
vidas = hearts.Vida(screen)
life = 5
kills = 0
bullets = []
felipes = []
import pygame
import gun
import hearts

# Define screen
screen = pygame.display.set_mode((1280, 720))
# Define objects
mira = gun.Pointer(screen, gun.gColor, 0, 0, gun.gSize ,gun.gWidth)
vidas = hearts.Vida(screen)
life = 5
kills = 0
bullets = []
felipes = []
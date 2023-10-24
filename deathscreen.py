# Imports
import pygame

# Function that handles the deathscreen and the game ending
def endGame(screen, kills):
    # Text layer 1 - Death
    screen.fill((144, 12, 63))
    fuente = pygame.font.Font(None, 100)
    image = pygame.image.load("./media/skull.png")
    text = "La has palmao"
    mensaje = fuente.render(text, 10, (255, 255, 255))
    screen.blit(mensaje, (screen.get_width() /2 - 230, screen.get_height()/2 - 100))
    # Text layer 2 - number of kills
    sKills = str(kills)
    text = "Mataste " + sKills + " Felipes"
    mensaje = fuente.render(text, 1, (255, 255, 255))
    screen.blit(mensaje, (screen.get_width() /2 - 230, screen.get_height()/2 + 100))
    screen.blit(image,(screen.get_width() /2,screen.get_height()/2))
    # Pygame stuff and quit if event is met
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit

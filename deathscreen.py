import pygame

def endGame(screen, kills):
    screen.fill((144, 12, 63))
    fuente = pygame.font.Font(None, 100)

    text = "La has palmao"
    mensaje = fuente.render(text, 10, (255, 255, 255))
    screen.blit(mensaje, (screen.get_width() /2 - 200, screen.get_height()/2 - 100))
    sKills = str(kills)
    text = "Mataste " + sKills + " Felipes"
    mensaje = fuente.render(text, 1, (255, 255, 255))
    screen.blit(mensaje, (screen.get_width() /2 - 200, screen.get_height()/2 + 100))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit
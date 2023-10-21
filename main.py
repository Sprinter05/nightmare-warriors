# Example file showing a circle moving on screen
import pygame
import gun
# import manolo

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")

clock = pygame.time.Clock()
running = True
deltaTime = 0

# Define objects
mira = gun.Pointer(screen, gun.gColor, gun.gRect,gun.gWidth)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black") # Clear Screen
    # Gun stuff
    mira.display()
    # Something
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
		# # player.move(0, screen)
		# player_pos += (0, 10);
    # if keys[pygame.K_s]:
		# # manolo.move(1, screen)
		# player_pos += (0, -10);
    # if keys[pygame.K_a]:
		# # manolo.move(3, screen)
		# player_pos += (-10, 0);
    # if keys[pygame.K_d]:
		# # manolo.move(2, screen)
		# player_pos += (10, 0);

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    deltaTime = clock.tick(60) / 1000

pygame.quit()

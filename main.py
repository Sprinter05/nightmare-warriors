# Example file showing a circle moving on screen
import pygame
import gun
import player

# import manolo

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")

clock = pygame.time.Clock()
running = True
deltaTime = 0
keys = pygame.key.get_pressed()

# Define objects
mira = gun.Pointer(screen, gun.gColor, pygame.Rect(0, 0, gun.gSize, gun.gSize) ,gun.gWidth)
manolo = player.Player(screen, player.ppos, player.psize, player.pcolor)

while running:
    # Poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    screen.fill("black")
    # Player stuff
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      manolo.pos[0] -= 300 * deltaTime
    if keys[pygame.K_d]:
      manolo.pos[0] += 300 * deltaTime
    manolo.show()
    # Gun stuff
    mPosX, mPosY = pygame.mouse.get_pos()
    mPosX -= gun.gSize/2
    mPosY -= gun.gSize/2
    mira.rect = (mPosX, mPosY, gun.gSize, gun.gSize)
    mira.display()
    # Flip and deltaTime garbage
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

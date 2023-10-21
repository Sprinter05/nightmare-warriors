# Example file showing a circle moving on screen
import pygame
import gun
import player

# import manolo

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")

# Vars
clock = pygame.time.Clock()
running = True
deltaTime = 0
keys = pygame.key.get_pressed()
# Time get
delay = 50
lastShot = 0

# Define objects
mira = gun.Pointer(screen, gun.gColor, pygame.Rect(0, 0, gun.gSize, gun.gSize) ,gun.gWidth)
manolo = player.Player(screen, player.ppos, player.psize, player.pcolor)
bullets = []

while running:
    # Poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    screen.fill("black")
    # Update vars
    keys = pygame.key.get_pressed()
    # Player stuff
    if keys[pygame.K_a]:
      manolo.pos[0] -= player.pvel * deltaTime
    if keys[pygame.K_d]:
      manolo.pos[0] += player.pvel * deltaTime
    manolo.show()
    # Gun stuff
    mPosX, mPosY = pygame.mouse.get_pos()
    mPosX -= gun.gSize/2
    mPosY -= gun.gSize/2
    mira.rect = (mPosX, mPosY, gun.gSize, gun.gSize)
    mira.display()
    # Bullet stuff
    if (keys[pygame.K_SPACE] and (pygame.time.get_ticks() - lastShot > delay)):
       bullets.append(gun.Bullet(screen,manolo.pos[0]+manolo.size[0]/2, manolo.pos[1]+manolo.size[1]/2, mPosX, mPosY, 20 , 10))
       lastShot = pygame.time.get_ticks()
    for b in bullets:
        if b.exist():
           b.show()
           b.move()
        else:      
           bullets.remove(b)
    # Flip and deltaTime garbage
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

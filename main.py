# Example file showing a circle moving on screen
import pygame
import gun
import player
import math
import enemy

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
delay = 100
lastShot = 0
radius = 200

# Define objects
manolo = player.Player(screen, player.ppos, player.psize, player.pcolor)
manoloImg = pygame.image.load("./Manolo64.png")
mira = gun.Pointer(screen, gun.gColor, 0, 0, gun.gSize ,gun.gWidth)
bullets = []
felipes = []
for f in range(0,20):
  felipes.append(enemy.enemy(screen,(0,0,255),500,500))




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
    screen.blit(manoloImg, (manolo.pos[0]-manolo.size[0]/2,manolo.pos[1]-manolo.size[1]/2))
    # Gun stuff
    playx = manolo.pos[0]
    playy = manolo.pos[1]
    mPosX, mPosY = pygame.mouse.get_pos()
    # Very complicated math no one should have to touch
    deltaX = mPosX - playx
    deltaY = mPosY - playy
    mAng = math.atan2(deltaY, deltaX)
    mVect = pygame.Vector2(radius*math.cos(mAng), radius*math.sin(mAng))
    playerP = pygame.Vector2(playx, playy)
    mira.x = playerP.x + mVect.x + manolo.size[0]/2
    mira.y = playerP.y + mVect.y + manolo.size[1]/2
    # Check if gun out of radius
    mira.display()
    # Bullet stuff
    if (keys[pygame.K_SPACE] and (pygame.time.get_ticks() - lastShot > delay)):
       bullets.append(gun.Bullet(screen,manolo.pos[0]+manolo.size[0]/2, manolo.pos[1]+manolo.size[1]/2, mira.x, mira.y, 20 , 10))
       lastShot = pygame.time.get_ticks()
    for b in bullets:
        if b.exist():
           b.show()
           b.move()
        else:      
           bullets.remove(b)
    # Felipe
    for f in felipes:
      f.draw(manolo.pos[0],manolo.pos[1],screen)
    # Flip and deltaTime garbage
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

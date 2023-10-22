# Example file showing a circle moving on screen
import pygame
import gun
import player
import math
import enemy
import random
import hearts
import deathscreen

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")
bgimg = pygame.image.load("./media/background.jpg")
bgimg = pygame.transform.scale(bgimg, (1280, 720))
# Vars
clock = pygame.time.Clock()
running = True
deltaTime = 0
life = 5
keys = pygame.key.get_pressed()
# Time get
delay = 100
lastShot = 0
radius = 200
kills = 0

# Define objects
manolo = player.Player(screen, player.ppos, player.psize, player.pcolor)
manoloImg = pygame.image.load("./media/manolo64.png")
mira = gun.Pointer(screen, gun.gColor, 0, 0, gun.gSize ,gun.gWidth)
bullets = []
felipes = []
for f in range(0,20):
  felipes.append(enemy.enemy(screen,(0,0,255),500,500))
vidas = hearts.Vida(screen)

def checkcol(man,fel):
    #Collision
    hitbox = pygame.Rect(man.pos[0],man.pos[1],man.size[0],man.size[1])
    enemy = pygame.Rect(fel.x,fel.y,32,32)
    damage = hitbox.colliderect(enemy)
    if damage:
       return True
    else:
       return False
def checkhit(b,fel):
  enemy = pygame.Rect(fel.x,fel.y,32,32)
  bullet = pygame.Rect(b.x,b.y,b.size,b.size)
  hit = bullet.colliderect(enemy)
  if hit:
     return True
  else:
     return False
while running:
    # Poll events
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               manolo.isJump = True
    # Clear screeen
    rectImg = bgimg.get_rect()
    rectImg = rectImg.move((0, 0))
    screen.blit(bgimg, rectImg)
    # Update vars
    keys = pygame.key.get_pressed()
    mouses = pygame.mouse.get_pressed()
    # Player stuff
    if keys[pygame.K_a]:
      manolo.pos[0] -= player.pvel * deltaTime
    if keys[pygame.K_d]:
      manolo.pos[0] += player.pvel * deltaTime
    
    manolo.show()
    manolo.jump()
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
    if (mouses[0] and (pygame.time.get_ticks() - lastShot > delay)):
       bullets.append(gun.Bullet(screen,manolo.pos[0]+manolo.size[0]/2, manolo.pos[1]+manolo.size[1]/2, mira.x, mira.y, 20 , 10))
       lastShot = pygame.time.get_ticks()
    for b in bullets:
        for f in felipes:
           if checkhit(b,f):
              bullets.remove(b)
              felipes.remove(f)
              felipes.append(enemy.enemy(screen,(0,0,255),500,500))
              if random.randrange(0,5) == 0:
                felipes.append(enemy.enemy(screen,(0,0,255),500,500))
              kills += 1
              break
        if b.exist():
           b.show()
           b.move()
        else:
           if b in bullets:
            bullets.remove(b)
    # Felipe
    for f in felipes:
      f.draw(manolo.pos[0],manolo.pos[1],screen)
      if checkcol(manolo, f):
        life -= 1
        vidas.hit()
        #meter vergas eiqui
        felipes.remove(f)
        felipes.append(enemy.enemy(screen,(0,0,255),500,500))
        if random.randrange(0,5) == 0:
          felipes.append(enemy.enemy(screen,(0,0,255),500,500))

    if life <= 0:
      deathscreen.endGame(screen,kills)
      break
    # Flip and deltaTime garbage
    vidas.draw()
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

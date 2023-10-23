import pygame
from player import manolo
from gun import mira
import enemy
import random
import deathscreen
from vars import screen,vidas,bullets,felipes,life,kills # super temporal

# pygame setup
pygame.init()
pygame.display.set_caption("Nightmare warriors")
bgimg = pygame.image.load("./media/background.jpg")
# pygame clock shenaningans
clock = pygame.time.Clock()
running = True
deltaTime = 0

for f in range(0,20):
  felipes.append(enemy.enemy(screen,(0,0,255),500,500))

def checkhit(b,fel):
  enemy = pygame.Rect(fel.x,fel.y,32,32)
  bullet = pygame.Rect(b.x,b.y,b.size,b.size)
  hit = bullet.colliderect(enemy)
  if hit:
     return True
  else:
     return False
# Main event
while running:
    # Poll events
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    screen.blit(bgimg, (0,0))
    # Update inputs
    keys = pygame.key.get_pressed()
    mouses = pygame.mouse.get_pressed()
    # Run player functions
    manolo.show()
    manolo.move(keys,deltaTime)
    manolo.shoot(bullets, mira, mouses)
    manolo.jump()
    # Display crosshair
    mira.display(manolo)
    # Bullet stuff
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
      if manolo.checkcol(f):
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

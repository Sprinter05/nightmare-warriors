# Import everything necessary
import pygame
from player import manolo
from gun import mira
from hearts import vidas
import enemy
import random
import deathscreen
from vars import screen,bullets,felipes,kills # super temporal

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

# Game functions
def killEnemy(buls,fels,scr,man):
   for b in buls:
        for f in fels:
           if b.checkhit(f):
              buls.remove(b)
              fels.remove(f)
              fels.append(enemy.enemy(scr,(0,0,255),500,500))
              if random.randrange(0,5) == 0:
                fels.append(enemy.enemy(scr,(0,0,255),500,500))
              man.kills += 1
              break
        if b.exist():
           b.show()
           b.move()
        else:
           if b in buls:
            buls.remove(b)
def endlessWave(man,fels,scr,vidas):
   for f in fels:
      f.draw(man.pos[0],man.pos[1],scr)
      if manolo.checkcol(f):
        man.lifes -= 1
        vidas.hit()
        fels.remove(f)
        fels.append(enemy.enemy(scr,(0,0,255),500,500))
        if random.randrange(0,5) == 0:
          fels.append(enemy.enemy(scr,(0,0,255),500,500))

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
    # Enemy stuff
    killEnemy(bullets,felipes,screen,manolo)
    endlessWave(manolo,felipes,screen,vidas)
    if manolo.lifes <= 0:
      deathscreen.endGame(screen,manolo.kills)
      break
    # Flip and deltaTime garbage
    vidas.draw()
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

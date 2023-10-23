import pygame
import random
# Define screen
screen = pygame.display.set_mode((1280, 720))
# Define functions
def killEnemy(buls,fels,scr,man,EnemyObj):
   for b in buls:
        for f in fels:
           if b.checkhit(f):
              buls.remove(b)
              fels.remove(f)
              fels.append(EnemyObj(scr,(0,0,255),500,500))
              if random.randrange(0,5) == 0:
                fels.append(EnemyObj(scr,(0,0,255),500,500))
              man.kills += 1
              break
        if b.exist():
           b.show()
           b.move()
        else:
           if b in buls:
            buls.remove(b)
def endlessWave(man,fels,scr,vidas,EnemyObj):
   for f in fels:
      f.draw(man.pos[0],man.pos[1])
      if man.checkcol(f):
        man.lifes -= 1
        vidas.hit()
        fels.remove(f)
        fels.append(EnemyObj(scr,(0,0,255),500,500))
        if random.randrange(0,5) == 0:
          fels.append(EnemyObj(scr,(0,0,255),500,500))

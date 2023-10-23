# Imports
import pygame
import random

# Define screen
screen = pygame.display.set_mode((1280, 720))

# Define functions
# Function that handles kills if an enemy is hit
def killEnemy(buls,fels,scr,man,EnemyObj):
   for b in buls:
        for f in fels:
           if b.checkEnemyHit(f): # Collision between bullet and enemy
              buls.remove(b)
              fels.remove(f)
              # Add more enemies to the array whenever one is killed
              fels.append(EnemyObj(scr,(0,0,255),500,500))
              # Add another enemy by lottery to increase difficulty
              if random.randrange(0,5) == 0:
                fels.append(EnemyObj(scr,(0,0,255),500,500))
              man.kills += 1 # Increase kill count
              break
        # Check if bullet is out of bounds, if not, display on the screen
        if b.exist():
           b.show()
           b.move()
        else: # Remove bullet if out of bounds
           if b in buls:
            buls.remove(b)
# Function that handles enemies hitting the player
def enemyHits(man,fels,scr,vidas,EnemyObj):
   for f in fels:
      f.draw(man.x,man.y) # Draw the enemy from the array
      # Check collisions between player and enemies
      if man.checkPlayerHit(f):
        man.lifes -= 1
        vidas.hit()
        fels.remove(f) # Remove from array
        # Add another enemy to the array when it hits the player
        fels.append(EnemyObj(scr,(0,0,255),500,500))
        # Also add more enemies by lottery
        if random.randrange(0,5) == 0:
          fels.append(EnemyObj(scr,(0,0,255),500,500))

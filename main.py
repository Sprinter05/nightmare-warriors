# Import libraries
import pygame
# Import object files
import player
import enemy
import gun
import hearts
# Import others
import deathscreen
import vars

# Pygame setup and load images
pygame.init()
pygame.display.set_caption("Nightmare warriors")
bgimg = pygame.image.load("./media/background.jpg")
# Pygame clock and deltaTime shenaningans
clock = pygame.time.Clock()
running = True
deltaTime = 0
# Main loop
while running:
    # Poll quit event
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
    # Clear screeen so that frames are clean
    vars.screen.blit(bgimg, (0,0))
    # Update input arrays
    keys = pygame.key.get_pressed()
    mouses = pygame.mouse.get_pressed()
    # Run player functions
    player.manolo.show()
    player.manolo.move(keys,deltaTime)
    player.manolo.shoot(gun.bullets, gun.mira, mouses, gun.Bullet)
    player.manolo.jump()
    # Run crosshair functions
    gun.mira.display(player.manolo)
    # Run hearts on the screen functions
    hearts.vidas.draw()
    # Run different game functions
    vars.killEnemy(gun.bullets,enemy.felipes,vars.screen,player.manolo,enemy.Felipe) # Enemy is killed function
    vars.enemyHits(player.manolo,enemy.felipes,vars.screen,hearts.vidas,enemy.Felipe) # Player is hit function
    # Trigger death if dead
    if player.manolo.lifes <= 0:
      deathscreen.endGame(vars.screen,player.manolo.kills)
      break # Avoids errors on close
    # Flip and deltaTime garbage, also clock stuff
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

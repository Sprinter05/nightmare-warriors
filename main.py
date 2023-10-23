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

# pygame setup
pygame.init()
pygame.display.set_caption("Nightmare warriors")
bgimg = pygame.image.load("./media/background.jpg")
# pygame clock shenaningans
clock = pygame.time.Clock()
running = True
deltaTime = 0
# Main event
while running:
    # Poll events
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    vars.screen.blit(bgimg, (0,0))
    # Update inputs
    keys = pygame.key.get_pressed()
    mouses = pygame.mouse.get_pressed()
    # Run player functions
    player.manolo.show()
    player.manolo.move(keys,deltaTime)
    player.manolo.shoot(gun.bullets, gun.mira, mouses, gun.Bullet)
    player.manolo.jump()
    # Display crosshair
    gun.mira.display(player.manolo)
    # Display lifes
    hearts.vidas.draw()
    # Enemy stuff
    vars.killEnemy(gun.bullets,enemy.felipes,vars.screen,player.manolo,enemy.Enemy)
    vars.endlessWave(player.manolo,enemy.felipes,vars.screen,hearts.vidas,enemy.Enemy)
    # Triger death if dead
    if player.manolo.lifes <= 0:
      deathscreen.endGame(vars.screen,player.manolo.kills)
      break
    # Flip and deltaTime garbage
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()

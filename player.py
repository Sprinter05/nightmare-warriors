# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = (50,150)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Screen preparing
    screen.fill("Black")
 
    
    color="Blue"
    player = pygame.Rect(player_pos,player_size)
    pygame.draw.rect(screen,color,(player_pos,player_size))
    
    #keybinds      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
   
    #collisions
    enemy = pygame.mouse.get_pos()

    collide = player.collidepoint(enemy)
    if collide == True:
        color="Red"
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
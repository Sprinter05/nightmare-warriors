# Imports
import pygame

# Init start variables
pygame.font.init() 
my_font = pygame.font.SysFont('Ubuntu Mono', 30)
logo = pygame.image.load("./media/logo.png")
logo = pygame.transform.scale(logo, (900, 78))
# Init a fake game that will then run the actual game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")
running = True
clock = pygame.time.Clock()
running = True
deltaTime = 0
# Variables to animate the "Press Space" text
anim = True
lastAnim = pygame.time.get_ticks()
delay = 500

# Loop the fake game until Space is pressed
while running:
    # Poll quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    screen.fill("black")
    # Render logo
    rectLogo = logo.get_rect()
    rectLogo = rectLogo.move((180, 200))
    screen.blit(logo, rectLogo)
    # Render "Press Space" text
    text_surface = my_font.render('PRESS SPACE TO START', False, (255, 255, 255))
    # Animate the text
    if anim:
        screen.blit(text_surface, (530,500))
    if pygame.time.get_ticks() - lastAnim > delay:
        if anim:
            anim = False
            lastAnim = pygame.time.get_ticks()
        else:
            anim = True
            lastAnim = pygame.time.get_ticks()
    # Detech key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        import main 
        main # Run the actual game
        break
    # Pygame clock and deltaTime stuff
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()
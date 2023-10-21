import pygame

# Init font
pygame.font.init() 
my_font = pygame.font.SysFont('Ubuntu Mono', 30)
# Logo
logo = pygame.image.load("./Nightmare Warriors big.png")
logo = pygame.transform.scale(logo, (900, 78))
# Init game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nightmare warriors")
running = True
clock = pygame.time.Clock()
running = True
deltaTime = 0
anim = True
lastAnim = pygame.time.get_ticks()
delay = 500
# Loop until Space pressed
while running:
    # Poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear screeen
    screen.fill("black")
    # Render logo
    rectLogo = logo.get_rect()
    rectLogo = rectLogo.move((180, 200))
    screen.blit(logo, rectLogo)
    # Render text
    text_surface = my_font.render('PRESS SPACE TO START', False, (255, 255, 255))
    if anim:
        screen.blit(text_surface, (530,500))
    if pygame.time.get_ticks() - lastAnim > delay:
        if anim:
            anim = False
            lastAnim = pygame.time.get_ticks()
        else:
            anim = True
            lastAnim = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    # Detect key press
    if keys[pygame.K_SPACE]:
        import main
        main
        break
    # idk pygame stuff
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000
pygame.quit()
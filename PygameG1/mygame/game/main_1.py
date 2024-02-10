import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

main_cat = pygame.image.load("img/cat2.png")
main_cat = pygame.transform.scale(main_cat, (90,70))

main_fon = pygame.image.load("img/fon.jpg")
main_fon = pygame.transform.scale(main_fon, (800,600))

bullet = pygame.image.load("img/banan-PhotoRoom.png-PhotoRoom.png")
bullet = pygame.transform.scale(bullet, (50,50))

land = pygame.image.load("img/land.png")
land = pygame.transform.scale(land,(screen_width,250))

x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
speed = 0.05
x_cat, y_cat = 10, 80

stap_sound = pygame.mixer.Sound("sound/blizkiy-odinarnyiy-chtkiy-shag-po-staromu-polu.mp3")
fon_sound = pygame.mixer.Sound("sound/Corporate-Business.mp3")




while True:
    screen.blit(main_fon, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(bullet, (100, 100))

    screen.blit(land, (0,470))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_cat += speed
        # stap_sound.play()
    if keys[pygame.K_a]:
        x_cat -= speed
        # stap_sound.play()
    if keys[pygame.K_s]:
        y_cat += speed
        # stap_sound.play()
    if keys[pygame.K_w]:
        y_cat -= speed
        # stap_sound.play()

    screen.blit(main_cat, (x_cat, y_cat))

    if keys[pygame.K_SPACE]:
        screen.blit(bullet, (0, 100))



    pygame.display.update()
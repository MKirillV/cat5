import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 20)
font2 = pygame.font.SysFont("Kristen ITC", 30)

hero_img = pygame.image.load("img/cat2.png")
hero_img = pygame.transform.scale(hero_img, (50,50))

hero_img_rect = hero_img.get_rect()
hero_img = pygame.transform.rotate(hero_img, 100)
rot_hero_img = hero_img.get_rect(center=hero_img_rect.center)


fon_img = pygame.image.load("img/fon.jpg")
fon_img = pygame.transform.scale(fon_img, (800,600))

sound_stap = pygame.mixer.Sound("sound/blizkiy-odinarnyiy-chtkiy-shag-po-staromu-polu.mp3")



x,y = 140, 40
x1,y1 = 140, 280
x2,y2 = 140, 280
x3,y3 = 140, 280
speed = 0.1
rot = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(fon_img, (0, 0))
    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))
    text2 = font2.render("Welcome to game2!!", True, (110, 10, 100))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("Welcome to game3!!", True, (110, 110, 100))
    screen.blit(textadsf, (x2, y2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        # x3 += speed

        sound_stap.play()
    if keys[pygame.K_a]:
        x3 -= speed
        sound_stap.play()
    if keys[pygame.K_s]:
        y3 += speed
        sound_stap.play()
    if keys[pygame.K_w]:
        y3 -= speed
        sound_stap.play()
    if not keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_w]:
        sound_stap.stop()


    screen.blit(hero_img, rot_hero_img)


    pygame.display.update()

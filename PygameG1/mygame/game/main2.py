import pygame
import random


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Bradley Hand ITC", 50)
img = pygame.image.load("img/1.jpg")

img = pygame.transform.scale(img, (50,50))
img2 = pygame.transform.scale(img, (30,30))

speed = 0.1
img_x = 40
img_y = 90
img_x2 = 40
img_y2 = 90

def hero():
    global img_y
    global img_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print("вверх")
        img_y -= speed
    if keys[pygame.K_DOWN]:
        print("вниз")
        img_y += speed
    if keys[pygame.K_LEFT]:
        print("влево")
        img_x -= speed
    if keys[pygame.K_RIGHT]:
        print("вправо")
        img_x += speed

    screen.blit(img, (img_x, img_y))

def anty_hero():
    global img_y2
    global img_x2
    keys = pygame.key.get_pressed()

    img_y2 -= (random.randint(-1, 1))/10
    img_x2 += random.randint(-1, 1)

    screen.blit(img2, (img_x2, img_x2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    text = font.render("START", True, (0,255,0))
    screen.blit(text, (40, 70))
    text = font.render("STOP", True, (100, 255, 0))
    screen.blit(text, (40, 270))

    hero()
    anty_hero()


    pygame.display.update()



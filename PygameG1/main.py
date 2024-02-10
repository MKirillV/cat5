import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))
    text2 = font2.render("Welcome to game2!!", True, (110, 10, 100))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("Welcome to game3!!", True, (110, 110, 100))
    screen.blit(textadsf, (x2, y2))

    pygame.display.update()

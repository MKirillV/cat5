
class Hero():
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
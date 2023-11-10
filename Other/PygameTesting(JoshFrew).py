import pygame
import random
pygame.init()

displaywidth = 600
displayheight = 600

win = pygame.display.set_mode((displaywidth, displayheight))
my_font = pygame.font.SysFont("Jokerman", 60, False, False, None)

pygame.display.set_caption("Test Pygame")

x = 295
y = 295
width = 10
height = 10
vel = 2
run = True
GameOver = False
spawn = 0
doemov = True
doimov = True

e_y = 1
e_width = 20
e_height = 30
e_vel = vel - 0.75


class Enemy:

    def __init__(self, startx, starty, e_width, e_height, e_vel):
        self.x = startx
        self.y = starty
        self.width = e_width
        self.height = e_height
        self.vel = e_vel

    def move(self, x, y):
        # print("test")
        self.y += self.vel
        if self.y < y:
            if self.x < x - 5:
                self.x += self.vel
            elif self.x > x - 5:
                self.x -= self.vel
        pygame.draw.rect(win, (255, 50, 50), (self.x, self.y, self.width, self.height))

    def doemov(self, displayheight, x, y):
        # print("test")
        if self.y < displayheight and doemov:
            self.move(x, y)


class Hero:

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def move(self):
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel
        if keys[pygame.K_w]:
            self.y -= self.vel
        if keys[pygame.K_s]:
            self.y += self.vel
        pygame.draw.rect(win, (255, 0, 255), (self.x, self.y, self.width, self.height))

H1 = Hero(x, y, width, height, vel)

while run:
    pygame.time.delay(5)
    win.fill((10, 10, 10))
    keys = pygame.key.get_pressed()

    if spawn % 600 == 0:
        E1 = Enemy(random.randint(1, 600), e_y, e_width, e_height, e_vel)
    elif spawn % 600 == 200:
        E2 = Enemy(random.randint(1, 600), e_y, e_width, e_height, e_vel)
    elif spawn % 600 == 400:
        E3 = Enemy(random.randint(1, 600), e_y, e_width, e_height, e_vel)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False

    if doimov:
        H1.move()

    try:
        E1.doemov(displayheight, x, y)
    except:
        pass
    try:
        E2.doemov(displayheight, x, y)
    except:
        pass
    try:
        E3.doemov(displayheight, x, y)
    except:
        pass

    if H1.x < 0 or H1.x > displaywidth or H1.y < 0 or H1.y > displayheight:
        GameOver = True

    spawn += 1

    if GameOver:
        End_message = my_font.render("Game Over!", 1, (255, 255, 0))
        win.blit(End_message, (125, 100))
        doemov = False

    pygame.display.update()


pygame.quit()

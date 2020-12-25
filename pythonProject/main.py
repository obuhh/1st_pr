import pygame
import random

class Button:
    def __init__(self, x, y, w, h, unpr, pr, act, action, text):
        self.x = x
        self.y = y
        self.unpr = unpr
        self.pr = pr
        self.act = act
        self.h = h
        self.w = w
        self.action = action
        self.text = text
    def draw(self):
        pygame.draw.rect(win, self.unpr, (self.x, self.y, self.w, self.h))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.w:
            if self.y < mouse[1] < self.y + self.h:
                if click[0]:
                    pygame.draw.rect(win, self.pr, (self.x + 10, self.y + 10, self.w - 20, self.h - 20))
                    if self.action is not None:
                        self.action()
                else:
                    pygame.draw.rect(win, self.act, (self.x + 10, self.y + 10, self.w - 20, self.h - 20))
        print_text(self.text, self.x + 20, self.y + 10)

pygame.init()
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("nian")
wp = [pygame.image.load('skin/wp.png') ,pygame.image.load('skin/bp.png')]
men = pygame.image.load('skin/menu7.png')

a = []
for i in range(72):
    a.append([0] * 102)

a[20][10] = 1
a[20][11] = 1
a[20][12] = 1
a[19][12] = 1
a[18][11] = 1

a[5][5] = 1
a[5][6] = 1
a[5][7] = 1

a[30][30] = 1
a[30][29] = 1
a[30][31] = 1
a[29][30] = 1
a[30][36] = 1
a[30][35] = 1
a[30][37] = 1
a[29][36] = 1

b = []
for i in range(72):
    b.append([0] * 102)

def print_text(message, x, y, font_color = (0, 0, 0), font_size = 30):
    #font_type = pygame.font.Font(font_type, font_size)
    font = pygame.font.SysFont('comicsansms', font_size)
    text = font.render(message, 1, font_color)
    win.blit(text, (x, y))

def drawWindow():
    for i in range(1, 71):
        for j in range(1, 101):
            win.blit(wp[a[i][j]], ((j-1)*10, (i-1)*10))

def recountMas():
    for i in range(1, 71):
        for j in range(1, 101):
            sum = a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j - 1] + a[i][j + 1] + a[i + 1][j - 1] + a[i + 1][j] + a[i + 1][j + 1]
            if a[i][j] == 0:
                if sum == 3:
                    b[i][j] = 1
            if a[i][j] == 1:
                b[i][j] = 1
                if (sum == 3) or (sum == 2):
                    b[i][j] = 1
                #else:
                #    b[i][j] = 0
    for i in range(1, 71):
        for j in range(1, 101):
            a[i][j] = b[i][j]

def delete():
    for i in range(1, 71):
        for j in range(1, 101):
            a[i][j] = 0
            b[i][j] = 0

def ran():
    for i in range(1, 71):
        for j in range(1, 101):
            a[i][j] = random.randint(0, 1)
            b[i][j] = 0

button_rand = Button(90, 120, 140, 70, (255, 211, 155), (236, 74, 180), (255, 164, 255), ran, 'random')
button_delete = Button(250, 120, 130, 70, (255, 211, 155), (236, 74, 180), (255, 164, 255), delete, 'delete')

def menu():
    kek = True
    while kek:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            kek = False
        drawWindow()
        win.blit(men, (0, 200))
        button_rand.draw()
        button_delete.draw()
        pygame.display.update()

drawWindow()
menu()
run = True
fl = False
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        fl = False
        menu()
    if keys[pygame.K_n]:
        fl = True
    if keys[pygame.K_m]:
        fl = False
    if fl or keys[pygame.K_SPACE]:
        recountMas()
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        x = ((pos[1] - 1) // 10) + 1
        y = ((pos[0] - 1) // 10) + 1
        a[x][y] = 1
    if pressed[2]:
        x = ((pos[1] - 1) // 10) + 1
        y = ((pos[0] - 1) // 10) + 1
        a[x][y] = 0
    drawWindow()
    pygame.display.update()
pygame.quit()
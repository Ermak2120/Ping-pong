from pygame import *
from random import *
from time import time as timer

class GameSprait(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.delay = 0

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprait):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_w  - 80:
            self.rect.y += self.speed
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_w  - 80:
            self.rect.y += self.speed

init()
back = (200, 255, 255)
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('ping.png', 30, 200, 50, 150, 4)
racket2 = Player('ping.png', 520, 200, 50, 150, 4)
ball = Player('pong.png', 200, 200, 50, 50, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.updateL()
        racket2.update()
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
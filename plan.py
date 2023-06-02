# импорты
from pygame import *
from random import randint 
gameover = False
# класс GameSprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super(). __init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс Player
class Player(GameSprite):
    def update(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_passed[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed


class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = 0
# Описание сцен

background = (300, 300, 300)
win_height = 500
win_width = 700 
window = display.set_mode((win_width, win_height))
background = (200, 255, 255)

racket1 = Player("34696-2-bamboo-stick.png", 0 , 300, 30, 100, 4)
racket2 = Player("34696-2-bamboo-stick.png", 670, 300, 30, 100, 4)
ball = Ball("1670473154_kartinkof-club-p-kartinki-bomzha-1.png",150, 150, 100, 100, 4)
clock = time.Clock()
while not gameover:
    for e in event.get():
        if e.type == QUIT:
            gameover = True
    window.fill(background)
    racket1.update()
    racket2.update()
    ball.update()
    racket1.reset()
    racket2.reset()
    ball.reset()
    

# Флаги состояния игры(цикл while)
# игра продолжается если 
#     не нажата кнопка "Завершить игру"
#     не закрыто приложение
# перемещение ракеток 
# обновление спрайтов и сцены
    display.update()
clock.tick(40)

# импорты
from pygame import *
from random import randint 


gameover = False
speed_x = 3
speed_y = 3
back = (200, 255, 255) 



# класс GameSprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс Player
class Player(GameSprite):
    def update_two(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_DOWN] and self.rect.y < win_height -100:
            self.rect.y += self.speed
    def update_one(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_s] and self.rect.y < win_height -100:
            self.rect.y += self.speed




# class Ball(GameSprite):
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.y > win_height:
#             self.rect.y = 0
#             self.rect.x = 0
# # Описание сцен

background = (300, 300, 300)
win_height = 500
win_width = 700 
window = display.set_mode((win_width, win_height))
background = (200, 255, 255)

racket1 = Player("34696-2-bamboo-stick.png", 0 , 300, 30, 100, 10)
racket2 = Player("34696-2-bamboo-stick.png", 670, 300, 30, 100, 10)
ball = Player("1670473154_kartinkof-club-p-kartinki-bomzha-1.png",150, 150, 100, 100, 10)
game_over = transform.scale(image.load("game_over.png"), (450, 450))

clock = time.Clock()
game = True 
finish = False

while game:
    window.fill(background)
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        racket1.update_one()
        racket2.update_two()
        racket1.reset()
        racket2.reset()
        ball.reset()

    if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
        speed_x *= -1
    
    if ball.rect.y > 400 or ball.rect.y < 0:
        speed_y *= -1
    
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x < 0 or ball.rect.x > 670:
        finish = True
        window.blit(game_over,(130,30))
        


# Флаги состояния игры(цикл while)   
# игра продолжается если 
#     не нажата кнопка "Завершить игру"
#     не закрыто приложение
# перемещение ракеток 
# обновление спрайтов и сцены
    display.update()
    clock.tick(40)

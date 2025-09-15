from pygame import *

screenwidth = 700
screenheight = 500

FPS = 60

game_on = True
finish = False

window = display.set_mode((screenheight, screenwidth))
display.set_caption('Catcher game')

background = transform.scale(image.load('bg.jpg'), (screenwidth, screenheight))
mixer.init()
mixer.music.load('')
mixer.music.play()

clock = time.CLock()

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self)
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < screenheight - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < screenwidth - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < screenheight - 80:
            self.rect.y += self.speeed

catcher = Player()
runner = Player()

font.init()
font = font.Font(None, 35)
lose = font.render('Catcher wins!')


while game_on:
    for e in even.get():
        if e.type == QUIT:
            game_on = False
    if finish != True:
        window.fill(background)
        player1.update_l()
        player2.update_r()

        if sprite collide_rect(player1, player2):
            finish = True
            window.blit(lose(200, 200))
            game_over = True
    window.blit(background, (0, 0))

    display.update()
    clock.tick(FPS)

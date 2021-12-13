import pygame
from pygame.locals import *
import sys
import random
import math
from main_variables import *
from pygame import mixer

#Every Game needs a background#
class background():
        def __init__(self):
            self.image = BGimage
            self.rectimg = RECTS[1]

            self.bgY1 = -250
            self.bgX1 = 0
            self.bgY2 = -250
            self.Height = 600
            self.bgX2 = self.Height  #self.rectimg.height
            self.moving_speed = 7
            
        def update(self):
            self.bgX1 -= self.moving_speed
            self.bgX2 -= self.moving_speed
            if self.bgX1 <= -self.Height: 
                self.bgX1 = self.Height
            if self.bgX2 <= -self.Height:
                self.bgX2 = self.Height

        def render(self):
            screen.blit(self.image, (self.bgX1, self.bgY1))
            screen.blit(self.image, (self.bgX2, self.bgY2))
#A less boring way of Seeing the cursor on screen and potetialy a futer game feature#
#Currently, this is disabled#
class Target():
        def __init__(self):
            self.image_1 = Target1
            self.image_2 = Target2
            self.image_3 = Target3
            self.image_4 = Target4
            self.image_5 = Target5
            self.image_6 = Target6
            self.image_7 = Target7
            self.image_8 = Target8
            self.image_9 = Target9
            self.image_0 = Target0
            self.image = self.image_5
      
        def update(self):
            pos = pygame.mouse.get_pos()
            self.x_target = pos[0]
            self.y_target = pos[1]
        def change(self):
                self.image = self.image_0

        def render(self):
            screen.blit(self.image, (self.x_target, self.y_target))
        def show(self):
                screen.blit(self.image_0, (self.x_target, self.y_target))
#Main Character#
class Jumper(pygame.sprite.Sprite):
        def __init__(self):
                self.image = HeroIcon
                self.game = 0
                self.rect = RECTS[2]
                self.rect.y = 370
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.rect.x = 120
                self.kill = 20
        def react(self):
                self.rect.y = 100
                return
        def Jump(self):
                self.rect.y = 320
        def Fall(self):
                self.rect.y = 370
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
        def jump(self):
                pass
        def hurt(self):
                self.kill -= 1
#Below is a list of enemies with basically the same properties but it was just to make multiples classes instead of a subclass#
class Enemy(pygame.sprite.Sprite):
        def __init__(self):
                self.image = Hand
                self.game = 0
                self.rect = RECTS[6]
                self.Height = 600
                self.rect.y = 370
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.rect.x = self.Height
                self.moving_speed =5
                self.go_back = -200
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 600
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
class Enemy2(pygame.sprite.Sprite):
        def __init__(self):
                self.image = Hand
                self.game = 0
                self.rect = RECTS[6]
                self.Height = 610
                self.rect.y = 370
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.rect.x = self.Height
                self.moving_speed =5
                self.go_back = -423
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 680
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
class Enemy3(pygame.sprite.Sprite):
        def __init__(self):
                self.image = Hand
                self.game = 0
                self.rect = RECTS[6]
                self.Height = -100
                self.rect.y = 370
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.x = self.Height
                self.moving_speed =5
                self.go_back = -3253
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 650
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
""" """
class Enemy4(pygame.sprite.Sprite):
        def __init__(self):
                self.image = FIRE
                self.game = 0
                self.rect = RECTS[7]
                self.Height = 600
                self.rect.y = 325
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.x = self.Height
                self.moving_speed =5
                self.go_back = -700
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 600
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
class Enemy5(pygame.sprite.Sprite):
        def __init__(self):
                self.image = FIRE
                self.game = 0
                self.rect = RECTS[7]
                self.Height = 610
                self.rect.y = 325
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.rect.x = self.Height
                self.moving_speed =9
                self.go_back = -629
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 600
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
class Enemy6(pygame.sprite.Sprite):
        def __init__(self):
                self.image = FIRE
                self.game = 0
                self.rect = RECTS[7]
                self.Height = -100
                self.rect.y = 325
                self.y_up = 320
                self.y_down = 370
                y = "320 or 370"
                self.rect.x = self.Height
                self.moving_speed =15
                self.go_back = -444
                
        def update(self):
                self.rect.x -= self.moving_speed
                if self.rect.x <= self.go_back:
                        self.rect.x = 600
        def show(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))
#Every Game needs a constantly updating score#
class Score():
        def __init__(self):
                self.score_value = 0
                self.floor = math.floor(self.score_value)
        def update(self):
                self.score_value += 0.01
        def increase(self):
                self.score_value += 1
        def decrease(self):
                self.score_value -= 1
                

                

import pygame
from pygame.locals import *
import sys
import random
import math

SIZE = (675, 405)

TOTAL_SCORE = 0

WHITE = (255,255,255)
GREEN = [0, 255, 0]
BLACK = [0, 0, 0]
COLORLIST = [(255,255,255), (0, 255, 0), (0, 0, 0), (255, 0, 0), (0, 0, 255), (255, 69, 0)]
screen = pygame.display.set_mode(SIZE)

running = True

Vec = pygame.math.Vector2


clock = pygame.time.Clock()

waiting = True

GRAV = 0.8
ACC = -0.12

# Background

BGimage = pygame.image.load("images\\Backgrounds\\Urithiru2.jpg")
BGimage = pygame.transform.scale(BGimage, (675, 810))

# Targets

Target1 = pygame.image.load("images\\Targets\\target_6.png")
Target1 = pygame.transform.scale(Target1, (50, 50))

Target2 = pygame.image.load("images\\Targets\\target_10.png")
Target2 = pygame.transform.scale(Target2, (50, 50))

Target3 = pygame.image.load("images\\Targets\\target_20.png")
Target3 = pygame.transform.scale(Target3, (50, 50))

Target4 = pygame.image.load("images\\Targets\\target_21.png")
Target4 = pygame.transform.scale(Target4, (50, 50))

Target5 = pygame.image.load("images\\Targets\\target_22.png")
Target5 = pygame.transform.scale(Target5, (50, 50))

Target6 = pygame.image.load("images\\Targets\\target_25.png")
Target6 = pygame.transform.scale(Target6, (50, 50))

Target7 = pygame.image.load("images\\Targets\\target_30.png")
Target7 = pygame.transform.scale(Target7, (50, 50))

Target8 = pygame.image.load("images\\Targets\\target_35.png")
Target8 = pygame.transform.scale(Target8, (50, 50))

Target9 = pygame.image.load("images\\Targets\\target_38.png")
Target9 = pygame.transform.scale(Target9, (50, 50))

Target0 = pygame.image.load("images\\Targets\\target_40.png")
Target0 = pygame.transform.scale(Target0, (50, 50))

# Jumper

HeroIcon = pygame.image.load("images\\itemImage\\Windrunner111.png")
HeroIcon = pygame.transform.scale(HeroIcon, (25, 25))

# ICONS Images for start screen?

ASurge = pygame.image.load("images\\svgtopngGLYPHS\\Adhesion_Surge-glyph.png")
ASurge = pygame.transform.scale(ASurge, (200, 200))
JSurge = pygame.image.load("images\\svgtopngGLYPHS\\Jeseh_glyph.png")
JSurge = pygame.transform.scale(JSurge, (200, 200))
GSurge = pygame.image.load("images\\svgtopngGLYPHS\\Gravitation_Surge-glyph.png")
GSurge = pygame.transform.scale(GSurge, (200, 200))

# ENEMY

Hand = pygame.image.load("images\\itemImage\\hand.png")
Hand = pygame.transform.scale(Hand, (25, 25))

FIRE = pygame.image.load("images\\itemImage\\FIRE.png")
FIRE = pygame.transform.scale(FIRE, (25, 14))

# Instruction
CREDIT = pygame.image.load("images\\RULES.png")
CREDIT = pygame.transform.scale(CREDIT, (200, 200))
END_CREDITS = pygame.image.load("images\\END_CREDITS.png")
END_CREDITS = pygame.transform.scale(END_CREDITS, (200, 200))
INFO = pygame.image.load("images\\INFO.png")
INFO = pygame.transform.scale(INFO, (300, 300))

#List#
RECTS = [BGimage.get_rect(),
         HeroIcon.get_rect(),
         ASurge.get_rect(),
         JSurge.get_rect(),
         GSurge.get_rect(),
         Hand.get_rect(),
         FIRE.get_rect(),
         CREDIT.get_rect(),
         END_CREDITS.get_rect(),
         INFO.get_rect()]

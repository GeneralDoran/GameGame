import pygame
from pygame.locals import *
import sys
import random
import math
from main_variables import *
from char2 import *

def main():
        #Getting some variables and Sound and Characters set up#
        pygame.mouse.set_visible(True)
        start_screen()
        rule_screen()
        pygame.font.init()
        ScoreText = pygame.font.SysFont('Comic Sans MS', 20)
        running = True
        h = background()
        aim = Target()
        hero = Jumper()
        vil = Enemy()
        e2 = Enemy2()
        e3 = Enemy3()
        #e4 = Enemy4()
        #e5 = Enemy5()
        e6 = Enemy6()
        score = Score()
        clock = pygame.time.Clock()
        SPEED = 60

        # MUSIC

        mixer.init()
        mixer.music.load("AnotherSong.4.9.mp3")
        mixer.music.set_volume(2)
        mixer.music.play()

        while running:
                #Updates and Event Handling#
                pygame.mouse.set_visible(True)
                pygame.display.set_caption("Underneath Urithiru")
                events = pygame.event.get()
                keys = pygame.key.get_pressed()
                aim.update()
                h.update()
                vil.update()
                e2.update()
                e3.update()
                #e4.update()
                #e5.update()
                e6.update()
                score.update()
                ScoreNumber = ScoreText.render(str("SCORE: "+ str(math.floor(score.score_value * 100) / 100)), True, COLORLIST[1])
                HNum = ScoreText.render("Health: " + str(hero.kill), True, COLORLIST[3])
                SNum = ScoreText.render("Speed: " + str(SPEED), True, COLORLIST[5])
                for event in events:
                        #Keyboard input#
                        if event.type == QUIT:
                                pygame.quit()
                                running = False
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        running = False
                                if event.key == K_w:
                                        hero.Jump()
                                if event.key == K_b:
                                        mixer.music.stop()
                                        start_screen()
                                        mixer.music.play()
                                if event.key == K_p:
                                        mixer.music.stop()
                                        global TOTAL_SCORE
                                        TOTAL_SCORE = int(math.floor(score.score_value))
                                        return
                                if event.key == K_UP:
                                        SPEED += 1
                                if event.key == K_DOWN:
                                        SPEED -= 1
                                if event.key == K_1:
                                        SPEED = 60
                                if event.key == K_2:
                                        SPEED = 40
                                if event.key == K_3:
                                        SPEED = 50
                                if event.key == K_4:
                                        SPEED = 70
                                if event.key == K_5:
                                        SPEED = 80
                                if event.key == K_6:
                                        SPEED = 90
                                if event.key == K_7:
                                        SPEED = 100
                                if event.key == K_8:
                                        SPEED = 30
                                if event.key == K_9:
                                        SPEED = 20
                                if event.key == K_0:
                                        SPEED = 1
                        if event.type == KEYUP:
                                if event.key == K_w:
                                        hero.Fall()
                #Character Death Check#
                collide = hero.rect.colliderect(vil.rect) or hero.rect.colliderect(e2.rect) or hero.rect.colliderect(e3.rect) or hero.rect.colliderect(e6.rect)
                death = False

                if collide:
                        print("hit")
                        hero.hurt()
                        print(str(hero.kill))
                        collide = False
                if hero.kill <= 0:
                        death = True
                if death:
                        mixer.music.stop()
                        TOTAL_SCORE = int(math.floor(score.score_value))
                        return
                """
                HealthNumber = ScoreText.render(str("SCORE: "+ str(kill), True, GREEN)
                """
                #Displaying stuff to the computer screen#
                h.render()
                vil.show()
                e2.show()
                e3.show()
                #e4.show()
                #e5.show()
                e6.show()
                hero.show()
                screen.blit(ScoreNumber, (0, 0))
                screen.blit(HNum, (0, 30))
                screen.blit(SNum, (0, 60))
                #screen.blit(HealthNumber, (250, 0))
                clock.tick(int(SPEED))
                pygame.display.update()

def rule_screen():
                #Setting up some Pictures and Variables#
        waiting = True
        SIZE = (675, 405)
        halfW = int(675/2)
        halfH = int(405/2)
        pygame.display.set_caption("Underneath Urithiru : Lobby")
        WHITE = [255,255,255]
        screen = pygame.display.set_mode(SIZE)
        herald = JSurge
        glyph1 = ASurge
        glyph2 = GSurge
        GC = GREEN
        pygame.font.init()
        credit = INFO
        pygame.mouse.set_visible(True)# Just so you can seeit on screen#
        while waiting:
                #Event handling#
                events = pygame.event.get()
                pygame.mouse.set_visible(True)
                for event in events:
                        #User input#
                        if event.type == QUIT:
                                pygame.quit()
                                waiting = False
                        elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        waiting = False
                                return
                #Showing Images to Screen#
                screen.fill(WHITE)
                screen.blit(glyph1, (int(halfW - 345 ), int(halfH + 10)))\

                screen.blit(glyph2, (int(halfW + 167 ), int(halfH + 10)))
                screen.blit(credit, (205, 0))
                pygame.display.update()
                

def start_screen():
        #Setting up some Pictures and Variables#
        waiting = True
        SIZE = (675, 405)
        halfW = int(675/2)
        halfH = int(405/2)
        pygame.display.set_caption("Underneath Urithiru : Lobby")
        WHITE = [255,255,255]
        screen = pygame.display.set_mode(SIZE)
        herald = JSurge
        glyph1 = ASurge
        glyph2 = GSurge
        GC = GREEN
        pygame.font.init()
        credit = CREDIT
        pygame.mouse.set_visible(True)# Just so you can seeit on screen#
        while waiting:
                #Event handling#
                events = pygame.event.get()
                pygame.mouse.set_visible(True)
                for event in events:
                        #User input#
                        if event.type == QUIT:
                                pygame.quit()
                                waiting = False
                        elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        waiting = False
                                return
                #Showing Images to Screen#
                screen.fill(WHITE)
                screen.blit(herald, (int(halfW - 100  ), int(halfH - 205)))
                screen.blit(glyph1, (int(halfW - 345 ), int(halfH + 10)))\

                screen.blit(glyph2, (int(halfW + 167 ), int(halfH + 10)))
                screen.blit(credit, (250, 210))
                pygame.display.update()
def endScreen():
        #Getting some variables and Sound set up#
        waiting = True
        pygame.display.set_caption("Underneath Urithiru : Lobby")
        WHITE = [255,255,255]
        pygame.font.init()
        screen = pygame.display.set_mode(SIZE)
        ScoreText = pygame.font.SysFont('Comic Sans MS', 20)
        score = TOTAL_SCORE
        end = Score()
        end.score_value = 0
        endCredit = END_CREDITS
        clock = pygame.time.Clock()
        # MUSIC
        
        mixer.init()
        mixer.music.load("YYhY.6.0.mp3")
        mixer.music.set_volume(2)
        mixer.music.play()
        #Events and updates#
        while waiting:
                events = pygame.event.get()
                
                ScoreNumber = ScoreText.render(str("Score: " +str(score)), True, COLORLIST[4])
                pygame.mouse.set_visible(True)
                for event in events:
                        if event.type == QUIT:
                                waiting = False
                        elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        waiting = False
                                elif event.key == K_r:
                                        mixer.music.stop()
                                        GameGame()
                if end.score_value > 10000:
                        return
                #Showing Images to Screen#
                screen.fill(WHITE)
                screen.blit(ScoreNumber, (0, 0))
                screen.blit(endCredit, (220, 210))
                end.increase()
                print(end.score_value)
                clock.tick(60)
                pygame.display.update()

#Just a function for Simplification#
def GameGame():
        pygame.init()
        main()
        endScreen()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
        GameGame()


                        
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

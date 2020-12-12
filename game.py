import math 
import random 
import time 
import pygame
import sys 


FPS = 60

pygame.init()

win = pygame.display.set_mode((640,480)) 
pygame.display.set_caption("First Game")

#whatever this is
clock = pygame.time.Clock()

#Images
ZebraB = pygame.image.load(r"assets\images\Zebra.png")
GreenB = pygame.image.load(r"assets\images\Green.png")
PinkB = pygame.image.load(r"assets\images\pink.png")
RedB = pygame.image.load(r"assets\images\Red.png")
YellowB = pygame.image.load(r"assets\images\yellow.png")

mainMenupic = pygame.image.load(r'assets\images\Christmas.png') 
#Music 
Main_Menu_Music = pygame.mixer.music.load(r'assets\music\Joy_To_The_World_-_Instrumental_with_Lyrics_no_vocals.mp3')
Map_Selection_Music = pygame.mixer.music.load(r'assets\music\Feliz_Navidad_Instrumental.mp3')
Battle_Music = pygame.mixer.music.load(r'assets\music\Silent_Night_rock_instrumental_-_Zachary_Russell.mp3')
Battle_Music2 = pygame.mixer.music.load(r'assets\music\Jingle_Bells_-_Merry_Heavy_Metal_Christmas.mp3')

onMenu = True 

#Map

ice_map = pygame.image.load(r"assets\images\Frozen Ice Map.png")
win.blit(ZebraB, (0, 0))
win.blit(ice_map, (0,0)) 
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
            run = False 
    # while onMenu: 
    #     pygame.mixer.music.play(Main_Menu_Music) 
    # win.draw()
    win.blit(ice_map, (0,0)) 
    #bloonType is the bloon that is being shown
    bloonType = ZebraB
    height = bloonType.get_height()
    width = bloonType.get_width()
    if pygame.mouse.get_pressed():
        cursorPos = pygame.mouse.get_pos()
        xco = cursorPos[0]
        yco = cursorPos[1]
        #This is subtracting the coordinates by half of both width and height to get the centre
        win.blit(bloonType, (xco-width/2, yco-height/2))
    pygame.display.update()

clock.tick(FPS)

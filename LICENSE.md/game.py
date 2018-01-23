#scoring system

import pygame
import time
import random

pygame.init()

disp_w = 800
disp_h = 600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
car_w = 120

gameDisp=pygame.display.set_mode((disp_w,disp_h))
pygame.display.set_caption('Racer Game')
clock=pygame.time.Clock()


carImg= pygame.image.load('car.png')

def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Dodged : "+str(count),True,black)
    gameDisp.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisp, color, [thingx,thingy,thingw,thingh])
    
def car(x,y):
    gameDisp.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True,red)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((disp_w/2),(disp_h/2))    
    gameDisp.blit(TextSurf, TextRect)         

    pygame.display.update()
    time.sleep(2)
    game_loop()
    
    
def crash():
    message_display('you crashed')  

def game_loop():
    x=(disp_w *0.45)
    y=(disp_h*0.8)
    x_change = 0
    dodged = 0
    
    thing_startx = random.randrange(0,disp_w)
    thing_starty = -600               
    thing_speed = random.randrange(5,12)
    thing_height = random.randrange(100,200)
    thing_width = 100
    ##
    
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:          
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change =5

            if event.type ==pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change      
        gameDisp.fill(white)
        
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty = thing_starty + thing_speed

        
        car(x,y)
        things_dodged(dodged)

        
        if x < 0-40 or x > disp_w-car_w:
            crash()     

        if thing_starty > disp_h:       
            thing_starty = 0-thing_height           
            thing_startx = random.randrange(0,disp_w)
            thing_height = random.randrange(100,200)
            thing_speed = random.randrange(10,15)
            dodged += 1             #counter incr

        #object collision logic
        if y < (thing_starty+thing_height):     
            if x+40 > thing_startx and x+40 < (thing_startx + thing_width) or (x + car_w) > thing_startx and (x + car_w) < (thing_startx + thing_width):
                crash()            
        
        pygame.display.update()
        clock.tick(80)

game_loop()
pygame.quit()
quit()

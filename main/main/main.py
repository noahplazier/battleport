""" PROJECT 2 : TEAM 1"""
#Imports

import pygame
import math
width = 1280
height = 720
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()

pygame.mixer.music.load("Achtergrond.mp3")
pygame.mixer.music.play(loops=200, start=0.0)

#global image files
#set a resolution
radar = pygame.image.load('radar.jpg')
background_startscherm = pygame.image.load('radar background.jpg')
boten = pygame.image.load('boten achtergrond.jpg')
zee = pygame.image.load('Bord.jpg')
boot2rood = pygame.image.load('boot2rood.png')
boot2geel = pygame.image.load('boot2geel.png')
label1=pygame.image.load('button groen 1.png')
label3=pygame.image.load('button groen 3.png')
spelregels1=pygame.image.load('Spelregels 1.png')
spelregels2=pygame.image.load('Spelregels 2.png')
spelregels3=pygame.image.load('Spelregels 3.png')
spelregels4=pygame.image.load('Spelregels 4.png')
spelregels5=pygame.image.load('Spelregels 5.png')
settings=pygame.image.load('Settings.png')

black=(0,0,0)
white=(255,255,255)
grey = (128,128,128)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
bright_grey=(155,155,155)
volume = 1
#quit functie
def quitgame():
    pygame.quit()
    quit ()

class bootje2():
    def __init__ (self,x,y,player):
        self.x = x
        self.y = y
        self.player = player
        self.mode = "attacking"
        self.hp = 2
    def update (self):
        keys = pygame.key.get_pressed()
        
        if keys [pygame.K_LEFT]:
            self.x = self.x - 20
        elif keys [pygame.K_RIGHT]:
            self.x = self.x + 20

        if keys [pygame.K_UP]:
            self.y = self.y - 20
        elif keys [pygame.K_DOWN]:
            self.y = self.y + 20
    def draw(self):
        screen.blit(boot2geel,[self.x,self.y])
    def range(self):
        self.range = range
        if self.mode == "defensive" :
            #alleen verticaal schieten
            self.range = 3
        else:
            self.range = 2
    def movement(self):
        if self.mode == "defensive" :
            #alleen verticaal schieten
            self.movement = 0
        else:
            self.movement = 3 
            
############################################################

class Tile:
    def __init__(self, x, y, pos, size):
        self.X = x
        self.Y = y
        self.Pos = pos
        self.Size = size
        self.Color = (0,0,0)
        
    def Clear(self):
        self.Color = (0,0,0)
        
    def Draw(self):
        pygame.draw.rect(screen, self.Color, (self.X, self.Y, self.Size, self.Size))
        pygame.draw.lines(screen, (100,100,100), True, [(self.X,self.Y), (self.X+self.Size,self.Y), (self.X+self.Size,self.Y+self.Size), (self.X,self.Y+self.Size)],2)
        

class Grid:
    def __init__(self,x,y,size,tilesize):
        self.Tile_size = tilesize
        self.Size = size
        self.X = x
        self.Y = y

        
        self.Tile_x = self.X
        self.Tile_y = self.Y
        self.Tiles = [''] * self.Size
        for x in range(0, self.Size):
            self.Tiles[x] = [''] * self.Size
            for y in range(0, self.Size):
                self.Tiles[x][y] = Tile(self.Tile_x, self.Tile_y, [x,y], self.Tile_size)
                self.Tile_y = self.Tile_y + self.Tile_size
            self.Tile_x = self.Tile_x + self.Tile_size
            self.Tile_y = self.Y

    def Change_color(self, tile_x, tile_y, color):
        self.Tiles[tile_x][tile_y].Color = color

    def Clear(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Clear()

    def Draw(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Draw()


##################################################################### 


def play_sound():
    pygame.init()
    sonar_sound = pygame.mixer.Sound('Sonar_Sound.wav')
    sonar_sound.play()
    pygame.mixer.Sound.set_volume(sonar_sound, volume)
    
# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (screen,msg,x,y,w,h,ic,ac,alw,ilw,fs,action = None, action2 = None):
    pygame.init()
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h),alw)
        if click[0] == 1 and action2 != None:
            action2()
        if click[0] == 1 and action != None:
            action()
            
            
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h),ilw)

    smallText = pygame.font.Font("freesansbold.ttf",fs)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def circle (screen,x,y,r,w,h,ic,ac,ilw,alw,newvolume):
    pygame.init()
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x1 = x-r
    y1= y-r

    if x1+w > mouse[0] > x1 and y1+h > mouse[1] > y1:
        pygame.draw.circle(screen,ac,(x,y),r,ilw)
        if click[0] == 1:
            volume = newvolume
            
    else:
        pygame.draw.circle(screen,ic,(x,y),r,alw)
    

def load_new_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)


    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        screen.blit(label1,[50,25])
        screen.blit(label3,[645,25])

        button (screen,"Load Game",255,175,200,75,green,bright_green,5,1,20, load_screen,play_sound)
        button (screen,"New Game",850,175,200,75,green,bright_green,5,1,20, new_screen,play_sound)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main-start-new
def new_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)
    testboot = bootje2(30,30,"player1")
    mooigrid = Grid(390,110,20,25)

    while not process_events():
        # Clear Screen
        screen.blit(zee, [0,0])
        mooigrid.Draw()
        
        testboot.update()
        testboot.draw()
        
        
        button (screen,"Menu",1090,0,100,50,grey,bright_grey,0,0,20)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
        pygame.display.update()

#main-start-load
def load_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

 
    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])

        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, load_new_screen)
        
        #Flip the screen
        pygame.display.flip()
#main-instructions
def instructions_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        screen.blit(label3, [240,50])
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Game Rules",450,200,200,75,green,bright_green,5,1,30, instructions1, play_sound)
       

        #Flip the screen
        pygame.display.flip()

def instructions1():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(spelregels1,[0,0])
        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20, instructions2)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()

def instructions2():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(spelregels2,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions3)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions1)

        #Flip the screen
        pygame.display.flip()

def instructions3():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(spelregels3,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions4)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions2)

        #Flip the screen
        pygame.display.flip()

def instructions4():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(spelregels4,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions5)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions3)

        #Flip the screen
        pygame.display.flip()

def instructions5():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(spelregels5,[0,0])

        button (screen,"Exit",1160,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions4)

        #Flip the screen
        pygame.display.flip()

#main-highscores
def highsccores_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main-options
def option_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)
    while not process_events():
        # Clear Screen
        screen.fill(black)
        screen.blit(settings,[37,0])
        circle (screen,445,218,10,20,20,green,bright_green,0,1, 0)
        circle (screen,540,218,10,20,20,green,bright_green,0,1, 0.25)
        circle (screen,640,218,10,20,20,green,bright_green,0,1,0.50)
        circle (screen,741,218,10,20,20,green,bright_green,0,1,0.75)
        circle (screen,842,218,10,20,20,green,bright_green,0,1,1)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main
def program():
    width = 1280
    height = 720
    size = (width, height)
    #start PyGame
    pygame.init()

    screen = pygame.display.set_mode(size)

    

    while not process_events():
        # Clear Screen
        screen.blit(background_startscherm,[0,0])
        #button
        button (screen,"Start!",350,200,200,75,green,bright_green,5,1,30, load_new_screen, play_sound)
        button (screen,"Instructions",670,580,200,75,green,bright_green,5,1,30, instructions_screen,play_sound)
        button (screen,"Highscores",930,300,200,75,green,bright_green,5,1,30, highsccores_screen,play_sound)
        button (screen,"Options",1160,650,100,50,grey,bright_grey,0,0,20, option_screen)
        button (screen,"Quit",20,650,100,50,red,bright_red,0,0,20, quitgame)

        #Flip the screen
        pygame.display.flip()

# Start the program
program()

#end
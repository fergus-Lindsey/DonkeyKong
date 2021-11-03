#ICS3U - 03
#FINAL PROJECT - MISSON: DONKEYKONG RE-ENACTMENT
#2019/06/14
#sorry about all the spelling mistakes in advance
#Lindsey Ferguson
from pygame import *
from math import *
from random import *

red = (255,0,0)
white = (255,255,255) #these are the main colours i use throughout the whole prgram, so i dont have to re-write then everytime
blue = (0,0,255)

screen = display.set_mode((490,590))#this makes the screen

import os
init()       #this make sure you dont have to move the window everytime
inf=display.Info()
w,h=inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '10,10'

font.init()
MyFont = font.SysFont("Jumpman",25)
smallFont = font.SysFont("jumpman",20)#this imports and initializes my fonts, so i can add things like score, and levels in different sizes
verySmallFont = font.SysFont("jumpman",14)
bigFont = font.SysFont("jumpman",35)
MyFont2 = font.SysFont("Jumpman",40)

#----------------------------------------------------------------------------------------------------------------------
#pictures
#this is where i upload all my photos, outside of the loops to make it load faster.
#i added some photos into lists to make my animations look animated

####PAGES####
#title screen
titlescreen = transform.scale(image.load("titlescreen.png"),(500,590)) #this i smy title page, the one you see when you first load the program as a loading page
#how high can you go page
hhcyg = transform.scale(image.load("hhcyg.png"),(500,590))#this is the how high can you go page
#death page
deathpage = transform.scale(image.load("deathpage.png"),(500,590))

page = "Title Page" #this sets the page to always t title  page so it starts off the same thing eveytime

####MARIO####
#standing marios
rightMario = transform.scale(image.load("walkright/walkright3.png"),(25,25)) #this is so when mario isnt walking he stands, eahc for the correct direction 
leftMario = transform.scale(image.load("side mario0.png"),(22,22))
hammerstandR=transform.scale(image.load("hammer1.png"),(35,35)) #this is so when Hammer mario isnt walking he stands, eahc for the correct direction
hammerstandL=transform.scale(image.load("lefthammer.png"),(35,35))
#mario walking 
RMarioPics = []
RMarioPics.append(transform.scale(image.load("walkright/walkright1.png"),(25,25))) #this allows for mario to apper to walk right when the right arrow key is pressed down
RMarioPics.append(transform.scale(image.load("walkright/walkright2.png"),(25,25)))
RMarioPics.append(transform.scale(image.load("walkright/walkright3.png"),(25,25)))
HRMarioPics = []
HRMarioPics.append(transform.scale(image.load("rightMarioHammer/rightMarioHammer0.png"),(35,35))) #this is the same as walk right, but with a hammer
HRMarioPics.append(transform.scale(image.load("hammer2.png"),(25,35)))
HRMarioPics.append(transform.scale(image.load("rightMarioHammer/rightMarioHammer2.png"),(35,35)))
rightMarioHammer1 = transform.scale(image.load("rightMarioHammer/rightMarioHammer0.png"),(35,35))
LMarioPics = []
LMarioPics.append(transform.scale(image.load("walkleft/walkleft1.png"),(25,25)))#this allows for mario to apper to walk right when the right arrow key is pressed down
LMarioPics.append(transform.scale(image.load("walkleft/walkleft2.png"),(25,25)))
LMarioPics.append(transform.scale(image.load("walkleft/walkleft3.png"),(25,25)))
HLMarioPics = []
HLMarioPics.append(transform.scale(image.load("leftHammerMario/leftHammerMario0.png"),(35,35)))#this is the same as walk left, but with a hammer
HLMarioPics.append(transform.scale(image.load("leftHammerMario/leftHammerMario1.png"),(35,35)))
HLMarioPics.append(transform.scale(image.load("leftHammerMario/leftHammerMario2.png"),(35,35)))
#climb
UDMarioPics = []
UDMarioPics.append(transform.scale(image.load("climb/climb0.png"),(25,25))) #when mario collides with a ladder and the up arrow is pressed this makes him look like hes climbing up
UDMarioPics.append(transform.scale(image.load("climb/climb1.png"),(25,25)))
UDMarioPics.append(transform.scale(image.load("climb/climb2.png"),(25,25)))

####DONKEY KONG####
#climb
DKpics=[]
DKpics.append(transform.scale(image.load("dk-climb/dk-climb0.png"),(75,75))) #this makes him climb up a ladder in the intro
DKpics.append(transform.scale(image.load("dk-climb/dk-climb1.png"),(75,75)))
DKpics.append(transform.scale(image.load("dk-climb/dk-climb2.png"),(75,75)))
#dance 
bigDKDancePics = []
bigDKDancePics.append(transform.scale(image.load("normal/normal0.png"),(85,85))) #this is for the into of him doing a dance, just slightly bigger than DKDancePics
bigDKDancePics.append(transform.scale(image.load("normal/normal1.png"),(85,85)))
DKDancePics = []
DKDancePics.append(transform.scale(image.load("normal/normal0.png"),(65,65)))
DKDancePics.append(transform.scale(image.load("normal/normal1.png"),(65,65)))
#rollling barrel
DKrollPics = []
DKrollPics.append(transform.scale(image.load("roll/roll3.png"),(65,65)))#makes it look like he rolled the barrel
jumpPics =[]
jumpPics.append(transform.scale(image.load("jump/jump0.png"),(65,65)))
jumpPics.append(transform.scale(image.load("jump/jump1.png"),(65,65)))
jumpPics.append(transform.scale(image.load("jump/jump2.png"),(65,65)))

####PRINCESS####
PrincessPics = []
PrincessPics.append(transform.scale(image.load("princess/princess0.png"),(25,25))) #this animated the princess so it looks like shes moving side to side
PrincessPics.append(transform.scale(image.load("princess/princess1.png"),(25,25)))
PrincessPics.append(transform.scale(image.load("princess/princess2.png"),(25,25)))
PrincessPics.append(transform.scale(image.load("princess/princess3.png"),(25,25)))

####DECORATIONS+EXTRAS####
#fire barrel
FirePics = []
FirePics.append(transform.scale(image.load("fire thing/fire thing0.png"),(25,40))) #this is the fire barrel at the bottom eft, aso when barrels hit it they delete, so the game dosent agg
FirePics.append(transform.scale(image.load("fire thing/fire thing1.png"),(25,40)))
#rolling barrels
barrelPics = []
barrelPics.append(transform.scale(image.load("barrels rolling/barrels rolling0.png"),(22,22))) #this makes the barres ook like their turning
barrelPics.append(transform.scale(image.load("barrels rolling/barrels rolling1.png"),(22,22)))
barrelPics.append(transform.scale(image.load("barrels rolling/barrels rolling2.png"),(22,22)))
barrelPics.append(transform.scale(image.load("barrels rolling/barrels rolling3.png"),(22,22)))
#bricks
brickPic1 = transform.scale(image.load("lbrick0.png"),(460,45))
brickAngle1 = -1.3
b1 = transform.rotate(brickPic1,brickAngle1)
b2 = transform.rotate(brickPic1,brickAngle1+4)
b3 = transform.rotate(brickPic1,brickAngle1-1.2)
b4 = transform.rotate(brickPic1,brickAngle1+3.2)
b5 = transform.rotate(brickPic1,brickAngle1-1.2)
b6 = transform.rotate(brickPic1,brickAngle1+2.5)

hammerpic = transform.scale(image.load("hammer0.png"),(25,25))
introMario = transform.scale(image.load("hammer1.png"),(45,45))
donkeykongwordart = transform.scale(image.load("donkeykongwordart.png"),(250,125))
highscorePic = transform.scale(image.load("highscore.jpg"),(490,590))
instructionsPic = transform.scale(image.load("instructions.png"),(490,590))
ladderpic = transform.scale(image.load("ladder.png"),(23,55))
brokenladderPic = transform.scale(image.load("brokeenladder0.png"),(23,65)) #decorations
halfbrokenladderPic = transform.scale(image.load("halfbroke0.png"),(20,20))
brickPic2 = transform.scale(image.load("lbrick0.png"),(460,40))
barrelpic = transform.scale(image.load("barrel0.png"),(20,25))
smallbrickpic = transform.scale(image.load("small brick0.png"),(100,30))
smallbarrelpic = transform.scale(image.load("barrel0.png"),(8,12))
smallhammerpic = transform.scale(image.load("hammer0.png"),(10,10))
lifespic = transform.scale(image.load("lives.png"),(20,20))
winpic =  transform.scale(image.load("win page 2.png"),(250,80))

####LISTS####
hammer =[[300,430,25,25],[40,150,25,25]]
ladder = [[430,490,25,55],[30,400,25,55],[430,320,25,55],[30,235,25,55],[435,138,25,55]]
barrels = [[100,100,True]]
laddersL = [[220,500,23,55],[220,500,23,55],[220,450,23,55],[220,400,23,55],[220,350,23,55],[220,295,23,55],[220,240,23,55],[220,190,23,55],[220,135,23,55]]
laddersR = [[250,500,23,55],[250,500,23,55],[250,450,23,55],[250,400,23,55],[250,350,23,55],[250,295,23,55],[250,240,23,55],[250,190,23,55],[250,135,23,55]]
#--------------------------------------------------------------------------------------------------------------------------------------------------------
####MASKS#####
mask = Surface((500,590))#this is the mask so it recognoizes when mario steps onto stuff
mask.fill(0)#this makes the mask black so evrything thats not black get recognized as some sort of platform
brickAngle1 = -1.3
brick1=mask.blit(transform.rotate(brickPic1,brickAngle1),(10,90)) #adding the bricks to the mask so on ground and find ground can recoginzize that mario isnt on the platfrom and them slowly shift him so he is
brick2=mask.blit(transform.rotate(brickPic1,brickAngle1+4),(20,170))
brick2.x-=55
brick2.width+=55
brick3=mask.blit(transform.rotate(brickPic1,brickAngle1-1.2),(5,260))
brick3.x-=55
brick3.width+=55
brick4=mask.blit(transform.rotate(brickPic1,brickAngle1+3.2),(25,350)) #extends the reach of the platfroms to allow for the barrels to fall 
brick4.x-=55
brick4.width+=55
brick5=mask.blit(transform.rotate(brickPic1,brickAngle1-1.2),(5,430))
brick5.x-=55
brick5.width+=55
brick6=mask.blit(transform.rotate(brickPic1,brickAngle1+2.5),(15,518))
brick6.x-=55
brick6.width+=55
ladderpic= transform.scale(image.load("ladder.png"),(25,55))
ladderss =image.load("ladder.png")
ladder2 = transform.scale(ladderss,(23,55))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
####IMPORTANT VARABLES####
#positions
DKx,DKy = 215,520
intromariox,intromarioy = 120,320
Mariox,Marioy = 40,500 #where mairo starts the game
X = 0
Y = 1
#point variables
score = 0
barrelpoints = 0
hammerpoints = 0
#random
HammerM = False #sets if mario has a hammer 
keys = key.get_pressed()
direction = "right"
gameAngle = 0 #allows me to make the platform
Mladder = False
myClock = time.Clock()
rand = randint(100,120)
#ground variables
ground = 3
gravity = 1
#frames
MarioFrame = 0
MarioFrameDelay = 10
Dkframe = 0 #frame acts like a timer, and helps blit the animations correctly
DkframeDelay = 10 #slows down frames
frame = 0
FDelay = 10
hammertimer = 0
angryDelay = 10
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
####FUNCTIONS####
def openingPageDraw(screen,laddersL,laddersR,angryframe,DKx,DKy):
    angryframe+=1
    screen.fill(0)
    screen.blit(brickPic2,(10,90))
    screen.blit(brickPic2,(20,170))
    screen.blit(brickPic2,(5,260))
    screen.blit(brickPic2,(25,350))#this draws the donkeykong warm up, it adds the bricks and ladders
    screen.blit(brickPic2,(5,430))
    screen.blit(brickPic2,(15,518))
    princessladder1 = screen.blit(ladderpic,(143,65))
    princessladder2 = screen.blit(ladderpic,(165,65))
    princessladder3 = screen.blit(ladderpic,(220,65))
    screen.blit(smallbrickpic,(143,40))
    for i in range(len(laddersL)):
        screen.blit(ladder2,laddersL[i]) #this adds the adders to the screen
    for i in range(len(laddersR)):
        screen.blit(ladder2,laddersR[i])        
        
def titlePageDraw(screen):
    screen.blit(titlescreen,(0,0))
    display.flip()#when page == title screen this blits it to the screen
    
def introductionDraw(screen,DKx,DKy,intromariox,intromarioy): #this draws the section after the titlepage
    screen.fill(0)
    bigbarrelpic = transform.scale(image.load("barrel0.png"),(30,40)) 
    screen.blit(donkeykongwordart,(120,30))
    
    pressEnter = verySmallFont.render("*USE KEYS TO MOVE UP/DOWN*PRESS ENTER TO CONTINUE*PRESS BACKSPACE TO GO BACK*",True,blue)
    screen.blit(pressEnter,(10,570))

    DKx,DKy = 200,200
    screen.blit(bigDKDancePics[frame//20%2],(DKx,DKy)) #this makes donkeykong appear to dance on the screen
    screen.blit(bigbarrelpic,(30,190))
    screen.blit(bigbarrelpic,(30,155))#this adds barrels for decortaion
    screen.blit(bigbarrelpic,(62,190))
    screen.blit(bigbarrelpic,(62,155))
    screen.blit(bigbarrelpic,(395,190))
    screen.blit(bigbarrelpic,(395,155))
    screen.blit(bigbarrelpic,(427,190))
    screen.blit(bigbarrelpic,(427,155))
    screen.blit(FirePics[frame//5%2],(50,115))#these add flamin barrels also as decoration 
    screen.blit(FirePics[frame//5%2],(410,115))
    newgame = bigFont.render("NEW GAME",True,red) #this adds the word NEW GAME onto the screen, so when users see it they know to click on it to start
    screen.blit(newgame,(200,350))
    draw.rect(screen,red,(190,343,155,35),4)
    HighScore = bigFont.render("HIGH SCORES",True,red) #this adds the word highscores onto the screen, 
    screen.blit(HighScore,(200,410))
    draw.rect(screen,red,(190,405,188,35),4) #the rects are also just for decortaion 
    instructions = bigFont.render("INSTRUCTIONS",True,red) #this adds the word instructions onto the screen, 
    screen.blit(instructions,(200,480))
    draw.rect(screen,red,(190,475,210,35),4)

def gamePageDraw(screen,hammertimer,PrincessPics,FirePics,Mariox,Marioy,barrels,score,barrelpoints,hammerpoints,hammer,DKx,DKy,DKDancePics,ladderpic,brokenladderPic,halfbrokenladderPic,barrelpic,smallbrickpic,smallbarrelpic,smallhammerpic):
    #this is the most important draw page, as its where the whole game gets drawn onto the screen, this is also where most of the animation happens 
    screen.fill(0)
    screen.blit(smallbrickpic,(143,40))#this adds the little platfrom where the princess is trapped on
    
    screen.blit(smallhammerpic,(8,40)) #this is the picture for the little points icons so when you jump/hit something you can see where you get points
    screen.blit(smallbarrelpic,(8,25))
    
    screen.blit(b1,(10,90)) #this blits all the platforms to the screen, 
    screen.blit(b2,(20,170))
    screen.blit(b3,(5,260))
    screen.blit(b4,(25,350))
    screen.blit(b5,(5,430))
    screen.blit(b6,(15,518))
    
    screen.blit(brokenladderPic,(200,405)) #broken ladders - as decoration only serves no purpose to the game
    screen.blit(brokenladderPic,(360,142))
    screen.blit(halfbrokenladderPic,(380,490))#half broken ladders- also decore
    screen.blit(halfbrokenladderPic,(120,310))
    screen.blit(halfbrokenladderPic,(80,140))
    
    screen.blit(ladderpic,(ladder[0]))#ladders - these allow for mario to travel from platform to platform when hes infront of one and the up arrow is pressed
    screen.blit(ladderpic,(ladder[1]))#this is where i add them to the screen from a list
    screen.blit(ladderpic,(ladder[2]))
    screen.blit(ladderpic,(ladder[3]))
    screen.blit(ladderpic,(ladder[4]))
    
    l1 = Rect(ladder[0])#these rects allow for mario to register when hes on a lddder and so he can climb up them
    l2 = Rect(ladder[1])
    l3 = Rect(ladder[2])
    l4 = Rect(ladder[3])
    l5 = Rect(ladder[4])
    
    princessladder1 = screen.blit(ladderpic,(143,65))#these are just 3 ladders to 'support' the princess platfrom -- decoration
    princessladder2 = screen.blit(ladderpic,(165,65))
    princessladder3 = screen.blit(ladderpic,(220,65))
    screen.blit(smallbrickpic,(143,40))#this is where the princess stands on -- decoration
    
    screen.blit(FirePics[frame//5%2],(20,515))     #this is where i blit the animation for the fire can so it looks like the fire is always moving
    screen.blit(PrincessPics[frame//14%4],(170,30))#the princess is added to the screen
    
    if Dkframe == -1:
        screen.blit(DKDancePics[frame//20%2],(DKx,DKy))# this makes donkey kong dance untill a barrel is rolled, when a barrel is rlled, the function 'timer'
    else:                                              # makes dk frame not == -1 (it makes it dkframe//left) allow it to look like hes rolling the barrel 
        screen.blit(DKrollPics[Dkframe//2%1],(DKx,DKy))#giving the user a head up, then making dkframe == -1 again
        
    screen.blit(barrelpic,(10,90))#these are the barrels in the top left cornor just for decortaion
    screen.blit(barrelpic,(10,65))
    screen.blit(barrelpic,(32,90))
    screen.blit(barrelpic,(32,65))
    
    SCORE = MyFont.render("HIGH SCORE",True,red)
    screen.blit(SCORE,(200,10))
    ScoreDraw = MyFont.render(str(score),True,white)
    screen.blit(ScoreDraw,(260,25))                                         #these are where i write out the points and add them to the screen, so when the user
    hammerPointsDraw = smallFont.render("="+str(hammerpoints),True,white)   # gets points it adds onto the varibales before being blited onto the screen
    screen.blit(hammerPointsDraw,(15,40))
    barrelPointsDraw = smallFont.render("="+str(barrelpoints),True,white)
    screen.blit(barrelPointsDraw,(15,25))
    
    for barr in barrels:                             #this allows for the barrel animation and for the rolling of the actual barrels
        screen.blit(barrelPics[frame//5%4],barr[:2]) 

def onLadder(Mariox,Marioy,ladder):
    global gravity, Mladder
    Mladder = False 
    marioRect = Rect(Mariox,Marioy,25,25)
    Ladder1 = Rect(ladder[0])
    Ladder2 = Rect(ladder[1]) #adds the ladderss to the screen
    Ladder3 = Rect(ladder[2])
    Ladder4 = Rect(ladder[3])
    Ladder5 = Rect(ladder[4])
    if marioRect.colliderect(Ladder1):
         Mladder = True
         gravity = 0 
    elif marioRect.colliderect(Ladder2):
         Mladder = True
         gravity = 0 
    elif marioRect.colliderect(Ladder3): #if mario collides with these ladders it makes Mladder true so he can climb up them
         Mladder = True
         gravity = 0 
    elif marioRect.colliderect(Ladder4):
         Mladder = True
         gravity = 0 
    elif marioRect.colliderect(Ladder5):
         Mladder = True
         gravity = 0
         
def Move(screen,Mariox,Marioy):
    global direction
    if keys[K_RIGHT] and HammerM == False and Mariox > 0 and Mariox < 490:
        direction = "right"
        Mariox += 2
        screen.blit(RMarioPics[MarioFrame//5%3],(Mariox,Marioy))
    elif HammerM == True:
        if keys[K_RIGHT] and Mariox > 0 and Mariox < 490:
            direction = "right"
            Mariox += 2
            screen.blit(HRMarioPics[MarioFrame//5%3],(Mariox,Marioy))
        if keys[K_LEFT] and Mariox > 0 and Mariox < 490:
            direction = "left"
            Mariox -= 2
            screen.blit(HLMarioPics[MarioFrame//5%3],(Mariox,Marioy))
        else:
            if direction == "left":
                screen.blit(hammerstandL,(Mariox,Marioy))
            if direction == "right":
                screen.blit(rightMarioHammer1,(Mariox,Marioy))
    elif keys[K_LEFT] and HammerM == False and Mariox > 0 and Mariox < 490:
        direction = "left"
        Mariox -= 2
        screen.blit(LMarioPics[MarioFrame//4%3],(Mariox,Marioy))
    elif keys[K_UP] and Mladder ==  True and HammerM == False:
        Marioy -= 4
        gravity = False
        screen.blit(UDMarioPics[MarioFrame//4%3],(Mariox,Marioy))
    else:
        if direction == "left":
            screen.blit(leftMario,(Mariox,Marioy))
        if direction == "right":
            screen.blit(rightMario,(Mariox,Marioy))
    onLadder(Mariox,Marioy,ladder)
    return (Mariox,Marioy)

def onGround(Mariox,Marioy):
    if HammerM == True: #since mario with a hammer is bigger then regular mario, the ground will be different for both of them
        pic = 35        #this sets the ground to 2 different settings depending on if mario has the hammer
    else:
        pic = 25
    x,y = int(Mariox+12.5),int(Marioy+pic)
    if y >= screen.get_height() or x < 0 or x >= screen.get_height():
        return True
    else:
        return mask.get_at((x,y))[:3] != (0,0,0) #this sets the platforms as anything but the colour black, as the mask is the colour black
    
def findGround(Mariox,Marioy):
    while onGround(Mariox,Marioy):
        Marioy-=1
    return Marioy

def hhcygDraw(screen):
    screen.fill(0)
    screen.blit(hhcyg,(0,0))
    display.flip()
    time.wait(2000)
    screen.fill(0)
    
def barrelOnGround(barr):
    cx = int(barr[X]+11)
    cy = int(barr[Y]+22)
    sRect = screen.get_rect()
    if sRect.collidepoint((cx,cy)):
        return mask.get_at((cx,cy))[:3] != (0,0,0)
    return False

def barrelFindGround(barrels): #this recognizes when the barrels are not on the ground and then corrects 
    for barr in barrels:       #them to be on the ground, by adding 1 (moving it up) until its on the ground/platform
        while not barrelOnGround(barr):
            barr[Y]+=1
    return barrels 

def moveBarrels(barrels):
    for barr in barrels: #this allows the barrels to move different directions depending on when brick it lands on (as they're slanted in different directions)
        if brick1.collidepoint(barr[X],barr[Y]):
            barr[X]+=3
        if brick2.collidepoint(barr[X],barr[Y]):
            barr[X]-=3
        if brick3.collidepoint(barr[X],barr[Y]):
            barr[X]+=3
        if brick4.collidepoint(barr[X],barr[Y]):
            barr[X]-=3
        if brick5.collidepoint(barr[X],barr[Y]):
            barr[X]+=3
        if brick6.collidepoint(barr[X],barr[Y]):
            barr[X]-=3
def jumpDraw(screen):
    dkbrick1 = screen.blit(brickPic2,(10,90))
    dkbrick2 = screen.blit(brickPic2,(20,170))
    dkbrick3 = screen.blit(brickPic2,(5,260)) #adds the normal ones
    dkbrick4 = screen.blit(brickPic2,(25,350))
    dkbrick5 = screen.blit(brickPic2,(5,430))
    dkbrick6 = screen.blit(brickPic2,(15,518))
    screen.blit(smallbrickpic,(143,40))
    screen.blit(jumpPics[angryframe//5%3],(DKx,DKy))
    time.wait(20)
    del dkbrick1    
    screen.blit(b1,(10,90))
    time.wait(20)
    del dkbrick2
    screen.blit(b2,(20,170)) #deletes straight platfroms and blits the crooked ones to the screen,looking like donkeykong jumpped and broke them 
    time.wait(20)
    del dkbrick3
    screen.blit(b3,(5,260))
    time.wait(20)
    del dkbrick4#blits the crooked one
    screen.blit(b4,(25,350))
    time.wait(20)
    del dkbrick5
    screen.blit(b5,(5,430))
    time.wait(20)
    del dkbrick6
    screen.blit(b6,(15,518))
    screen.blit(smallbrickpic,(143,40))
    princessladder1 = screen.blit(ladderpic,(143,65))
    princessladder2 = screen.blit(ladderpic,(165,65))
    princessladder3 = screen.blit(ladderpic,(220,65))
    screen.blit(jumpPics[angryframe//2%3],(DKx,DKy))
    screen.blit(PrincessPics[angryframe//14%4],(170,30))   

def barrelTimer(barrels,DKx,DKy,rand,Dkframe):
    if frame == rand:
        rand = frame + randint(100,120)        #mr.McKenzies mathical magic 
        barrels.append([100,100,True])
        
    elif frame > rand -30:
        left = rand - frame
        Dkframe = left //5 
    else:
        Dkframe = -1   
    return Dkframe,rand
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
####RUNNING####

angryframe = 0
running = True
while running :
    keyPress = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == KEYDOWN:
            keyPress = True
            if evt.key == K_ESCAPE:
                running = False
            if not onLadder(Mariox,Marioy,ladder) and  evt.key == K_SPACE and Marioy == findGround(Mariox,Marioy) and ground == True:
                #this allows for amrio to jump when: hes not a ladder, the space bar is pressed, and hes on the ground
                gravity = -5
                onGround(Mariox,Marioy) == False
                ground = False
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    keys = key.get_pressed()
    mouse.set_visible(False)

    for barrel in barrels:        
        if not barrelOnGround(barrel): #this makes the barrels fin the ground so when they roll off a platform then can find the next one
            barrelFindGround(barrels)
            barrel[2] = True
    
    if page == "angry page":
        angryDelay -=1
        angryframe +=1
        if DKy > 50:
            DKy -= 1.5
            openingPageDraw(screen,laddersL,laddersR,angryframe,DKx,DKy)
            screen.blit(DKpics[angryframe//8%3],(DKx,DKy)) 
            dkrect = Rect(DKx,DKy,75,75)
        if len(laddersR) > 0:
            if angryframe == 35:
                laddersL.remove(laddersL[0]) #allows for the ladders to delete after every 35 frame (appears to look like it deltes after dk touches it)
                laddersR.remove(laddersR[0])
                angryframe = 0
        
        nextrect = Rect(230,30,25,25)
        if dkrect.colliderect(nextrect):
            angryframe = 0
            page = "next"
    if page == "next":
        angryDelay -=1
        angryframe +=1
        screen.fill(0)
        screen.blit(brickPic2,(10,90))
        screen.blit(brickPic2,(20,170))
        screen.blit(brickPic2,(5,260))
        screen.blit(brickPic2,(25,350))
        screen.blit(brickPic2,(5,430))
        screen.blit(brickPic2,(15,518))
        princessladder1 = screen.blit(ladderpic,(143,65))
        princessladder2 = screen.blit(ladderpic,(165,65))
        princessladder3 = screen.blit(ladderpic,(220,65))
        screen.blit(smallbrickpic,(143,40))
        screen.blit(DKDancePics[angryframe//10%2],(DKx,DKy))
        screen.blit(PrincessPics[angryframe//14%4],(170,30))
        
        if angryframe  == 50:
            angryframe =0
            page = "jump"
            
    if page == "jump":
        angryDelay -=1
        angryframe +=1
        screen.fill(0)
        jumpDraw(screen)
        
        if angryframe == 20:
            page = "game Page"
    if page == "intro page":
        frame+=1
        introductionDraw(screen,DKx,DKy,intromariox,intromarioy)
        startRect = Rect(120,350,200,25)
        highscoreRect = Rect(120,420,200,25)
        instructionsRect = Rect(120,490,200,25)
        if keyPress and keys[K_DOWN] and intromarioy < 450: #this makes it so you can choose where in  the menu you want to go                         
            intromarioy += 70
        if keyPress and keys[K_UP] and intromarioy > 350:
            intromarioy -= 70
        screen.blit(introMario,(intromariox,intromarioy))
        intromarioRect = Rect(intromariox,intromarioy,45,45)
        if intromarioRect.colliderect(startRect) and keys[K_RETURN]:
            frame = 0
            page = "hhcyg Page"
        if intromarioRect.colliderect(highscoreRect) and keys[K_RETURN]:
            page = "highscore page"
        if intromarioRect.colliderect(instructionsRect) and keys[K_RETURN]:
            page = "instruction page"
            
    if page == "instruction page":
        screen.blit(instructionsPic,(0,0))
        if keys[K_BACKSPACE]:
            page = "intro page"
            
    if page == "highscore page":
        screen.blit(highscorePic,(0,0))
        if keys[K_BACKSPACE]:
            page = "intro page"
            
    if page == "Title Page":
        titlePageDraw(screen)
        time.wait(2000)
        page = "intro page"
        
    if page == "hhcyg Page":
        hhcygDraw(screen)
        page = "angry page"
        lifes = 3
        HammerTimer = 0
        frame =0
   
    if page == "game Page":
        frame +=1
        DKx,DKy = 50,50
        hammerTimer = -1
        gamePageDraw(screen,hammertimer,PrincessPics,FirePics,Mariox,Marioy,barrels,score,barrelpoints,hammerpoints,hammer,DKx,DKy,DKDancePics,ladderpic,brokenladderPic,halfbrokenladderPic,barrelpic,smallbrickpic,smallbarrelpic,smallhammerpic)
        marioRect = Rect(Mariox,Marioy,25,25)
        DonkeyKongRect = Rect(DKx,DKy,65,65)
        hammerRect = Rect(300,430,25,25)
        hammerRect1 = Rect(150,40,25,25)
        level = MyFont.render("L = 01",True,blue)
        screen.blit(level,(400,30))
        if marioRect.colliderect(DonkeyKongRect):
            page = "win page"
        if marioRect.colliderect(hammerRect):
            HammerM = True                          #these check to see if mario collides with hammer, then hammer mario appears
            hammerpoints +=1
        if marioRect.colliderect(hammerRect1):
            HammerM = True
            hammerpoints +=1
        for i in range(len(hammer)):
            screen.blit(hammerpic,(hammer[i]))
        if HammerM == True:
            hammertimer += 1
        if hammertimer == 250: #this is the timer for the hammr, you get 250 frames before its back to regualr mario
            HammerM = False
            
        Mariox,Marioy=Move(screen,Mariox,Marioy) #this sets mx,my to the move varibale
        Dkframe,rand = barrelTimer(barrels,DKx,DKy,rand,Dkframe)
        moveBarrels(barrels)
        
        for barr in barrels[:]:

            fireRect = Rect(10,512,25,40)
            barrelrect = Rect(barr[X],barr[Y],25,25)   #this draws a box around each barrel
            if barrelrect.colliderect(fireRect):       #when the barrel rect collides with the firerect
                del barrels[0]                         #it deletes the barrels so the game runs faster

            pointsrect = Rect(barr[X],barr[Y]-20,2,30) #this draws a thin rectange above each barrel
            if marioRect.colliderect(pointsrect):      #when mario collides with the rect he gets 20 points
                score += 20
                barrelpoints +=1
                
            if barrelrect.colliderect(marioRect)and HammerM == False: #when the barrel rect collides with mario, then mario gets sent back to the start 
                Mariox,Marioy = 40,500                                #and looses a life, and all the barrels re-start aswell 
                direction == "right"
                lifes -= 1
                if score <= 0:
                    score -= 100
                barrels = []
                time.wait(100)
        
            if barrelrect.colliderect(marioRect) and HammerM == True: #when a barel collides with mario but mario has a hammer, 
                barrels.remove(barr)                                  #the barrel gets removed and mario gets points
                score += 50
                barrelpoints += 1
                    
        if page == "win page":                                                          #when mario collides with donkeykong he wins the game,
            screen.fill(0)                                                              #getting then sent to the win page
            MyFont2 = font.SysFont("Jumpman",40)
            winner = MyFont2.render("YOU WIN!!! :)",True,blue)
            screen.blit(winner,(140,40))
            HighScore = bigFont.render("HIGH SCORE:",True,red) #this adds the word highscores onto the screen, 
            screen.blit(HighScore,(150,110))
            ScoreDraw = MyFont2.render(str(score+hammerpoints+barrelpoints),True,white) #this prints out the final score in a REALLY big font
            screen.blit(ScoreDraw,(220,195))
            screen.blit(winpic,(100,430))
            display.flip()
            time.wait(5000)
            page = "intro page"                                                         #after winning you get sent back into the intro
            
        for i in range(lifes):#this draws the marios at the top left of the screen based on how many lives you have left, ex. when 2 lives only 2 marios get blit
            screen.blit(lifespic,((10+(i*20)),2))
            
        if lifes == 0:                   #when your lives = 0 then you get sent to the death page where it tells you your score and 
            screen.blit(deathpage,(0,0)) #shows you a picture of dead mario before restarting the game
            barrels = []                 #this gets rid of all the barrels so they stop rolling and it allows the game to move faster
            ScoreDraw = MyFont2.render(str(score+hammerpoints+barrelpoints),True,white) #this shows your total score 
            screen.blit(ScoreDraw,(300,295))
            display.flip()
            time.wait(5000)
            page = "Title Page"          #after losing you then get sent back to the start
            
    Marioy += gravity
    if onGround(Mariox,Marioy): #when mario is on the ground garity == 0 
        gravity = 0
        Marioy=findGround(Mariox,Marioy) #makes sure hes on the ground, then once hes on the ground, thats make sit true
        ground = True
    
    gravity += 0.3
    MarioFrameDelay -=1
    MarioFrame += 1
    DkframeDelay =-2
    FDelay -=1
    display.flip()
    myClock.tick(50)
#---------
quit()

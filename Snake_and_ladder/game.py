import pygame
import random

SCREEN_HEIGHT=800
SCREEN_WIDTH=1000
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
LIGHT_GREEN=(0,200,0)
RED=(255,0,0)
LIGHT_RED=(200,0,0)
BLUE=(0,0,255)
ORANGE=(255,125,0)
GAP=213
REV_GAP=93


pygame.init()
screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("Snakes and Ladders")
snake=pygame.image.load("snake.png")
snake.set_colorkey(BLACK)
pygame.display.set_icon(snake)
clock=pygame.time.Clock()
start=False
turn=1
logo=pygame.image.load("logo.jpg")
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.count=0
        self.start=False
        self.value=0
        self.direction="fwd"
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.x_speed=0
        self.y_speed=0

    def update(self):
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed




def circle(x,y,w,h,ac,ic):
    pygame.init()
    global count
    value=0
    
    font=pygame.font.Font('freesansbold.ttf',14)
    text=font.render("Click anywhere",True,BLACK)
    text_rect=text.get_rect()
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.ellipse(screen,ac,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)

        
    else:
        pygame.draw.ellipse(screen,ic,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)
   

def button(x,y,w,h,ac,ic,players,msg):
    pygame.init()
    font=pygame.font.Font('freesansbold.ttf',25)
    text=font.render(msg,True,BLACK)
    text_rect=text.get_rect()
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.ellipse(screen,ac,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)
        if click[0]==1:
            pygame.mixer.music.stop()
            main(players)
    else:
        pygame.draw.ellipse(screen,ic,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)
    
buttons=[[200,600,75,50,1,"1 P"],
         [375,600,75,50,2,"2 P"],
         [550,600,75,50,3,"3 P"],
         [725,600,75,50,4,"4 P"]]

def game_intro():
    pygame.init()
    intro=True
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play(loops=-1)
    logo_rect=logo.get_rect()
    logo_rect.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
        screen.fill(WHITE)
        screen.blit(logo,logo_rect)
        for lst in buttons:
            button(lst[0],lst[1],lst[2],lst[3],GREEN,LIGHT_GREEN,lst[4],lst[5])
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def quitgame():

    pygame.quit()

def end_button(x,y,w,h,ac,ic,msg,action=None):
    pygame.init()
    font=pygame.font.Font('freesansbold.ttf',25)
    text=font.render(msg,True,BLACK)
    text_rect=text.get_rect()
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)
        if click[0]==1:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
        text_rect.center=((x+w/2),(y+h/2))
        screen.blit(text,text_rect)


def message_display(text):
    pygame.init()
    largeText=pygame.font.Font('freesansbold.ttf',115)
    textsurf=largeText.render(text,True,BLACK)
    textrect=textsurf.get_rect()
    textrect.center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(textsurf,textrect)
    pygame.display.update()

def display_moves(moves,color):
    pygame.init()
    text=pygame.font.Font('freesansbold.ttf',25)
    textsurf=text.render(str(moves),True,BLACK)
    textrect=textsurf.get_rect()
    textrect.center=(97,350)
    pygame.draw.ellipse(screen,color,(47,300,100,100))
    screen.blit(textsurf,textrect)
    

def end_screen(msg):
    
    end=True

    while end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=False
        screen.fill(WHITE)
        message_display("Player "+str(msg)+" Wins")
        end_button(200,600,200,100,GREEN,LIGHT_GREEN,"Play Again!",game_intro)
        end_button(600,600,200,100,RED,LIGHT_RED,"Quit!",quitgame)
        pygame.display.flip()
        clock.tick(4)
    pygame.quit()

player_list=pygame.sprite.Group()
image=pygame.image.load("snake-and-ladder-board-game.jpg")
image.set_colorkey(WHITE)

def function(player,value,color):
    display_moves(value,color)
    print("value={}".format(value))
    if player.start==False and value==6:
        player.rect.x=155
        player.rect.y=708
        player.x_speed=0
        value=0
        player.start=True
    elif player.start==True and value!=0:
            
        if player.rect.x==155:
            player.rect.x+=74*value
            print(f"x= {player.rect.x}")
            print(f"y= {player.rect.y}")
        elif player.rect.y==33 and player.rect.x<685:
            if (player.rect.x-(74*value)>225):
                player.rect.x-=74*value
                if player.rect.x<240:
                    end_screen(turn)
           
                
        elif player.rect.x in range(225,905):
            if player.direction=="fwd":
                print("fd")
                player.rect.x+=74*value
         
                if player.rect.x>896:
                    diff=player.rect.x-896
                    player.rect.y-=75
                    player.rect.x=970
                    player.direction="rev"
                    player.rect.x=player.rect.x-diff
      
                    
            elif player.direction=="rev":
                player.rect.x-=74*value
                print("rev")
     
                if player.rect.x<230:
                    diff=230-player.rect.x
                    player.rect.y-=75
                    player.rect.x=156
                    player.direction="fwd"
                    player.rect.x=player.rect.x+diff
            if player.rect.y<28 or (player.rect.x<225 and player.rect.y<90):
                end_screen(turn)

   
        # no 2
        if 300<=player.rect.x<=340 and player.rect.y>700:
            player.rect.x=383
            player.rect.y=483
            player.direction="rev"

        #no 4
        if 448<=player.rect.x<=488 and player.rect.y>700:
            player.rect.x=676
            player.rect.y=633
            player.direction="rev"
        #no 9
        if 818<=player.rect.x<=848 and player.rect.y>700:
            player.rect.x=896
            player.rect.y=483
            player.direction="rev"
        
        #no 33
        if 740<=player.rect.x<=780 and 555>player.rect.y>480:
            player.rect.x=526
            player.rect.y=108
            player.direction="fwd"

        #no 52
        if 815<=player.rect.x<=855 and 350>player.rect.y>325:
            player.rect.x=748
            player.rect.y=108
            player.direction="fwd"

        #no 80
        if 225<=player.rect.x<=265 and 200>player.rect.y>180:
            player.rect.x=310
            player.rect.y=33
            player.direction="rev"

        #no 51
        if 890<=player.rect.x<=900 and 350>player.rect.y>325:
            player.rect.x=896
            player.rect.y=633
            player.direction="rev"

        #no 56
        if 525<=player.rect.x<=545 and 350>player.rect.y>325:
            player.rect.x=602
            player.rect.y=633
            player.direction="rev"

        #no 62
        if 300<=player.rect.x<=340 and 265>player.rect.y>250:
            player.rect.x=453
            player.rect.y=333
            player.direction="rev"

        #no 92
        if 818<=player.rect.x<=848 and 45>player.rect.y>30:
            player.rect.x=752
            player.rect.y=333
            player.direction="rev"

        #no 98
        if 375<=player.rect.x<=390 and 45>player.rect.y>30:
            player.rect.x=747
            player.rect.y=708
            player.direction="fwd" 

def main(gamers):
    global start
    global turn

    font=pygame.font.Font('freesansbold.ttf',25)
    check=0
    go1=0
    go2=0
    go3=0
    go4=0
    pygame.mixer.music.load("main_loop.mp3")
    pygame.mixer.music.play(loops=-1)

    if gamers==1:
        player_1=Player(25,550,"red.png")
        player_list.add(player_1)
    if gamers==2:
        player_1=Player(25,550,"red.png")
        player_2=Player(110,550,"green.png")
        player_list.add(player_1)
        player_list.add(player_2)
    if gamers==3:
        player_1=Player(25,550,"red.png")
        player_2=Player(110,550,"green.png")
        player_3=Player(67,470,"orange.png")
        player_list.add(player_1)
        player_list.add(player_2)
        player_list.add(player_3)
    if gamers==4:
        player_1=Player(25,550,"red.png")
        player_2=Player(110,550,"green.png")
        player_3=Player(25,470,"orange.png")
        player_4=Player(110,470,"blue.png")
        player_list.add(player_1)
        player_list.add(player_2)
        player_list.add(player_3)
        player_list.add(player_4)
    done=False
    while not done:
        mouse=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True

        
        screen.fill(BLACK)

        circle(50,650,100,100,RED,LIGHT_RED)

        if gamers==1:
            turn=1
        if turn==1:
            
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                if check==0:
                    value1=0
                    check=1
                elif check==1:
                    go1=1
                    value1=random.randrange(1,7)
                    if value1==6:
                        go1=0
                        turn=1
                    
                    #value1=1
                    function(player_1,value1,RED)


                if gamers>1 and go1==1:
                    turn=2
                #value=0
                            
        elif turn==2:
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                go2=1
                value2=random.randrange(1,7)
                if value2==6:
                    go2=0
                    turn=2

                function(player_2,value2,GREEN)
  

                if gamers>2 and go2==1:
                    turn=3
                elif gamers==2 and go2==1:
                    turn=1
        
        
        elif turn==3:
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                go3=1
                value3=random.randrange(1,7)
                if value3==6:
                    go3=0
                    turn=3
                function(player_3,value3,ORANGE)  
                            
                if gamers>3 and go3==1:
                    turn=4
                elif gamers==3 and go3==1:
                    turn=1

        elif turn==4:
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                go4=1
                value4=random.randrange(1,7)
                if value4==6:
                    go4=0
                    turn=4
                function(player_4,value4,BLUE)
                            
                if go4==1:
                    turn=1

        player_list.update()
        screen.blit(image,[195,0])
        player_list.draw(screen)
        pygame.display.update()
        clock.tick(4)
    pygame.quit()
        
        
            

if start==False:
    game_intro()
pygame.quit()
    
    

import pygame,sys,random,time
from pygame.locals import *    #从pygame模块中导入常用的函数和常量
score=0
pause=False
black_color=pygame.Color(0,0,0)
white_color=pygame.Color(255,255,255)
red_color=pygame.Color(255,0,0)
grey_color=pygame.Color(150,150,150)
green_color=(0,200,0)
bright_green=(0,255,0)
blue_color=(0,0,200)
bright_blue=(0,0,255)
#游戏结束
def GameOver(gamesuface):
    GameOver_font=pygame.font.SysFont('MicrosoftYaHei',16)
    GameOver_color=GameOver_font.render('Game over',True,grey_color)
    GameOver_location=GameOver_color.get_rect()
    GameOver_location.midtop=(320,10)
    gamesuface.blit(GameOver_color,GameOver_location)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def showScore(gamesuface):
    global  score
    score_font=pygame.font.SysFont('宋体',30,True)
    score_color=score_font.render(u'Score : %d' %score,True,[255,0,0],[20,20])
    score_location=score_color.get_rect()
    score_location.midtop=(700,20)
    gamesuface.blit(score_color,score_location)
    pygame.display.flip()


def text_objects(text,font):
    textSuface=font.render(text,True,black_color)
    return textSuface,textSuface.get_rect()
def button(gamesuface,msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamesuface,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
        else:
            pygame.draw.rect(gamesuface,ic,(x,y,w,h))
            smallText=pygame.font.SysFont('comicsansms',20)
            textSurf,textRect=text_objects(msg,smallText)
            textRect.center=((x+(w/2),(y+(h/2))))
            gamesuface.blit(textSurf,textRect)
def unpause():
    global pause
    pause=False
def pause(gamesuface):
    global pause
    largeText=pygame.font.SysFont('comicsansms',115)
    TextSurf,TextRect=text_objects('pause',largeText)
    TextRect.center=(320,240)
    gamesuface.blit(TextSurf,TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        button('continue',150,450,100,50,green_color,bright_green,unpause())
        button('Quit',550,450,100,50,blue_color,bright_blue,GameOver(gamesuface))
        pygame.display.flip()




#定义主函数
def main():
    global score
    pygame.init()

    ftpsClock=pygame.time.Clock()
    gamesuface= pygame.display.set_mode((800,480))
    pygame.display.set_caption('Snake')

    #初始化蛇的起始位置
    snakeposition=[100,100]
    #初始化贪吃蛇的长度
    snakelength=[[100,100],[80,100],[60,100]]
    #初始化目标方块的位置
    square_purpose=[300,300]
    #初始化一个数来判断目标方块是否存在
    square_position=1
    #初始化蛇的移动方向
    derection='right'
    change_derection=derection
    #游戏分数

    #进行游戏主循环
    while True:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==ord('d'):
                    change_derection='right'
                if event.key==pygame.K_LEFT or event.key==ord('a'):
                    change_derection='left'
                if event.key==pygame.K_UP or event.key==ord('w'):
                    change_derection='up'
                if event.key==pygame.K_DOWN or event.key==ord('s'):
                    change_derection='down'
                if event.key==pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key==pygame.K_SPACE:
                    pause(gamesuface)


        #判断移动方向是否相反
        if change_derection=='left' and not  change_derection=='right':
            derection=change_derection
        if change_derection=='right' and not change_derection=='left':
            derection=change_derection
        if change_derection=='up'  and not change_derection=='down':
            derection=change_derection
        if change_derection=='down' and not change_derection=='up':
            derection=change_derection
        #根据移动方向，改变坐标
        if derection=='left':
            snakeposition[0]-=20
        if derection=='right':
            snakeposition[0]+=20
        if derection=='up':
            snakeposition[1]-=20
        if derection=='down':
            snakeposition[1]+=20

        #增加蛇的长度：   头部增加
        snakelength.insert(0,list(snakeposition))   #0表示插入到list的头部，list(snakeposition)是要插入的对象

        #判断食物是否被吃掉
        if snakeposition[0]==square_purpose[0] and snakeposition[1]==square_purpose[1]:
            square_position=0     #表示食物已经被吃掉
            score+=1
        else:
            #尾部减少
            snakelength.pop()
        #重新生成目标方块
        if square_position==0:
            x=random.randrange(1,32)
            y=random.randrange(1,24)
            square_purpose=[int(x*20),int(y*20)]
            square_position=1

        #绘制pygame显示层ssssss
        gamesuface.fill(black_color)    #背景黑色
        showScore(gamesuface)
        for position in snakelength:
            pygame.draw.rect(gamesuface,white_color,pygame.Rect(position[0],position[1],20,20))   #绘制蛇
            pygame.draw.rect(gamesuface,red_color,pygame.Rect(square_purpose[0],square_purpose[1],20,20))   #绘制食物
        for y in range(0,24):
            pygame.draw.rect(gamesuface, white_color, pygame.Rect(620,int(20*y), 20, 20))  # 绘制墙

        #刷新pygame显示层
        pygame.display.flip()

        if snakeposition[0]<0 or snakeposition[0]>600:    #x坐标约束
            GameOver(gamesuface)
        if snakeposition[1]<0 or snakeposition[1]>460:    #y坐标约束
            GameOver(gamesuface)
        for snakebody in snakelength[1:]:
            if snakeposition[0]==snakebody[0] and snakeposition[1]==snakebody:
                GameOver(gamesuface)
        #控制游戏速度
        ftpsClock.tick(5)

if __name__=='__main__':
    main()













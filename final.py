import pygame as pg, random, math
import os
from pygame.locals import QUIT,MOUSEBUTTONUP
from random import randint

level=0

#文字
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)
    
#初始畫面 
def draw_init():
    screen.blit(background_img, (0,0))
    draw_text(screen, 'Have Fun Game!', 34, screen.get_width()/2,screen.get_height()/6)
    draw_text(screen, '第一關:打磚塊', 64, screen.get_width()/2,screen.get_height()/3)
    draw_text(screen, '藉由 ← → 一起把磚塊打掉吧~!', 22,screen.get_width()/2, screen.get_height()/1.5)
    draw_text(screen, '點擊滑鼠左鍵開始遊戲!', 15, screen.get_width()/2,screen.get_height()*3/4)
    pg.display.update()
    # waiting = True
    # while waiting:
    #     clock.tick(40)
    #     # 取得輸入
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()                
    #             return True
    #         buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
    #         if buttons[0]: 
    #             waiting = False
    #             return False     
            
#第二關畫面             
def two_init():
    screen.blit(background_img, (0,0))
    # draw_text(screen, '第二關:OOXX!', 64, screen.get_width()/2,screen.get_height()/3)
    # draw_text(screen, '藉由滑鼠點擊格子 一起打敗對手吧~!', 22,screen.get_width()/2, screen.get_height()/1.5)
    # draw_text(screen, '點擊滑鼠左鍵開始遊戲!', 18, screen.get_width()/2,screen.get_height()*3/4)
    draw_text(screen, '第二關:猜數字!', 64, screen.get_width()/2,screen.get_height()/3)
    draw_text(screen, '請在框框中猜數字 1~100 答對即可過關', 22,screen.get_width()/2, screen.get_height()/1.5)
    draw_text(screen, '點擊滑鼠左鍵開始遊戲!', 18, screen.get_width()/2,screen.get_height()*3/4)
    pg.display.update()
    waiting = True
    pg.display.update()
    waiting = True
    while waiting:
        clock.tick(40)
        # 取得輸入
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()                
                return True
            buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
            if buttons[0]:
                # OOXX()
                guessing()
                waiting = False
                return False
#第三關畫面              
def three_init():
    screen.blit(background_img, (0,0))
    # draw_text(screen, '第三關:猜數字!', 64, screen.get_width()/2,screen.get_height()/3)
    # draw_text(screen, '請在框框中猜數字 1~100 答對即可過關', 22,screen.get_width()/2, screen.get_height()/1.5)
    draw_text(screen, '第三關:1A2B!', 64, screen.get_width()/2,screen.get_height()/3)
    draw_text(screen, '請在框框中猜4位數字 不可重複 答對即可過關', 22,screen.get_width()/2, screen.get_height()/1.5)
    draw_text(screen, '點擊滑鼠左鍵開始遊戲!', 18, screen.get_width()/2,screen.get_height()*3/4)
    pg.display.update()
    waiting = True
    while waiting:
        clock.tick(40)
        # 取得輸入
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()  
                return True
            buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
            if buttons[0]:
                AABB()    
                waiting = False
                return False
                         
#結束畫面  
def final_init():
    screen.blit(background_img, (0,0))
    draw_text(screen, '遊戲結束!!', 64, screen.get_width()/2,screen.get_height()/3)
    draw_text(screen, '按A鍵可重新開始遊戲!', 18, screen.get_width()/2,screen.get_height()*3/4)
    pg.display.update()
    waiting = True
    while waiting:
        clock.tick(40)
        # 取得輸入
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()                
                return True
            key_pressed = pg.key.get_pressed()
            if key_pressed[pg.K_a]:
                pg.init()
                pg.display.update()
                brickgame()  
                waiting = False
                #playing = True
                return False    
                       
            
#建立球體
class Ball(pg.sprite.Sprite):
    dx = 0         #x位移量
    dy = 0         #y位移量
    x = 0          #球x坐標
    y = 0          #球y坐標
    direction = 0  #球移動方向
    speed = 0      #球移動速度
 
    def __init__(self, sp, srx, sry, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        #繪製球體
        #self.image = pg.Surface([radium*2, radium*2])  
        self.image = pg.transform.scale(ball_img,(90,90))
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)       #初始位置
        self.direction = random.randint(40,70)  #移動角度

 #球體移動 
    def update(self):         
        radian = math.radians(self.direction)    #角度轉為弳度
        self.dx = self.speed * math.cos(radian)  #球水平運動速度
        self.dy = -self.speed * math.sin(radian) #球垂直運動速度
        self.x += self.dx     #計算球新坐標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        #到達左右邊界
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
            self.bouncelr()
        elif(self.rect.top <= 10):  #到達上邊界
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):  #到達下邊界出界
            return True
        else:
            return False
    def bounceup(self):  #上邊界反彈
        self.direction = 360 - self.direction

    def bouncelr(self):  #左右邊界反彈
        self.direction = (180 - self.direction) % 360

#磚塊類別            
class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([78, 38])  #原磚塊長寬38x13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
#板子類別
class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        #self.image = pg.image.load("dog.jpg")  #圖片!!!!!!!!!
        #self.image = pg.Surface([50, 20])
        self.image = pg.transform.scale(pad_img,(95,40)) 
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 25
        
        
#板子位置隨滑鼠移動 (原本為滑鼠移動)
    def update(self):  
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_RIGHT]:
            self.rect.x += 15
        if key_pressed[pg.K_LEFT]:
            self.rect.x -= 15
            
        if self.rect.right > screen.get_width():
          self.rect.right = screen.get_width()
        if self.rect.left < 0:
            self.rect.left = 0

                       
def brickgame():
    downmsg=""
    score = 0  #得分   
    show_init = True    
    playing = False  #開始時球不會移動
    running = True  
    clock = pg.time.Clock()
    while running:    
        if show_init:
            close = draw_init()
            if close:
                break
            show_init = False
            allsprite = pg.sprite.Group()  #建立全部角色群組
            bricks = pg.sprite.Group()     #建立磚塊角色群組
            ball = Ball(10, 300, 300, 15, (255,123,188)) #建立粉球(原本15, 300, 350, 10, (255,123,188))
            allsprite.add(ball)  #加入全部角色群組
            pad = Pad()          #建立滑板球物件
            allsprite.add(pad)   #加入全部角色群組
            
            #建立磚塊
            for row in range(0, 4):          #4列方塊
                for column in range(0, 10):  #每列10磚塊
                    if row == 1 or row == 0: 
                        brick = Brick((153,205,255), column * 80 + 1, row * 40 + 1)   #原位置為40*15
                    if row == 2: 
                        brick = Brick((94,175,254), column * 80 + 1, row * 40 + 1)    
                    if row == 3 or row == 4:  
                        brick = Brick((52,153,207), column * 80 + 1, row * 40 + 1)  
                    bricks.add(brick)     #加入磚塊角色群組
                    allsprite.add(brick)  #加入全部角色群組
                    score = 0  #得分     
                    downmsg = "Score: " + str(score)
        clock.tick(40)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False 
            buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
            if buttons[0]:    #按滑鼠左鍵後球可移動       
                playing = True
                
        
        #遊戲進行中 down
        if playing == True:  
            screen.blit(background_img , (0,0))  #清除繪圖視窗
            fail = ball.update()  #移動球體
            if fail:              #球出界
                show_init = True
                two_init()
            pad.update()          #更新滑板位置
            #檢查球和磚塊碰撞
            hitbrick = pg.sprite.spritecollide(ball, bricks, True)  
            if len(hitbrick) > 0:  #球和磚塊發生碰撞
                score += len(hitbrick)  #計算分數
                ball.rect.y += 20  #球向下移
                ball.bounceup()    #球反彈
                if len(bricks) == 0:  #所有磚塊消失
                    show_init = True
                    
                    
            #檢查球和滑板碰撞
            hitpad = pg.sprite.collide_rect(ball, pad)  
            if hitpad:  #球和滑板發生碰撞
                ball.bounceup()  #球反彈
            allsprite.draw(screen)  #繪製所有角色
            downmsg = "Score: " + str(score)
            
        #繪製下方訊息    
        message = dfont.render(downmsg+"/40", 1, (255,255,255))
        screen.blit(message, (10,screen.get_height()-30))
        pg.display.update()            

#def OOXX():
    
    
    # pg.init()#初始化
    # screen.fill((0,0,0))#視窗顏色
    # clock = pg.time.Clock()
    # font = pg.font.SysFont("arial",20)#字體大小
    # gameover = False
    # left = False
    # win = 0
    # player = 1#預設為1P
    # data = [[0,0,0],[0,0,0],[0,0,0]]#建立一個3x3陣列
    # main_surface = pg.Surface((200,200))#建立主要圖層
    # pg.draw.rect(main_surface,(150,150,150),[25,25,150,150],3)#畫出格線
    # pg.draw.line(main_surface,(150,150,150),(25,75),(175,75),3)
    # pg.draw.line(main_surface,(150,150,150),(25,125),(175,125),3)
    # pg.draw.line(main_surface,(150,150,150),(75,25),(75,175),3)
    # pg.draw.line(main_surface,(150,150,150),(125,25),(125,175),3)
    
    # while 1:
    #     x,y = pg.mouse.get_pos()#滑鼠游標的座標
    #     left = pg.mouse.get_pressed()[0]#滑鼠左鍵是否被按下
    #     for event in pg.event.get():#退出遊戲判定
    #         if event.type == QUIT:
    #             pg.quit()
    #             break
    #         if event.type == MOUSEBUTTONUP:#滑鼠鍵放開判定
    #             if left:
    #                 left = "depress"#如果滑鼠左鍵放開,則把left設為depress
        
    #     prompt_surface = pg.Surface((200,25))#建立空的提示圖層
    #     if gameover == True:
    #         draw_text(screen, '點擊滑鼠即可至第三關!', 18, screen.get_width()/2,screen.get_height()*3/4)
    #         clock.tick(40)
    #     # 取得輸入
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 pg.quit()                
    #                 return True
    #             if event.type == pg.MOUSEBUTTONDOWN:
    #                 three_init()
    #             # buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
    #             # if buttons[0]:
    #             #     three_init()
    #             #     return False
            
    #     if win == -1:#平手
    #         pg.display.update()
    #         prompt_surface.blit(font.render("No one won...",True,(255,255,255)),(50,0))#印出沒人贏
    #         gameover = True
            
          
    #     elif win == 1 or win == 2:#某人贏了
    #         prompt_surface.blit(font.render("P%d win!"%win,True,(255,255,255)),(75,0))#印出誰贏
    #         gameover = True


            
    #     elif left == "depress" and abs(x-100) < 75 and abs(y-100) < 75:#滑鼠按下判定區
    #         i,j = int((x-25)//50),int((y-25)//50)#計算行列
    #         if data[i][j] == 0:#空格子才能選
    #             if player == 1:
    #                 data[i][j] = 1
    #                 pg.draw.circle(main_surface,(50,255,50),(50+50*i,50+50*j),15,3)#P1畫圈
    #                 player = 2#換人
    #             elif player == 2:
    #                 data[i][j] = 2
    #                 for i in range(1, 10):
  

def guessing():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 28)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    aa=''
    y=20
    done = False
    answer = randint(1, 100)
    prompt_surface = pg.Surface((screen.get_width(),300))#建立空的提示圖層
    prompt_surface.blit(font.render(str(answer),True,(20,20,20)),(screen.get_width()-80,screen.get_height()/2))
      
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        try:
                            text = int(text)
                        except ValueError:
                            aa="error"
                            continue
                            
                        if int(text) < 1 or int(text)>= 100 :
                            aa="error" 
                            continue 
                        if text == answer:
                            aa="bingo！"
                            draw_text(screen, '點擊滑鼠即可至第三關!', 18, screen.get_width()/2,screen.get_height()*3/4)
                            clock.tick(40)
                            # for event in pg.event.get():
                            #     if event.type == pg.QUIT:
                            #         pg.quit() 
                            #     buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
                            #     if buttons[0]:
                            #         three_init()
                            three_init()
                            break
                        
                        elif text <= answer:
                            aa=",too small"
                        else:
                            aa=",too big" 
                                 
                        prompt_surface.blit(font.render("You input:"+str(text)+aa,True,(255,255,255)),(50,y))
                        pg.display.flip()
                        text = '' 
                        y=y+30
                            
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
             
        
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(str(text), True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        draw_text(screen, '請在框框中猜數字(1-100)，猜對即可過關', 18, screen.get_width()/2,screen.get_height()/10)
        screen.blit(prompt_surface,(0,175))#印出提示圖層
        pg.display.flip()
        clock.tick(30)
        
def ending():
    screen.fill((0,0,0))
    draw_text(screen, 'Bingo!', 64, screen.get_width()/2,screen.get_height()/3)
    draw_text(screen, '恭喜你成功了', 22,screen.get_width()/2, screen.get_height()/1.5)
    #draw_text(screen, '點擊滑鼠左鍵 結算成績!', 18, screen.get_width()/2,screen.get_height()*3/4)
    draw_text(screen, '點擊滑鼠左鍵 結束遊戲!', 18, screen.get_width()/2,screen.get_height()*3/4)
    pg.display.update()
    waiting = True
    while waiting:
        clock.tick(40)
        # 取得輸入
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()                
                return True
            buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
            if buttons[0]:
                final_init()
                waiting = False
                #playing = True
                return False


    # def succ():
    #     screen.fill((0,0,0))
    #     draw_text(screen, 'Bingo!', 64, screen.get_width()/2,screen.get_height()/3)
    #     draw_text(screen, '恭喜你成功了', 22,screen.get_width()/2, screen.get_height()/1.5)
    #     draw_text(screen, '點擊滑鼠左鍵 結算成績!', 18, screen.get_width()/2,screen.get_height()*3/4)
    #     pg.display.update()
    #     waiting = True
    #     while waiting:
    #         clock.tick(40)
    #         # 取得輸入
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 pg.quit()                
    #                 return True
    #             buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
    #             if buttons[0]:
    #                 final_init()
    #                 waiting = False
    #                 #playing = True
    #                 return False  
def AABB():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 28)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text=""
    aa=''
    y=20
    done = False
    AA=BB=0
    # answer = randint(1,100)
    norepeat=[0,1,2,3,4,5,6,7,8,9]#所有答案結果
    answer=[0,0,0,0]#四個答案
    while len(norepeat) == 10:
        for i in range(4):
            answer[i]=norepeat[randint(0,len(norepeat)-1)]#從norepeat隨機取數當答案
            norepeat.remove(answer[i])#把已經有的答案從norepeat中去除，避免有重複的數字
            
    
    prompt_surface = pg.Surface((screen.get_width(),300))#建立空的提示圖層
    prompt_surface.blit(font.render(str(answer),True,(20,20,20)),(screen.get_width()-80,screen.get_height()/2))
      
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        AA=BB=0#AA為有幾A，BB為有幾B
                        try:
                            text = str(text)
                        except ValueError:
                            aa="error"
                            continue 
                        #遊戲運算
                        for i in range(4):
                            for j in range(4):
                                if str(text[i])==str(answer[j]):
                                    #判斷為A
                                    if i==j:
                                        AA += 1
                                    else:
                                        BB += 1
                                    
                        if AA==4:
                            aa="bingo！"
                            ending()
                            break
                        else:
                            aa=str(AA)+"A"+str(BB)+"B"                                

                        prompt_surface.blit(font.render("You input:"+str(text),True,(255,255,255)),(50,y))
                        prompt_surface.blit(font.render(str(aa),True,(255,255,255)),(300,y))
                        pg.display.flip()
                        text=""
                        y=y+30
                            
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(str(text), True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        draw_text(screen, '請在框框中猜4位數字 不可重複 答對即可過關', 18, screen.get_width()/2,screen.get_height()/10)
        screen.blit(prompt_surface,(0,175))#印出提示圖層
        pg.display.flip()
        clock.tick(30)

    # if __name__ == '__main__':
    #     pg.init()
    #     main()
    #     pg.quit()

 
# 遊戲初始化 and 創建視窗
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((800,500))
pg.display.set_caption("have Fun!") #標題
clock = pg.time.Clock()
level = 0
# 載入圖片音樂文字
background_img = pg.image.load(os.path.join("img", "background.png"))
background_img = background_img.convert()
ball_img = pg.image.load(os.path.join("img", "earth.png"))
pad_img = pg.image.load(os.path.join("img", "pad.png"))
pg.mixer.music.load(os.path.join("sound", "background.mp3"))
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(-1) #無限循環
font_name = os.path.join("font.ttf")   
sfont = pg.font.SysFont("SimHei", 14)   
lfont = pg.font.SysFont("SimHei", 14)   
dfont = pg.font.SysFont("Arial", 20)    #下方訊息字體
ffont = pg.font.SysFont("SimHei", 32)   #結束程式訊息字體

# 遊戲迴圈
# 運行的程式碼               
   
brickgame()   
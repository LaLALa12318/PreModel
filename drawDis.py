import turtle as tl
import random
from PIL import Image
import cv2
import math
import os

# tl = turtle.Turtle()  # 海龟的对象
def f1(L):
    tl.fillcolor("black")  # 三角形填充颜色
    tl.begin_fill()  # 填充开始
    for i in range(3):
        tl.fillcolor()
        tl.forward(L)
        tl.right(120)
    tl.end_fill()  # 填充结束
    tl.hideturtle()  # 隐藏画笔形状

# #画圆形病害
# def drawCricle():
#     L = 50  # 边长
#     N = 8  # 角的个数
#     jiaodu = 180 - 360 / (N)  # 每个三个型相对于上一个三角的角度，left转动
#
#     tl.speed(0)
#     tl.delay(0)  # 绘画延时为0
#
#
#
#     # 画外部的三角
#     tl.hideturtle()  # 隐藏画笔形状
#     for i in range(N):
#
#         tl.left(jiaodu)  # 下一个三角形的角度
#         tl.penup()
#         tl.forward(L)  # 新三角的起始位置
#         tl.pendown()
#         tl.right(180)  # 转动到画三角形的相对0度
#
#         f1(L)
#
#     # 画内部的多边形
#     tl.fillcolor("red")  # 填充颜色
#     tl.begin_fill()
#     for i in range(N):
#         tl.left(jiaodu)
#         tl.forward(L)
#         tl.right(180)  # 转动到画三角形的相对0度
#
#     tl.end_fill()
#     tl.hideturtle()  # 隐藏画笔形状
#     # tl.screen.mainloop()


#画圆形病害
def drawEdge():
    # tl.setup(400, 400)
    tl.screensize(400, 400)
    n = random.randint(10, 20)
    # 正n角形参数
    tl.speed(0)
    tl.delay(0)  # 绘画延时为0
    tl.width(2)  # 线粗2像素
    tl.pensize(15)
    tl.color('black', 'black')  # 设置边框和填充的颜色
    side = n  # 边数
    tl.begin_fill()
    for i in range(side):  # 循环一次画一次边，五角星5边，所以循环5次
        tl.forward(100)  # 边长
        tl.left(180 - 180 / side)  # 旋转角度
    tl.end_fill()
    tl.hideturtle()

#画方形病害
def drawBox():
    tl.screensize(400, 400)
    length = random.randint(100, 200)
    width=length/2
    point_Num=random.randint(3,6)

    tl.speed(0)
    tl.delay(0)
    tl.hideturtle()
    #下边长
    # tl.right(90)
    tl.fillcolor("black")  # 设置填充颜色绿色
    tl.begin_fill()  # 开始填充图像
    tl.left(90)
    tl.fd(width)  # t.forward可以写成t.fd,即fd。
    tl.right(90)
    tl.fd(length)
    tl.right(90)
    tl.fd(width)
    tl.right(90)
    tl.fd(length)
    tl.end_fill()  # 停止填充
    tl.right(180)


    for i in range(0,point_Num):
        pos=random.randint(0,length)
        r=random.randint(2,(int)(length/point_Num))
        tl.penup()
        tl.goto(pos,-1*r/2)
        tl.pendown()
        tl.fillcolor("black")  # 设置填充颜色绿色
        tl.begin_fill()
        # tl.color('black')
        tl.circle(r)
        tl.end_fill()

    for i in range(0, point_Num):
        pos = random.randint(0, length)
        r = random.randint(2, (int)(length / point_Num))
        tl.penup()
        tl.goto(pos, -1 * r / 2+width)
        tl.pendown()
        tl.fillcolor("black")  # 设置填充颜色绿色
        tl.begin_fill()
        # tl.color('black')
        tl.circle(r)
        tl.end_fill()
    for i in range(0, (int)(point_Num/2)):
        pos = random.randint(0, (int)(width))
        r = random.randint(2, (int)(width / point_Num))
        tl.penup()
        tl.goto(1*r/2, pos)
        tl.pendown()
        tl.fillcolor("black")  # 设置填充颜色绿色
        tl.begin_fill()
        # tl.color('black')
        tl.circle(r)
        tl.end_fill()
    for i in range(0, (int)(point_Num / 2)):
        pos = random.randint(0, (int)(width))
        r = random.randint(2, (int)(width / point_Num))
        tl.penup()
        tl.goto(-1 * r / 2+length, pos)
        tl.pendown()
        tl.fillcolor("black")  # 设置填充颜色绿色
        tl.begin_fill()
        # tl.color('black')
        tl.circle(r)
        tl.end_fill()
    tl.hideturtle()
    tl.goto(0,0)
    tl.seth(0)




def drawManhole(savePath,r,flag):
    road_Path=r"D:\lalala_Road_Data/"+str(random.randint(0,19))+"/"
    #圆形井盖
    if(flag==0):
        point_Pos = random.randint(0, 19)  # 圆心位置
        start_Pos = (int)(point_Pos - (r / 8))
        end_Pos = math.ceil(point_Pos + (r / 8))

        if (start_Pos < 0):
            start_Pos = 0
        if (end_Pos > 20):
            end_Pos = 20

        x = random.randint(100, 500)
        y = random.randint(2, 5)
        for i in range(start_Pos, point_Pos):
            manholeLength = (int)(math.sqrt(r * r - (point_Pos - i) * (r / 8) * (point_Pos - i) * (r / 8))) * 2
            img = cv2.imread(road_Path + str(i) + ".png", 1)
            print(savePath + str(i) + ".png")
            img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
            pos_Left = ((int)(x - manholeLength / 2), 0)
            pos_Right = ((int)(x + manholeLength / 2), y)
            img_AfterDraw = cv2.rectangle(img, pos_Left, pos_Right, (0, 255, 0), -1)
            img_AfterDraw=cv2.rectangle(img_AfterDraw, ((int)(x - manholeLength / 2),y),((int)(x + manholeLength / 2), 180),(0,0,0),-1)
            cv2.imwrite(savePath + str(i) + ".png", img_AfterDraw)

        for i in range(point_Pos, end_Pos):
            manholeLength = (int)(math.sqrt(r * r - (i - point_Pos) * (r / 8) * (i - point_Pos) * (r / 8))) * 2
            img = cv2.imread(road_Path + str(i) + ".png", 1)
            # print(img_AfterDraw)
            print(savePath + str(i) + ".png")
            img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
            pos_Left = ((int)(x - manholeLength / 2), 0)
            pos_Right = ((int)(x + manholeLength / 2), y)
            img_AfterDraw = cv2.rectangle(img, pos_Left, pos_Right, (0, 255, 0), -1)
            img_AfterDraw = cv2.rectangle(img_AfterDraw, ((int)(x - manholeLength / 2), y),((int)(x + manholeLength / 2), 180), (0, 0, 0), -1)
            cv2.imwrite(savePath + str(i) + ".png", img_AfterDraw)
        if (start_Pos != 0):
            for i in range(0, start_Pos):
                img = cv2.imread(road_Path + str(i) + ".png", 1)
                print(road_Path + str(i) + ".png", end_Pos)
                img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(savePath + str(i) + ".png", img)
        if (end_Pos != 19):
            for i in range(end_Pos, 20):
                img = cv2.imread(road_Path + str(i) + ".png", 1)
                print(road_Path + str(i) + ".png", end_Pos)
                img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)

                cv2.imwrite(savePath + str(i) + ".png", img)

    #方形井盖
    elif(flag==1):
        manholeLength=r[0]
        manholeWidth=r[1]
        point_Pos = random.randint(0, 19)  # 圆心位置
        start_Pos = (int)(point_Pos - (manholeWidth / 8))
        end_Pos = math.ceil(point_Pos + (manholeWidth / 8))

        if (start_Pos < 0):
            start_Pos = 0
        if (end_Pos > 20):
            end_Pos = 20
        x = random.randint(100, 500)
        y = random.randint(2, 5)

        for i in range(start_Pos, point_Pos):
            img = cv2.imread(road_Path + str(i) + ".png", 1)
            print(savePath + str(i) + ".png")
            img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
            pos_Left = ((int)(x - manholeLength / 2), 0)
            pos_Right = ((int)(x + manholeLength / 2), y)
            img_AfterDraw = cv2.rectangle(img, pos_Left, pos_Right, (0, 255, 0), -1)
            img_AfterDraw = cv2.rectangle(img_AfterDraw, ((int)(x - manholeLength / 2), y),((int)(x + manholeLength / 2), 180), (0, 0, 0), -1)
            cv2.imwrite(savePath + str(i) + ".png", img_AfterDraw)
        for i in range(point_Pos, end_Pos):
            img = cv2.imread(road_Path + str(i) + ".png", 1)
            print(savePath + str(i) + ".png")
            img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
            pos_Left = ((int)(x - manholeLength / 2), 0)
            pos_Right = ((int)(x + manholeLength / 2), y)
            img_AfterDraw = cv2.rectangle(img, pos_Left, pos_Right, (0, 255, 0), -1)
            img_AfterDraw = cv2.rectangle(img_AfterDraw, ((int)(x - manholeLength / 2), y),((int)(x + manholeLength / 2), 180), (0, 0, 0), -1)
            cv2.imwrite(savePath + str(i) + ".png", img_AfterDraw)
        if (start_Pos != 0):
            for i in range(0, start_Pos):
                img = cv2.imread(road_Path + str(i) + ".png", 1)
                print(road_Path + str(i) + ".png", end_Pos)
                img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(savePath + str(i) + ".png", img)
        if (end_Pos != 19):
            for i in range(end_Pos, 20):
                img = cv2.imread(road_Path + str(i) + ".png", 1)
                print(road_Path + str(i) + ".png", end_Pos)
                img = cv2.resize(img, (600, 180), interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(savePath + str(i) + ".png", img)

if __name__ == '__main__':
    # #分辨率0.01 像素*0.01=尺寸
########################################################  绘制井盖
   for j in range(0,3):
       for i in range(0, 20):
           r_Szie = [25, 30, 35]  # 对应尺寸500、600、700mm
           r_SzieType = ['500mm', '600mm', '700mm']
           path = r"E:\PycharmProject\test\SimulateTDModel\disModel\manhole/"
           if (not (os.path.exists(path + r_SzieType[j]))):
               os.mkdir(path + r_SzieType[j])
           if(not (os.path.exists(path + r_SzieType[j]+"/"+str(i)))):
               os.mkdir(path + r_SzieType[j]+"/"+str(i))

           # r_Index = random.randint(0, 2)
           # r = r_Szie[r_Index]

           drawManhole(path + r_SzieType[j]+"/"+str(i)+ "/",r_Szie[j],0)

   for j in range(0,3):
       for i in range(0,20):
           manholeSize=[[75,45],[60,60],[40,60]]
           path = r"E:\PycharmProject\test\SimulateTDModel\disModel\manhole/"
           firstPath=path+str(manholeSize[j][0]*10)+"-"+str(manholeSize[j][1]*10)+"mm"
           print(firstPath)
           if (not (os.path.exists(firstPath))):
               os.mkdir(firstPath)
           if (not (os.path.exists(firstPath + "/" + str(i)))):
               os.mkdir(firstPath + "/" + str(i))
           drawManhole(firstPath + "/" + str(i)+"/",manholeSize[j],1)








#########################################################  绘制病害
    # dis_Size=[[20,50],[50,80],[80,110],[110,140]]
    # # drawCricle()
    # for i in dis_Size:
    #     #cricle
    #     #box
    #     path = r"E:\PycharmProject\test\SimulateTDModel\disShape\box/" + str(i[0])+"-"+str(i[1])
    #     if (not (os.path.exists(path))):
    #         os.mkdir(path)
    #     for j in range(0,20):
    #         pic_Size = random.randint(i[0], i[1])
    #         # drawEdge()#圆形病害
    #         drawBox()
    #         ts = tl.getscreen()
    #         ts.getcanvas().postscript(file=r"./circle1.eps")
    #         tl.clearscreen()
    #         im = Image.open("./circle1.eps")
    #         box = (360, 220, 480, 320)
    #         #cricle(355, 255, 442, 345)
    #         region = im.crop(box)
    #         region.save('./crop1.png')
    #
    #         img = cv2.imread('./crop1.png', 0)
    #         ret, binary = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
    #         binary_Save = cv2.resize(binary, (pic_Size, pic_Size), interpolation=cv2.INTER_NEAREST)
    #         #
    #         pic_Savepath = path + "/" + str(j) + "/"
    #         if (not (os.path.exists(pic_Savepath))):
    #             os.mkdir(pic_Savepath)
    #
    #
    #         dis_Mode=random.randint(0,2)
    #         pic_Num=(int)(pic_Size/8) #病害的尺寸，可以被雷达测线覆盖的数量，侧线间距8cm
    #         if (pic_Num % 2 == 0):
    #             pic_Num += 1
    #         for m in range(0,pic_Num):
    #
    #             if (dis_Mode == 0):  # 病害是对称的
    #                 print(i,j)
    #                 if(m<=pic_Num/2):
    #                     save_Size=(int)(pic_Size*(m+1)/(pic_Num/2))
    #                 else:
    #                     save_Size = (int)(pic_Size * ((pic_Num-m) / (pic_Num/2)))
    #
    #                 if(save_Size>0):
    #                     binary_Save = cv2.resize(binary, (save_Size, save_Size), interpolation=cv2.INTER_NEAREST)
    #                     cv2.imwrite(pic_Savepath + str(m) + ".png", binary_Save)
    #             elif (dis_Mode == 1):  # 病害由小到大
    #                 save_Size=(int)(pic_Size*((m+1)/pic_Num))
    #                 if (save_Size > 0):
    #                     binary_Save = cv2.resize(binary, (save_Size, save_Size), interpolation=cv2.INTER_NEAREST)
    #                     cv2.imwrite(pic_Savepath + str(m) + ".png", binary_Save)
    #             elif (dis_Mode == 2):  # 病害由大到小
    #                 save_Size = (int)(pic_Size * (1-(m + 1) / pic_Num))
    #                 if(save_Size>0):
    #                     binary_Save = cv2.resize(binary, (save_Size, save_Size), interpolation=cv2.INTER_NEAREST)
    #                     cv2.imwrite(pic_Savepath + str(m) + ".png", binary_Save)


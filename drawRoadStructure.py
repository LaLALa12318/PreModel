import turtle
import random
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch

# 生成随机数
def func1(amount,num):
    list1 = []
    for i in range(0,num-1):
        a = random.random()
        list1.append(a)
    list1.sort()
    list1.append(amount)

    list2 = []
    for i in range(len(list1)):
        if i == 0:
            b = list1[i]
        else:
            b = list1[i] - list1[i-1]
        list2.append(b)
    return list2



#画面层
def drawFirstLayer():

    turtle.speed(0)
    turtle.delay(0)
    turtle.tracer(False)
    #面层由细粒、中粒和粗粒组成    10
    # r细粒0.95-1.32（cm）==1-2个像素 red  厚度：4 cm==8 个像素点
    # r中粒1.6-1.9（cm）==3-4个像素 yellow  厚度：4-6 cm==8-12 个像素点
    # r粗粒1.9-2.65（cm）==4-5个像素 lightcoral  厚度：6-8 cm==12-16 个像素点
    for m in range(0,5000):
        select_Layer=random.random()*3
        if(select_Layer<=1):
            # 细粒
            #for i in range(0, 3000):
            x = random.randint(3, 397)
            y = random.randint(260, 270)
            depth = random.random() * 2.5
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("red")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer >1 ):
            # 中粒
            #for i in range(0, 700):
            x = random.randint(3, 397)
            y = random.randint(250, 260)
            depth = random.uniform(3.5, 5.5)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("yellow")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2):
            # 粗粒
            #for i in range(0, 900):
            x = random.randint(3, 397)
            y = random.randint(236, 252)
            depth = random.uniform(2.5, 4.5)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("lightcoral")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
    # 粗粒
    for i in range(0, 200):
        x = random.randint(3, 397)
        y = random.randint(236, 252)
        depth = random.uniform(2.5, 4.5)
        r = random.random() * depth  # 随机生成的半径

        turtle.penup()
        turtle.goto(x, y)
        turtle.begin_fill()  # 开始填充
        turtle.color("lightcoral")  # 填充
        turtle.circle(r)
        turtle.end_fill()  # 填充结束
        turtle.hideturtle()  # 隐藏画笔形状
    # 细粒
    for i in range(0, 1200):
        x = random.randint(3, 397)
        y = random.randint(262, 270)
        depth = random.random() * 2.5
        r = random.random() * depth  # 随机生成的半径

        turtle.penup()
        turtle.goto(x, y)
        turtle.begin_fill()  # 开始填充
        turtle.color("red")  # 填充
        turtle.circle(r)
        turtle.end_fill()  # 填充结束
        turtle.hideturtle()  # 隐藏画笔形状
    for i in range(0, 3000):
        x = random.randint(3, 397)
        y = random.randint(268, 270)
        depth = random.random() * 2.5
        r = random.random() * depth  # 随机生成的半径

        turtle.penup()
        turtle.goto(x, y)
        turtle.begin_fill()  # 开始填充
        turtle.color("red")  # 填充
        turtle.circle(r)
        turtle.end_fill()  # 填充结束
        turtle.hideturtle()  # 隐藏画笔形状

#画基层
def drawSecondLayer():
    # 基层厚度 20cm左右==40个像素点   30
    # 半径 0.5-1 60mm-70mm左右
    # blue 碎石
    # green 水泥混凝土
    # grey 砂砾
    turtle.speed(0)
    turtle.delay(0)
    layer1=0
    layer2=0
    layer3=0

    list_Ratio=func1(1,3)
    layer1_ratio =list_Ratio[0]
    layer2_ratio =list_Ratio[1]
    layer3_ratio = list_Ratio[2]

    allCount=30000
    for m in range(0, allCount):
        select_Layer = random.random() * 3
        if (select_Layer <= 1 ):
            layer1 += 1
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("blue")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            layer2+=1
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("green")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2 ):
            layer3+=1
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("grey")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状

    for m in range(0, 800):
        select_Layer = random.random() * 3
        if (select_Layer <= 1):
            x = random.randint(3, 397)
            y = random.randint(236, 240)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("blue")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            x = random.randint(3, 397)
            y = random.randint(236, 240)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("green")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2):
            x = random.randint(3, 397)
            y = random.randint(236, 240)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("grey")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状


    # 粗粒边界
    for i in range(0, 200):
        x = random.randint(3, 397)
        y = random.randint(235, 240)
        depth = random.uniform(2.5, 4.5)
        r = random.random() * depth  # 随机生成的半径

        turtle.penup()
        turtle.goto(x, y)
        turtle.begin_fill()  # 开始填充
        turtle.color("lightcoral")  # 填充
        turtle.circle(r)
        turtle.end_fill()  # 填充结束
        turtle.hideturtle()  # 隐藏画笔形状


#画垫层
def drawThirdLayer():
    #垫层厚度 15cm==30个像素
    #砂 slateblue
    #砾石 navy
    turtle.speed(0)
    turtle.delay(0)
    for m in range(0, 15000):
        select_Layer = random.random() * 2
        if (select_Layer <= 1):
            x = random.randint(3, 397)
            y = random.randint(160, 190)
            depth = random.uniform(0.5,1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("slateblue")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            x = random.randint(3, 397)
            y = random.randint(160, 190)
            depth = random.uniform(0.5,1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("navy")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状

    for m in range(0, 100):
        select_Layer = random.random() * 2
        if (select_Layer <= 1):
            x = random.randint(3, 397)
            y = random.randint(190, 192)
            depth = random.uniform(0.5,1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("slateblue")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            x = random.randint(3, 397)
            y = random.randint(190, 192)
            depth = random.uniform(0.5,1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("navy")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状

    #基层边界
    for m in range(0, 100):
        select_Layer = random.random() * 3
        if (select_Layer <= 1):
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("blue")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("green")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2):
            x = random.randint(3, 397)
            y = random.randint(190, 236)
            depth = random.uniform(0.5, 1)
            r = random.random() * depth

            turtle.speed(0)
            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("grey")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状


#画路基
def drawBasicLayer():
    #土1 gold
    #土2 peru
    #土3 saddlebrown
    turtle.speed(0)
    turtle.delay(0)
    for m in range(0, 20000):
        select_Layer = random.random() * 3
        if (select_Layer <= 1):
            # 细粒
            # for i in range(0, 3000):
            x = random.randint(3, 397)
            y = random.randint(0,160)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("gold")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            # 中粒
            # for i in range(0, 700):
            x = random.randint(3, 397)
            y = random.randint(0,160)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("peru")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2):
            # 粗粒
            # for i in range(0, 900):
            x = random.randint(3, 397)
            y = random.randint(0,160)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("saddlebrown")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状

    for m in range(0, 250):
        select_Layer = random.random() * 3
        if (select_Layer <= 1):
            # 细粒
            # for i in range(0, 3000):
            x = random.randint(3, 397)
            y = random.randint(160, 163)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("gold")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 2 and select_Layer > 1):
            # 中粒
            # for i in range(0, 700):
            x = random.randint(3, 397)
            y = random.randint(160, 162)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("peru")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状
        if (select_Layer <= 3 and select_Layer > 2):
            # 粗粒
            # for i in range(0, 900):
            x = random.randint(3, 397)
            y = random.randint(160, 162)
            depth = random.uniform(4, 6)
            r = random.random() * depth  # 随机生成的半径

            turtle.penup()
            turtle.goto(x, y)
            turtle.begin_fill()  # 开始填充
            turtle.color("saddlebrown")  # 填充
            turtle.circle(r)
            turtle.end_fill()  # 填充结束
            turtle.hideturtle()  # 隐藏画笔形状

    #垫层边界
    # for m in range(0, 300):
    #     select_Layer = random.random() * 2
    #     if (select_Layer <= 1):
    #         x = random.randint(3, 397)
    #         y = random.randint(160, 162)
    #         depth = random.uniform(0.5, 1)
    #         r = random.random() * depth
    #
    #         turtle.speed(0)
    #         turtle.penup()
    #         turtle.goto(x, y)
    #         turtle.begin_fill()  # 开始填充
    #         turtle.color("slateblue")  # 填充
    #         turtle.circle(r)
    #         turtle.end_fill()  # 填充结束
    #         turtle.hideturtle()  # 隐藏画笔形状
    #     if (select_Layer <= 2 and select_Layer > 1):
    #         x = random.randint(3, 397)
    #         y = random.randint(160, 162)
    #         depth = random.uniform(0.5, 1)
    #         r = random.random() * depth
    #
    #         turtle.speed(0)
    #         turtle.penup()
    #         turtle.goto(x, y)
    #         turtle.begin_fill()  # 开始填充
    #         turtle.color("navy")  # 填充
    #         turtle.circle(r)
    #         turtle.end_fill()  # 填充结束
    #         turtle.hideturtle()  # 隐藏画笔形状

#随机画一些石头
def drawStone():
    count=random.randint(3, 10)
    for m in range(0,count):
        x = random.randint(3, 397)
        y = random.randint(0, 160)
        depth = random.randint(5, 10)

        turtle.speed(0)
        turtle.penup()
        turtle.goto(x, y)  # 定义x,y坐标
        turtle.pendown()  # 落笔


        turtle.begin_fill()  # 开始填充
        turtle.color('darkred')  # 定义颜色
        turtle.circle(depth)
        turtle.end_fill()  # 填充结束
        turtle.hideturtle()  # 隐藏画笔形状

#生成D_Scan的标签
def opTarget_D_Txt(path, count):
    for j in range(0,600):
        D_Model=list()
        for mm in range(0,20):
            model_Path = path + str(mm) + ".png"
            # B_ScanPath = path + str(mm) + "_B.png"
            # save_Path = path.split("/")[-4] + "_" + path.split("/")[-3] + "_" + path.split("/")[-2]

            img = cv2.imread(model_Path, 1)
            img = np.array(img)
            temp = img[:,j]
            D_Model.append(temp)
        D_Model = np.array(D_Model)
        D_Model=np.rot90(D_Model,-1)
        D_Model=cv2.flip(D_Model,1)
        if (not (os.path.exists(path + "D/"))):
            os.mkdir(path + "D/")
        D_Model = cv2.resize(D_Model, (100, img.shape[0]), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(path + "D/" + str(j) + ".jpg", D_Model)

    for j in range(0, 600):
        D_Model = list()
        for mm in range(0, 20):
            model_Path = path + str(mm) + "_B.png"
            # B_ScanPath = path + str(mm) + "_B.png"
            # save_Path = path.split("/")[-4] + "_" + path.split("/")[-3] + "_" + path.split("/")[-2]

            img = cv2.imread(model_Path, 1)
            img = np.array(img)
            img_B = img[:340, :]
            img_B = cv2.resize(img_B, (600, 200), interpolation=cv2.INTER_CUBIC)
            img_B = np.array(img_B)
            temp = img_B[:, j]
            D_Model.append(temp)
        D_Model = np.array(D_Model)
        D_Model = np.rot90(D_Model, -1)
        D_Model = cv2.flip(D_Model, 1)
        if (not (os.path.exists(path + "D_Scan/"))):
            os.mkdir(path + "D_Scan/")
        D_Model = cv2.resize(D_Model, (100, img_B.shape[0]), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(path + "D_Scan/" + str(j) + ".jpg", D_Model)


    for q in range(0, 600):
        model_Path=path + "D/" + str(q) + ".jpg"
        img_DM=cv2.imread(model_Path)
        # img_DM=np.array(img_DM)
        img = np.array(img_DM)
        x_Start = 999
        x_End = -1
        y_Start = 999
        y_End = -1

        classID = 0
        # 寻找病害
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0):
                    if (j < x_Start):
                        x_Start = j
                    if (j > x_End):
                        x_End = j
                    if (i < y_Start):
                        y_Start = i
                    if (i > y_End):
                        y_End = i
                    classID = 0  # 1

        # # 说明没有找到病害，随机生成一个区域，标注为“正常”类别
        # if (x_Start == 999 and x_End == -1 and y_Start == 999 and y_End == -1):
        #     x_Start = random.randint(10, 400)
        #     x_Len = random.randint(60, 200)
        #     x_End = x_Start + x_Len
        #
        #     y_Start = random.randint(0, 80) + 20
        #     y_Len = random.randint(40, 99)
        #     y_End = y_Start + y_Len + 20

        # 说明该图片中存在图片,适当放大范围
        if (not (x_Start == 999 and x_End == -1 and y_Start == 999 and y_End == -1)):
            y_Start = y_Start + 5
            y_End = y_End + 5

            x_Len = x_End - x_Start
            x_Len = x_Len * 1.5
            x_Pos = (int)((x_Start + x_End) / 2)
            x_Start = x_Pos - (int)(x_Len / 2)
            x_End = x_Pos + (int)(x_Len / 2)

            y_Len = y_End - y_Start
            y_Len = y_Len * 1.8
            y_Pos = (int)((y_Start + y_End) / 2)
            y_Start = y_Pos - (int)(y_Len / 2)
            y_End = y_Pos + (int)(y_Len / 2)

            if (x_Start < 0):
                x_Start = 0
            if (x_End > 99):
                x_End = 99
            if (y_Start < 0):
                y_Start = 0
            if (y_End > 179):
                y_End = 179

            scan_Path = path + "D_Scan/" + str(q) + ".jpg"
            img_DScan = cv2.imread(scan_Path)
            # cv2.rectangle(img_DScan, (x_Start, y_Start), (x_End, y_End), (255, 0, 0), 1)
            # cv2.imshow("a",img_DScan)
            # cv2.imshow("b", img_DM)
            # cv2.waitKey(0)
            second_Path = path.split("/")[-4] + "_" + path.split("/")[-3] + "_" + path.split("/")[-2] + "_"
            if (count <= 40):
                f1 = open(
                    r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/train_D.txt",
                    "a")
                save_Path=r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/JPEGImagesTrain_D/"
                if (not (os.path.exists(save_Path))):
                    os.mkdir(save_Path)

                cv2.imwrite(save_Path+second_Path+str(q)+".jpg", img_DScan)
            else:
                f1 = open(
                    r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/test_D.txt",
                    "a")
                save_Path = r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/JPEGImagesTest_D/"
                if (not (os.path.exists(save_Path))):
                    os.mkdir(save_Path)
                cv2.imwrite(save_Path+second_Path + str(q)+".jpg", img_DScan)
            content_Input = save_Path +second_Path+ str(q)+".jpg" + " " + ",".join(
                [str(x_Start), str(y_Start), str(x_End), str(y_End), str(classID)])
            content_Input = content_Input + "\n"
            f1.write(content_Input)
            f1.close()
def opXML():
   #for qq in ["train","test"]:
   # for qq in ["train_C","test_C"]:
   for qq in ["train_D", "test_D"]:
       f1 = open(r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/"+qq+".txt",
                 "r")
       fileContent = f1.readlines()
       for m in fileContent:
           m.strip()
           img_Path = m.split(" ")[0]
           img = cv2.imread(img_Path, 0)
           img = np.array(img)
           height = img.shape[0]
           width = img.shape[1]
           depth = 1
           if (m[-2] == '0'):
               className = "Cavity"
           # else:
           #     className='Cavity'
           sizeInfor = m[:-1].split(" ")[1].split(",")
           xmin = sizeInfor[0]
           ymin = sizeInfor[1]
           xmax = sizeInfor[2]
           ymax = sizeInfor[3]
           # print(className)
           inputXML = "<annotation>\n" \
                      + "<size>\n" \
                      + "<width>" + str(width) + "</width>\n" \
                      + "<height>" + str(height) + "</height>\n" \
                      + "<depth>" + str(1) + "</depth>\n" \
                      + "</size>\n" \
                      + "<segmented>0</segmented>\n<difficult>0</difficult>\n" \
                      + "<object>\n" \
                      + "<name>" + className + "</name>\n" \
                      + "<pose>Unspecified</pose>\n" \
                      + "<truncated>0</truncated>\n" \
                      + "<difficult>0</difficult>\n" \
                      + "<bndbox>\n" \
                      + "<xmin>" + xmin + "</xmin>\n" \
                      + "<ymin>" + ymin + "</ymin>\n" \
                      + "<xmax>" + xmax + "</xmax>\n" \
                      + "<ymax>" + ymax + "</ymax>\n" \
                      + "</bndbox>\n" \
                      + "</object>\n</annotation>"
           if(qq=='train_D'):
               path=r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/AnnotationTrain_D/"
               if (not (os.path.exists(path))):
                   os.mkdir(path)

               XMLPath = path+ \
                         img_Path.split("/")[-1][:-4] + ".xml"
           else:
               path = r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg/AnnotationTest_D/"
               if (not (os.path.exists(path))):
                   os.mkdir(path)
               XMLPath = path + \
                         img_Path.split("/")[-1][:-4] + ".xml"
           fXML = open(XMLPath, "w")
           fXML.write(inputXML)
           fXML.close()

#生成C_Scan图像
def opCScanPic():
    path=r"E:\PycharmProject\YOLOv4-pytorch-master\realData_Pre/"
    disDir=os.listdir(path)
    for i in disDir[14:]:
        disDirNumAll=os.listdir(path+i)
        print("********************************************************************")
        print(i)
        savePath=r"E:\PycharmProject\YOLOv4-pytorch-master\realData_C/"+str(i)+"/"
        if (not (os.path.exists(savePath))):
            os.mkdir(savePath)

        up_Pos = int(input("请输入up="))
        low_Pos = int(input("请输入low="))
        for j in disDirNumAll:
            imagePath=(path + i + "/"+j)
            # print(path + i + "/"+j)
            img=cv2.imread(imagePath)
            img=np.array(img)
            img=img[up_Pos:low_Pos,:]
            cv2.imshow("a",img)
            cv2.waitKey(0)
            cv2.imwrite(savePath+j.split(".")[0]+".jpg",img)
            print(savePath+j.split(".")[0]+".jpg")

def opDScanPic():
    path = r"E:\PycharmProject\YOLOv4-pytorch-master\realData_Pre/"
    disDir = os.listdir(path)
    for i in disDir[4:]:
        disDirNumAll = os.listdir(path + i)
        print("********************************************************************")
        print(i)
        savePath = r"E:\PycharmProject\YOLOv4-pytorch-master\realData_D/"
        if (not (os.path.exists(savePath))):
            os.mkdir(savePath)
        savePath=r"E:\PycharmProject\YOLOv4-pytorch-master\realData_D/" + str(i) + "/"
        if (not (os.path.exists(savePath))):
            os.mkdir(savePath)
        left_Pos = int(input("请输入left="))
        right_Pos = int(input("请输入right="))
        for j in disDirNumAll:
            imagePath=(path + i + "/"+j)
            # print(path + i + "/"+j)
            img=cv2.imread(imagePath)
            img=np.array(img)
            img=img[:,left_Pos:right_Pos]
            cv2.imshow("a",img)
            cv2.waitKey(0)
            cv2.imwrite(savePath+j.split(".")[0]+".jpg",img)
            print(savePath+j.split(".")[0]+".jpg")



def drawLoss_mAP():
    lossPath = r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg\train_LOSSReal.txt"
    lossPath1 = r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg\train_LOSSRealPre.txt"

    mAPPath=r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg\test_mAPRealD.txt"
    mAPPathpre=r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg\test_mAPRealPreD.txt"

    floss = open(mAPPath,"r")
    fileContent = floss.readlines()
    lossValue = np.zeros(100)
    for m in fileContent:
        m.strip()
        # lossValue.append((float)(m.split(";")[0].split("(")[-1].split(")")[0]))
        print((float)(m.split(";")[0].split("(")[-1].split(")")[0]))
        tempValue=(float)(m.split(";")[0].split("(")[-1].split(")")[0])
        index=(int)(m.split(";")[1])
        lossValue[index]=tempValue+lossValue[index]
    for i in range(0, 100):
        lossValue[i]=lossValue[i]#/415  #566  915   1885

    floss1 = open(mAPPathpre, "r")
    fileContent1 = floss1.readlines()
    lossValue1 = np.zeros(100)
    for m in fileContent1:
        m.strip()
        # lossValue.append((float)(m.split(";")[0].split("(")[-1].split(")")[0]))
        print((float)(m.split(";")[0].split("(")[-1].split(")")[0]))
        tempValue = (float)(m.split(";")[0].split("(")[-1].split(")")[0])
        index = (int)(m.split(";")[1])
        lossValue1[index-50] = tempValue  +lossValue1[index-50]
    for i in range(0, 100):
        lossValue1[i] = lossValue1[i]#/415  # 566  915   1885     pre 109 397 415

    # lossPathOut = r"E:\PycharmProject\YOLOv4-pytorch-master\YOLOv4-pytorch-master\data\RadarData\BTrainImg\train_LOSSRealCOut.txt"
    # fout = open(lossPathOut, "w")
    # for m in lossValue:
    #     fout.writelines(str(m)+"\n")
    # fout.close()

    epochValue=list()
    for i in range(0,100):
        epochValue.append(i)
    plt.figure(figsize=(15,10))  #8 5   10 10
    # plt.rcParams['axes.facecolor'] = 'grey'
    # plt.rcParams['savefig.facecolor'] = 'grey'
    # plt.xlim(0)
    # plt.ylim(0,0.8)


    plt.title("Testing mAP_C_Transfer",fontsize=35)
    plt.xlabel('Epoch', fontsize=30)
    plt.ylabel('mAP', fontsize=30)  #mAP
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.ylim(0,0.5)
    plt.rcParams.update({'font.size': 25})
    plt.plot(epochValue,lossValue,label='Without pre_training',color='g',marker=".",linewidth=3,markersize=7)
    plt.plot(epochValue, lossValue1,label='After pre_training',marker='.', linewidth=3, markersize=7)
    plt.legend(loc=2)
    plt.show()
    print(lossValue)

    #      #4F4F4F       #CD4F39


    # fig, ax = plt.subplots(1, 1,figsize=(6, 4))
    # ax.plot(epochValue,lossValue,label='Without pre_training',color='#4F4F4F',marker=".",linewidth=3,markersize=7)
    # ax.plot(epochValue, lossValue1,label='After pre_training',color='#CD4F39',marker=".", linewidth=3, markersize=7)
    # ax.legend(loc=1)
    # ax.set_xlabel('Epoch')
    # ax.set_ylabel('total_loss')
    # axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
    #                bbox_to_anchor=(0.3, 0.1, 1, 1),
    #                bbox_transform=ax.transAxes)
    # axins.plot(epochValue[1:], lossValue[1:], label='Without pre_training', color='#4F4F4F', marker=".", linewidth=3, markersize=7)
    # axins.plot(epochValue[1:], lossValue1[1:],label='After pre_training',color='#CD4F39',marker=".", linewidth=3, markersize=7)







if __name__ == '__main__':
    #2个像素==1cm
    #道路深度2m==200cm=400像素
    # im = Image.open("./circle.eps")
    # box = (365, 100, 660, 300)
    #
    # region = im.crop(box)
    # region.save('./crop.png')
    # # cv2.imwrite("./circle.png",im)
    # # im.save("./circle.png")
    # im = cv2.imread('./crop.png', 1)
    # im = cv2.resize(im, (600, 180), interpolation=cv2.INTER_NEAREST)
    # cv2.imwrite('./crop.png', im)

    # top_Path = r"E:\PycharmProject\YOLOv4-pytorch-master\disData_Pre/"
    # count = -1
    # for m in os.listdir(top_Path):
    #     second_Path = top_Path + m + "/"
    #     for n in os.listdir(second_Path):
    #         third_Path = second_Path + n + "/"
    #         for q in os.listdir(third_Path):
    #             pic_Path = third_Path + q + "/"
    #             count += 1
    #             print(pic_Path)
    #             opTarget_D_Txt(pic_Path, count)
    # opXML()
    # opCScanPic()
    # opDScanPic()
    drawLoss_mAP()


    # # os.popen('python -m tools.convert_png2h5 E://PycharmProject//test//crop.png 0.01 0.01 0.01')
    # turtle.screensize(400, 400)
    # for mmm in range(11,40):
    #     print(mmm)
    #     path="D:/lalala_Road_Data/"+str(mmm)
    #     if (not (os.path.exists(path))):
    #         os.mkdir(path)
    #     for nn in range(0,20):
    #
    #         turtle.hideturtle()  # 隐藏画笔形状
    #
    #         drawFirstLayer()
    #         drawSecondLayer()
    #         drawThirdLayer()
    #         drawBasicLayer()
    #         drawStone()
    #
    #         ts = turtle.getscreen()
    #         ts.getcanvas().postscript(file=r"./circle.eps")
    #         turtle.clearscreen()
    #         im = Image.open("./circle.eps")
    #         box = (365, 102, 660, 300)
    #
    #         region = im.crop(box)
    #         region.save('./crop.png')
    #         # cv2.imwrite("./circle.png",im)
    #         # im.save("./circle.png")
    #         im = cv2.imread('./crop.png', 1)
    #         im = cv2.resize(im, (600, 180), interpolation=cv2.INTER_NEAREST)
    #         cv2.imwrite(path + "/"+str(nn)+".png", im)
    # #         turtle.bye()

    
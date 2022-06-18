"""
python运行gprmax
读取.in文件
运行api函数模拟
"""
import sys
sys.path.append(r"D:\gprMax\gprMax\gprMax")
sys.path.append(r"D:\anaconda\envs\gprmax\lib\site-packages")
import os
import numpy as np
import matplotlib.pyplot as plt
from gprMax.gprMax import api
from tools.outputfiles_merge import get_output_data, merge_files
from tools.plot_Bscan import mpl_plot
import pycuda.driver as cuda
import numpy
import h5py
import cv2

#m为测线条数
def simulateDisease(m):
    # 文件路径+文件名
    dmax = r".\SimulateTDModel"  # 项目目录
    filename = os.path.join(dmax, 'TDModel.in')
    # 正演  n：仿真次数（A扫描次数）->B扫描
    api(filename, n=160, geometry_only=False)  # geometry_only：仅几何图形
    # api(filename, n=20, geometry_only=False,gpu={0})  #geometry_only：仅几何图形;并使用GPU进行加速
    merge_files(r".\SimulateTDModel\TDModel", removefiles=True)

    # 获取回波数据
    # A B扫描时out文件名不一样
    filename = os.path.join(r".\SimulateTDModel\TDModel_merged.out")
    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename, rxnumber, rxcomponent)

    # 保存回波数据
    np.savetxt("TDDisease.txt", outputdata, delimiter=';')

    # plt.ylabel('Time [ns]')
    plt.imshow(outputdata, extent=[0, outputdata.shape[1], outputdata.shape[0], 0], interpolation='bicubic',cmap='gray')

    ## B扫描绘图
    # plt = mpl_plot(filename,outputdata, dt*1e9, rxnumber, rxcomponent)
    plt.axis('off')
    plt.savefig("./SimulateTDModel/Bpic/lalala-simulate"+str(m)+".png",bbox_inches="tight", pad_inches=0.0)
    plt.show()
    # imag=cv2.imread("./SimulateTDModel/Bpic/lalala-simulate"+str(m)+".png",0)
    # imag=imag[100:,:]*5
    # cv2.imshow("la",imag)
    # cv2.waitKey(0)


#数组放大
def gainData():
    gain_Line=list()

    path="./TDDisease.txt"
    f=open(path)
    lines = f.readlines()

    for i in range(0,len(lines)-300):
        gain_Line.append((i*0.008)+1)


    B_Pic=list()
    for count in range(0, len(lines)-300):
        temp = list()
        for i in range(0, len(lines[count].split(";"))):
            temp.append((float)(lines[count].split(";")[i])*3+128)#*gain_Line[count]+128)
        B_Pic.append(temp)
    img=np.array(B_Pic)
    img=cv2.resize(img,(100,200),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("./gain.png",img)
    # img=cv2.imread("./gain.png",0)
    # plt.imshow(img, interpolation='bicubic',extent=[0, img.shape[1]*5, img.shape[0], 0],
    #            cmap='gray')
    # plt.show()


#循环扫描
def multiScan(path):
    #disModel\box\50-80\0/
    for m in range(0,20):
        f1 = open(r"E:\PycharmProject\test/SimulateTDModel/TDModel.in", "r")
        fileContent = f1.readlines()
        for i in range(0, np.array(fileContent).shape[0]):
            if ("geometry_objects_read" in fileContent[i]):
                insert_Line="#geometry_objects_read: 0 0 0 "+path+str(m)+".h5 E:/PycharmProject/test/material.txt\n"
                fileContent[i]=insert_Line
                print(fileContent[i])
        f1.close()
        f1 = open(r"E:\PycharmProject\test/SimulateTDModel/TDModel.in", "w")
        f1.writelines(fileContent)
        f1.close()


        # 文件路径+文件名
        dmax = r"E:\PycharmProject\test\SimulateTDModel"  # 项目目录
        filename = os.path.join(dmax, 'TDModel.in')
        # 正演  n：仿真次数（A扫描次数）->B扫描
        api(filename, n=580, geometry_only=False,gpu={0})  # geometry_only：仅几何图形
        # api(filename, n=20, geometry_only=False,gpu={0})  #geometry_only：仅几何图形;并使用GPU进行加速
        merge_files(r"E:\PycharmProject\test\SimulateTDModel\TDModel", removefiles=True)

        # 获取回波数据
        # A B扫描时out文件名不一样
        filename = os.path.join(r"E:\PycharmProject\test\SimulateTDModel\TDModel_merged.out")
        rxnumber = 1
        rxcomponent = 'Ez'
        outputdata, dt = get_output_data(filename, rxnumber, rxcomponent)

        # 保存回波数据
        np.savetxt(path+str(m)+".txt", outputdata, delimiter=';')

        # plt.ylabel('Time [ns]')
        plt.imshow(outputdata, extent=[0, outputdata.shape[1], outputdata.shape[0], 0], interpolation='bicubic',aspect='auto',
                   cmap='gray')

        ## B扫描绘图
        # plt = mpl_plot(filename,outputdata, dt*1e9, rxnumber, rxcomponent)
        plt.axis('off')
        # plt.savefig("./SimulateTDModel/Bpic/lalala-simulate" + str(m) + ".png", bbox_inches="tight", pad_inches=0.0)
        plt.show()

        gain_Line = list()

        # path = "./TDDisease.txt"
        f_Txt = open(path+str(m)+".txt")
        lines = f_Txt.readlines()

        for i in range(0, len(lines)):
            gain_Line.append((i * 0.008) + 1)

        B_Pic = list()
        for count in range(0, len(lines)):
            temp = list()
            for i in range(0, len(lines[count].split(";"))):
                temp.append((float)(lines[count].split(";")[i])*3 + 128)  # *gain_Line[count]+128)
            B_Pic.append(temp)
        img = np.array(B_Pic)
        img = cv2.resize(img, (580, 400), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(path+str(m)+"_B.png", img)
        f_Txt.close()

        # imag = cv2.imread("./SimulateTDModel/Bpic/lalala-simulate" + str(m) + ".png", 0)
        # imag = imag[100:, :] * 5
        # cv2.imshow("la", imag)
        # cv2.waitKey(0)


def creatHDF5(path):
    for mm in range(0,20):
        dx_dy_dz = (0.01, 0.01, 0.01)
        # print(path+"/"+str(mm)+".png")
        temp_img = cv2.imread(path+"/"+str(mm)+".png", 1)
        temp_img_RGB = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
        img = np.rot90(temp_img_RGB, k=3)
        hdf5file = path+"/"+str(mm)+".h5"
        data = np.ones((img.shape[0], img.shape[1], 1), dtype=np.int16) * -1

        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if (img[i][j][0] == 255 and img[i][j][1] == 0 and img[i][j][2] == 0):  # 红色
                    data[i][j] = 0
                if (img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 0):  # 黄色
                    data[i][j] = 1
                if (img[i][j][0] == 240 and img[i][j][1] == 128 and img[i][j][2] == 128):  # 粉色
                    data[i][j] = 2
                if (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 255):  # 蓝色
                    data[i][j] = 3
                if (img[i][j][0] == 0 and img[i][j][1] == 128 and img[i][j][2] == 0):  # 绿色
                    data[i][j] = 4
                if (img[i][j][0] == 128 and img[i][j][1] == 128 and img[i][j][2] == 128):  # 灰色
                    data[i][j] = 5
                if (img[i][j][0] == 106 and img[i][j][1] == 90 and img[i][j][2] == 205):  # 浅紫色
                    data[i][j] = 6
                if (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 128):  # 深紫色
                    data[i][j] = 7
                if (img[i][j][0] == 255 and img[i][j][1] == 215 and img[i][j][2] == 0):  # 土1
                    data[i][j] = 8
                if (img[i][j][0] == 205 and img[i][j][1] == 133 and img[i][j][2] == 63):  # 土2
                    data[i][j] = 9
                if (img[i][j][0] == 139 and img[i][j][1] == 69 and img[i][j][2] == 19):  # 土3
                    data[i][j] = 10
                if (img[i][j][0] == 139 and img[i][j][1] == 0 and img[i][j][2] == 0):  # 石头
                    data[i][j] = 11
                if (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0):  # 空洞
                    data[i][j] = 12
                if (img[i][j][0] == 0 and img[i][j][1] == 255 and img[i][j][2] == 0):  #井盖
                    data[i][j] = 13

        with h5py.File(hdf5file, 'w') as fout:
            fout.attrs['dx_dy_dz'] = dx_dy_dz
            fout.create_dataset('data', data=data)
    print("Finish 1")

if __name__ == '__main__':
    # for m in range(0,3):
    # imag = cv2.imread("./SimulateTDModel/Bpic/lalala-simulate1.png", 0)
    # imag = imag[100:, 50:]
    # imag=np.array(imag)
    # m=np.mean(imag)
    # for i in range(0,imag.shape[0]):
    #     for j in range(0,imag.shape[1]):
    #         if(imag[i][j]>m):
    #             imag[i][j]=imag[i][j]*1.5
    #         if (imag[i][j] < m):
    #             imag[i][j] = imag[i][j] * 0.5
    # cv2.imshow("la", imag)
    # cv2.waitKey(0)


    #循环扫描
    path=r"E:\PycharmProject\test\SimulateTDModel\disModel/"
    top_Path=os.listdir(path)
    for i in top_Path:
        second_Path=os.listdir(path+i+"/")
        for j in second_Path:
            third_Path=os.listdir(path+i+"/"+j+"/")
            for m in third_Path:
                dirPath=(path+i+"/"+j+"/"+m+"/")
                multiScan(dirPath)

    # multiScan(r"D:\disModel\box\50-80\0/")

    #"E:\PycharmProject\test\SimulateTDModel\disModel\box\50-80\0/"

    #单幅图像扫描
    # simulateDisease(1)
    # gainData()

    #生成HDF5文件
    # dirPath=r"E:\PycharmProject\test\SimulateTDModel\disModel/"
    # top_Path=os.listdir(dirPath)
    # for i in top_Path:
    #     shape_Path=os.listdir(dirPath+i+"/")
    #     for j in shape_Path:
    #         for m in range(0,20):
    #             print(dirPath+i+"/"+j+"/"+str(m)+"/")
    #             creatHDF5(dirPath+i+"/"+j+"/"+str(m)+"/")
        # print("1")



    # print(1)
    # f1=open(r"E:\PycharmProject\test\TDDisease.txt","r")
    # fileContent = f1.readlines()
    # image=list()
    # for i in range(0, np.array(fileContent).shape[0]):
    #     temp=list()
    #     for m in fileContent[i].split(";"):
    #         temp.append((float)(m))
    #     image.append(temp)
    # image=np.array(image)
    # plt.imshow(image, extent=[0, image.shape[1], image.shape[0], 0], interpolation='bicubic',
    #            aspect='auto', cmap='gray')
    #
    # ## B扫描绘图
    # # plt = mpl_plot(filename,outputdata, dt*1e9, rxnumber, rxcomponent)
    #
    # plt.savefig("./SimulateTDModel/Bpic/lalala-simulate0.png")
    # plt.show()
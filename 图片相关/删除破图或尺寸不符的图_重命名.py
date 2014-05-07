# -*- coding: utf-8 -*-

import math,time,os,re,imghdr,shutil
import numpy as np
from PIL import Image,ImageEnhance
start = time.clock()

path_origin = 'd:\\张玉龙\\Python\\Photos'
path_target = 'd:\\张玉龙\\Python\\Photos_Drop'

#迭代出原始路径下的目录
total = os.walk(path_origin)

for rootDir,pathList,fileList in total:
    #目标路径创建目录
    if os.path.exists(rootDir.replace(path_origin,path_target)):
        pass
    else:
        os.makedirs(rootDir.replace(path_origin,path_target))
    #迭代遍历目录下的文件
    for file in fileList: 
        #if os.path.isfile(os.path.join(rootDir.replace(path_origin,path_target),file))==False:
        im = os.path.join(rootDir,file)
        ##文件重命名，去掉’#‘和'%'
        if re.findall('%',im):
            os.rename(im,im.replace('%',''))
        elif re.findall('#',im):
            os.rename(im,im.replace('#',''))
        elif re.findall(' ',im):
            os.rename(im,im.replace(' ','a'))
        elif re.findall('.jpg.jpg',im):
            os.rename(im,im.replace('.jpg.jpg','.jpg').replace('.jpg.jpg','.jpg'))
        else:
            pass

        ##移动格式不正确的图片
        '''
        if imghdr.what(im)=='jpeg' or imghdr.what(im)=='png' or imghdr.what(im)=='bmp' or imghdr.what(im)=='gif':
            pass
        elif imghdr.what(im)==None:
            new  = os.path.join(rootDir.replace(path_origin,path_target),file)
            shutil.move(im,new)
        else:
            print(im)
        '''

        ##移动不符合尺寸的
        '''
        size = os.path.getsize(im)
        try:
            if size<25600:
                new  = os.path.join(rootDir.replace(path_origin,path_target),file)
                shutil.move(im,new)
                print(im)
                print(size)
            else:
                pass
        except:
            print(im)
        '''
        
end = time.clock()
print(end-start)



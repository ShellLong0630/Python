import math,time,os,re,imghdr,shutil
import numpy as np
from PIL import Image,ImageEnhance

path_origin = 'D:/张玉龙/Python/BaiduAlbum_20140415'
path_target = 'D:/张玉龙/Python/BaiduAlbum_20140415_Delete'

#迭代出原始路径下的目录
total = os.walk(path_origin)
#print(total)
for rootDir,pathList,fileList in total:
    if os.path.exists(rootDir.replace(path_origin,path_target)):
        pass
    else:
        os.makedirs(rootDir.replace(path_origin,path_target))
    #迭代遍历目录下的文件
    for file in fileList:
        im  = Image.open(os.path.join(rootDir,file))#打开图片
        box = im.getbbox()
        size = box[2]*box[3]
        if size<200000:#判断图片大小
            try:
                shutil.move(os.path.join(rootDir,file).replace('\\','/'),os.path.join(rootDir.replace(path_origin,path_target).replace('\\','/'),file))
            except:
                print(os.path.join(rootDir,file))
##                os.remove(os.path.join(rootDir,file))
        else:
            pass
    

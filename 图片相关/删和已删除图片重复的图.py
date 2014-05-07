# -*- coding: utf-8 -*-

import math,time,os,re,imghdr,shutil
import numpy as np
from PIL import Image,ImageEnhance
start = time.clock()

path_origin = 'd:\\张玉龙\\Python\\Photos'
path_target = 'd:\\张玉龙\\Python\\Photos_Drop'

#迭代出原始路径下的目录
total = os.walk(path_target)
drop_dic = {}
for rootDir,pathList,fileList in total:
    #迭代遍历目录下的文件
    for file in fileList: 
        file = re.sub('.jpg.jpg$','.jpg',file)
        file = re.sub('.jpg.jpg$','.jpg',file)
        if file not in drop_dic.keys():
            drop_dic[file]=1
        else:
            drop_dic[file]+=1
            
total1 = os.walk(path_origin)
for rootDir,pathList,fileList in total1:
    #迭代遍历目录下的文件
    for file in fileList: 
        try:
            if file in drop_dic.keys():
                if drop_dic[file]>1:
                    im   = os.path.join(rootDir,file)
                    new  = os.path.join(rootDir.replace(path_origin,path_target),file)
                    shutil.move(im,new)
            else:
                pass
        except:
            print(os.path.join(rootDir,file))
        
end = time.clock()
print(end-start)



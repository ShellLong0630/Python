import urllib.request,time,re,os
##url = "http://a4.att.hudong.com/75/93/01300000397019128202931308688.jpg"
##path = 'd:\\张玉龙\\Python\\%s_%s'% (url.split('/')[-2],url.split('/')[-1])
##data = urllib.request.urlopen(url).read()  
##f = open(path,"wb")  
##f.write(data)  
##f.close() 
file = 'D:\\张玉龙\\Python\\提交\\20140414_picUrl2.txt'
f1   = open(file,'r',encoding='utf-8')
for s in f1:   
    start = time.clock()
    b = re.split(',|"',s)
    localId = b[0]
    url = b[2]
    #print(url)
    Dir = 'd:\\张玉龙\\Python\\Pic_20140414\\'
    if os.path.exists(Dir+localId):
        pass
    else:
        os.makedirs(Dir+localId)
    path = Dir+localId+'\\%s_%s'% (url.split('/')[-2],url.split('/')[-1])
    #print(path)
    say = '%s ~ok~'% localId
    if os.path.isfile(path)==True:
        pass
    else:
        try:
            print(localId)
            data = urllib.request.urlopen(url).read()  
            f = open(path,"wb")  
            f.write(data)  
            f.close()       
        except:
            say = '%s failed!!'% localId
    end = time.clock()
    print(say,end-start)
f1.close()

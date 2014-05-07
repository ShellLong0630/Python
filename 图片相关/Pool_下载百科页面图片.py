import httplib2,urllib.request,re,os,time
from multiprocessing import Pool
import multiprocessing
b = []  
def getimg(m):
    start = time.clock()
    s = m
    b = re.split(',|"',s)
    localId = b[0]
    url = b[2]
    Dir = 'd:\\张玉龙\\Python\\BaiduAlbum_20140415\\'
    path = Dir+localId+'\\%s'% (url.split('/')[-1])
    say = '%s ~ok~'% localId
    if os.path.isfile(path)==True:
        pass
    else:
        try:
            data = urllib.request.urlopen(url).read()
            if os.path.exists(Dir+localId):
                pass
            else:
                os.makedirs(Dir+localId)
            f = open(path,"wb")  
            f.write(data)  
            f.close()
        except:
            say = '%s failed!!'% localId
    end = time.clock()
    print(say,end-start)
def main():
    file = 'D:\\张玉龙\\Python\\20140415_picUrl_baidu.txt'
    f1   = open(file,'r',encoding='utf-8')
    proclist = []
    pool     = Pool(processes=50)
    for s in f1:        
        result = pool.apply_async(getimg,(s,))        
    pool.close()
    pool.join()
    f1.close()
    
if __name__ == '__main__':
    print('start')
    main()
    os.system('pause')

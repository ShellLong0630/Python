import httplib2
import urllib.request
import re
import os,time,random
from multiprocessing import Pool
import multiprocessing
import json,mysql.connector
proxy=[]
bad=[]
ipfile=open('D:\\张玉龙\\Python\\代理IP\\trip_Ip_1403190404.txt','r',encoding='utf-8')
badIp1=open('D:\\张玉龙\\Python\\代理IP\\badIp.txt','r',encoding='utf-8')
#将badIp从ip列表中剔除
for ip in ipfile:
    proxy.append(ip.replace('\n',''))
for badip in badIp1:
    bad.append(badip.replace('\n',''))
    if re.findall(badip.replace('\n',''),str(proxy)):
        proxy.remove(badip.replace('\n',''))
badIp1.close()
def worker(j):
    j = j

    sourceId = re.split('_|-',j['sourceId'])[1]
    timebreak=0
    count    =0
    string   =''
    content  =''
    landmarks=[]
    #如果请求失败，则换个ip重新请求，3次机会后放弃
    while timebreak<10:
        timebreak+=1
        if os.path.isfile('D:\\张玉龙\\Python\\landmarks\\'+sourceId+'.txt')== False:
            #随机取一个代理ip                
            rando=random.randint(0,len(proxy)-1)
            proxyIp=proxy[rando]
            proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
            #使用代理ip请求
            opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            url='http://www.daodao.com/Attractions-%s-Activities-c47-%s_%s.html'% (sourceId,j['city'],j['provice'])
            headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
            req     =urllib.request.Request(url,None,headers)
            try:
                content=urllib.request.urlopen(req,timeout=10).read().decode('utf-8')
                break
            except:
                pass                        
        else:
            break
    #读到content后，再读翻页    
    if re.findall('地标\([\d]+\)',content):
        count    = int(re.findall('地标\(([\d]+)\)',content)[0])
        if count <16:
            landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)[0:count]
            for m in landmark:
                landmarks.append(m)
        else:
            landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)
            for m in landmark:
                landmarks.append(m)
            page     = int(re.findall('</b>/([\d]+)页</span>',content)[0])
            for t in range(page):
                if t==0:
                    pass
                else:
                    #随机取一个代理ip
                    timebreak2=0
                    while timebreak2<6:
                        timebreak2+=1
                        rando=random.randint(0,len(proxy)-1)
                        proxyIp=proxy[rando]
                        proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
                        #使用代理ip请求
                        opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
                        urllib.request.install_opener(opener)
                        url='http://www.daodao.com/Attractions-%s-Activities-c47-oa%s-%s_%s.html'% (sourceId,str(15*t),j['city'],j['provice'])
                        headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
                        req    =urllib.request.Request(url,None,headers)
                        try:
                            content=urllib.request.urlopen(req,timeout=10).read().decode('utf-8')
                            
                            landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)
                            for m in landmark:
                                landmarks.append(m)
                            if content:
                                break
                        except:
                            pass
    if landmarks:
        file2 = 'D:\\张玉龙\\Python\\landmarks\\'+sourceId+'.txt'
        f2   = open(file2,'w',encoding='utf-8')
        for k in landmarks:
            f2.write(k+'\n')                
        if len(landmarks)==count:
            string=sourceId+' is OK~'
        else:
            f2.write('part \n')
            string=sourceId+' is part'
        f2.close()    
    else:
        pass       
    if os.path.isfile('D:\\张玉龙\\Python\\landmarks\\'+sourceId+'.txt')==False:
        string=sourceId+' is failed！！！'
    print(str(string))
def main():
    file = 'D:\\张玉龙\\Python\\POIs_tripadvisor_20131210.txt'
    f   = open(file,'r',encoding='utf-8')
    dic = {}
    #badIp文件来追加存储不能返回结果的ip
    proclist=[]
    pool=Pool(processes=100)
    for s in f:
        j = json.loads(s)
        sourceId = re.split('_|-',j['sourceId'])[1]
        if sourceId not in dic.keys():
            dic[sourceId] = (j['city'],j['provice'])
            result = pool.apply_async(worker,(j,))
        else:
            pass
    pool.close()
    pool.join()
    f.close()
    ipfile.close()
if __name__ == '__main__':
    print('start')
    main()
    os.system('pause') 

       

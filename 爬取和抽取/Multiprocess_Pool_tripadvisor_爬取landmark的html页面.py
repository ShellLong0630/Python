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
    s = j
    sourceId = re.split('-Reviews',s)[0]
    timebreak=0
    count    =0
    string   =''
    content  =''
    #如果请求失败，则换个ip重新请求，10次机会后放弃
    while timebreak<10:
        timebreak+=1
        if os.path.isfile('D:\\张玉龙\\Python\\tripadvisor\\'+sourceId+'.html')== False:
            #随机取一个代理ip                
            rando=random.randint(0,len(proxy)-1)
            proxyIp=proxy[rando]
            proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
            #使用代理ip请求
            opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            url='http://www.daodao.com/Attraction_Review-%s'% (s.split('\n')[0])
            headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
            req     =urllib.request.Request(url,None,headers)
            try:
                content=urllib.request.urlopen(req,timeout=10).read().decode('utf-8')
                break
            except:
                pass                        
        else:
            break
    if content:
        file2 = 'D:\\张玉龙\\Python\\tripadvisor\\'+sourceId+'.html'
        f2   = open(file2,'w',encoding='utf-8')        
        f2.write(content)          
        f2.close()
        string=sourceId+' is ~ok~'
    else:
        pass       
    if os.path.isfile('D:\\张玉龙\\Python\\tripadvisor\\'+sourceId+'.html')==False:
        string=sourceId+' is failed！！！'
    print(str(string))
def main():
    file = 'D:\\张玉龙\\Python\\20140407_trip_landmarks.txt'
    f   = open(file,'r',encoding='utf-8')
    dic = {}
    #badIp文件来追加存储不能返回结果的ip
    proclist=[]
    pool=Pool(processes=100)
    for s in f:
        sourceId = re.split('-Reviews',s)[0]
        if sourceId not in dic.keys():
            dic[sourceId] = s
            result = pool.apply_async(worker,(s,))
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

       

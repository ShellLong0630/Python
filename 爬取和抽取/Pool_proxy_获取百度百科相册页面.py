import httplib2,urllib.request,re,os,time,random
from multiprocessing import Pool
import multiprocessing

proxy=[]
bad=[]
b=[]
ipfile=open('D:\\张玉龙\\Python\\代理IP\\BaiduBaike_Ip_140413.txt','r',encoding='utf-8')
badIp1=open('D:\\张玉龙\\Python\\代理IP\\badIp.txt','r',encoding='utf-8')
#将badIp从ip列表中剔除
for ip in ipfile:
    proxy.append(ip.replace('\n',''))
for badip in badIp1:
    bad.append(badip.replace('\n',''))
    if re.findall(badip.replace('\n',''),str(proxy)):
        proxy.remove(badip.replace('\n',''))
badIp1.close()
 
def geturl(m):
    s = m
    b = re.split(',|"',s)
    file2 = 'D:\\张玉龙\\Python\\Baidu_Album\\%s.html'% (b[0])
    file3 = 'D:\\张玉龙\\Python\\Baidu_Album\\e_%s.html'% (b[0])
    timebreak = 0    
    while timebreak<10:
        timebreak+=1
        if os.path.isfile(file2)==False and os.path.isfile(file3) == False:
            rando=random.randint(0,len(proxy)-1)
            proxyIp=proxy[rando]
            proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
            #使用代理ip请求
            opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            
            say = '%s  ~ok~'% (b[0])
            try:
                url = b[2]
                content =urllib.request.urlopen(url,timeout=10).read().decode('utf-8')                             
                if re.findall('"url":"http',content) :
                    f2 = open(file2,'w',encoding='utf-8')
                    f2.write(content)
                    f2.close()
                elif content:
                    f2 = open(file3,'w',encoding='utf-8')
                    f2.write(content)
                    f2.close()
            except:
                say = '%s error!'% (b[0])
        else:
            break
    if os.path.isfile(file2) == False and os.path.isfile(file3) == False:
        say = '%s is failed！！！'% (b[0])    
    print(say)
            
def main():
    f = open('D:\\张玉龙\\Python\\20140414_picUrl_baidu.txt','r',encoding='utf-8')
    proclist = []
    pool     = Pool(processes=100)
    for s in f:
        result = pool.apply_async(geturl,(s,))        
    pool.close()
    pool.join()
    f.close()
if __name__ == '__main__':
    print('start')
    main()
    os.system('pause')

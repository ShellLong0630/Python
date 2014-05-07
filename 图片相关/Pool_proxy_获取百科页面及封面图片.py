import httplib2,urllib.request,re,os,time,mysql.connector,random
from multiprocessing import Pool
import multiprocessing

proxy=[]
bad=[]
ipfile=open('D:\\张玉龙\\Python\\代理IP\\wikipedia_Ip_140413.txt','r',encoding='utf-8')
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
    file2 = 'D:\\张玉龙\\Python\\linkUrl_html\\w_%s.html'% (s[0])
    file3 = 'D:\\张玉龙\\Python\\linkUrl_html\\b_%s.html'% (s[0])
    file4 = 'D:\\张玉龙\\Python\\linkUrl_html\\s_%s.html'% (s[0])
    file5 = 'D:\\张玉龙\\Python\\linkUrl_html\\h_%s.html'% (s[0])
    file6 = 'D:\\张玉龙\\Python\\linkUrl_html\\e_%s.html'% (s[0])
    timebreak = 0    
    while timebreak<10:
        timebreak+=1
        if os.path.isfile(file2)==False and os.path.isfile(file3) == False and os.path.isfile(file4) == False and os.path.isfile(file5) == False and os.path.isfile(file6) == False:
            rando=random.randint(0,len(proxy)-1)
            proxyIp=proxy[rando]
            proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
            #使用代理ip请求
            opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            
            say = '%s  ~ok~'% (s[0])
            try:
                url = s[1]
                content =urllib.request.urlopen(url,timeout=10).read().decode('utf-8')                             
                if re.findall('.wikipedia.',s[1]) :
                    if re.findall('wikipedia',content) :
                        f2 = open(file2,'w',encoding='utf-8')
                        f2.write(content)
                        f2.close() 
                elif re.findall('.baidu.',s[1]) :
                    if re.findall('baidu',content) :
                        f2 = open(file3,'w',encoding='utf-8')
                        f2.write(content)
                        f2.close()
                elif re.findall('.soso.',s[1]) :
                    if re.findall('soso',content) :
                        f2 = open(file4,'w',encoding='utf-8')
                        f2.write(content)
                        f2.close()
                elif re.findall('www.baike.com',s[1]) :
                    if re.findall('www.baike.com',content) :
                        f2 = open(file5,'w',encoding='utf-8')
                        f2.write(content)
                        f2.close()
                elif content:
                    f2 = open(file6,'w',encoding='utf-8')
                    f2.write(content)
                    f2.close()
                        
            except:
                say = '%s error!'% (s[0])
        else:
            break
    if os.path.isfile(file2) == False and os.path.isfile(file3) == False and os.path.isfile(file4) == False and os.path.isfile(file5) == False and os.path.isfile(file6) == False:
        say = '%s is failed！！！'% (s[0])    
    print(say)
            
def main():
    host = '192.168.1.15'
    user = 'data'
    pwd  = 'skst'
    db   = 'wwere_v3'
    cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
    cursor = cnx.cursor()
    sql = "SELECT localId,linkUrl from landmark where linkUrl!=''"
    cursor.execute(sql)
    result = cursor.fetchall()
    proclist = []
    pool     = Pool(processes=100)
    for s in result:
        if s[1]:
            result = pool.apply_async(geturl,(s,))
        else:
            pass
    pool.close()
    pool.join()
    cnx.commit()
    cursor.close()
    cnx.close()
    
if __name__ == '__main__':
    print('start')
    main()
    os.system('pause')

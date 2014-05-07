import httplib2,urllib.request,re,os,time,mysql.connector,random
from multiprocessing import Pool
import multiprocessing

proxy=[]
bad=[]
ipfile=open('D:\\张玉龙\\Python\\代理IP\\baidu_Ip_140313.txt','r',encoding='utf-8')
badIp1=open('D:\\张玉龙\\Python\\代理IP\\badIp.txt','r',encoding='utf-8')
#将badIp从ip列表中剔除
for ip in ipfile:
    proxy.append(ip.replace('\n',''))
##for badip in badIp1:
##    bad.append(badip.replace('\n',''))
##    if re.findall(badip.replace('\n',''),str(proxy)):
##        proxy.remove(badip.replace('\n',''))
##badIp1.close()
 
def geturl(m):
    s = m
#    badIp=open('D:\\张玉龙\\Python\\代理IP\\badIp.txt','a',encoding='utf-8')
    file2 = 'D:\\张玉龙\\Python\\url_0504\\%s_%s.txt'% (s[0],s[1])
    file3 = 'D:\\张玉龙\\Python\\url_0504\\S_%s_%s.txt'% (s[0],s[1])
    timebreak = 0    
    while timebreak<5:
        timebreak+=1
        #print(timebreak)
        if os.path.isfile(file2)==False and os.path.isfile(file3) == False:
            rando=random.randint(0,len(proxy)-1)
            proxyIp=proxy[rando]
            proxy_support=urllib.request.ProxyHandler({'http':'http://'+proxyIp})
            #使用代理ip请求
            opener=urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            
            say = '%s_%s  ~ok~'% (s[0],s[1])
            string = urllib.request.quote(s[1])
            try:
                url_w = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
                content_w =urllib.request.urlopen(url_w,timeout=10).read().decode('utf-8')
                #print(content_w)
                key = re.findall('{"title":"([\S ]+) - Wikipedia, the free encyclopedia","url":"',content_w)
                url = re.findall(' - Wikipedia, the free encyclopedia","url":"([\S]+)"}',content_w)                               
                if url :
                    if str(key[0])==str(s[1]):                  
                        f2 = open(file2,'w',encoding='utf-8')
                        f2.write('%s,"%s","%s"\n'% (s[0],s[1],url[0]))
                        f2.close() 
                    else:                   
                        f2 = open(file3,'w',encoding='utf-8')
                        f2.write('%s,"%s","%s","%s"\n'% (s[0],s[1],key[0],url[0]))
                        f2.close()  
                    #f2.write('%s,"%s","%s"\n'% (s[0],s[1],url[0]))
                else:
                    key = re.findall('{"title":"([\S ]+) - 维基百科,自由的百科全书","url":"',content_w)
                    url = re.findall(' - 维基百科,自由的百科全书","url":"([\S]+)"}',content_w)               
                    if url:
                        if str(key[0])==str(s[1]):                  
                            f2 = open(file2,'w',encoding='utf-8')
                            f2.write('%s,"%s","%s"\n'% (s[0],s[1],url[0]))
                            f2.close() 
                        else:                   
                            f2 = open(file3,'w',encoding='utf-8')
                            f2.write('%s,"%s","%s","%s"\n'% (s[0],s[1],key[0],url[0]))
                            f2.close()  
                        #f2.write('%s,"%s","%s"\n'% (s[0],s[1],url[0]))
##                    else:
##                        url_b = 'http://www.baidu.com/baidu?word='+string+'%20%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91&ie=utf-8'
##                        content_b =urllib.request.urlopen(url_b,timeout=2).read().decode('utf-8')
##                        key = re.findall("title : '([\S]+)_百度百科', link : ",content_b)
##                        url = re.findall("_百度百科', link : '([\S]+)'}",content_b)                    
##                        if url:
##                            pass
##                        else:
##                            url_s = 'http://www.baidu.com/baidu?word='+string+'%20%E6%90%9C%E6%90%9C%E7%99%BE%E7%A7%91&ie=utf-8'
##                            content_s =urllib.request.urlopen(url_s,timeout=2).read().decode('utf-8')
##                            key = re.findall('{"title":"([\S]+) - 搜搜百科","url":"',content_s)
##                            url = re.findall(' - 搜搜百科","url":"([\S]+)"}',content_s)
##                            if url:
##                                pass
##                                    #f2.write('%s,"%s","%s"\n'% (s[0],s[1],url[0]))
##                if url:                    
##                    f2 = open(file2,'w',encoding='utf-8')
##                    f2.write('%s,"%s","%s","%s"\n'% (s[0],s[1],key[0],url[0]))
##                    f2.close()                    
##                else:
##                    pass
            except:
                #proxy.remove(proxyIp)
                #badIp.write(proxyIp+'\n')
                say = '%s_%s error!'% (s[0],s[1])
        else:
            pass
#    badIp.close()
    if os.path.isfile(file2) == False and os.path.isfile(file3) == False:
        say = '%s_%s is failed！！！'% (s[0],s[1])    
    print(say)
            
def main():
    host = '192.168.1.15'
    user = 'data'
    pwd  = 'skst'
    db   = 'wwere_v3'
    cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
    cursor = cnx.cursor()
    #sql = "SELECT l.localId,t.localName,c.cityName FROM (landmark l left join townfile_local t on l.localId=t.localId) left join city c on t.cityId=c.cityId where l.landmarkRank>0 and t.localName regexp '^[a-z]' and l.linkUrl='' and l.updateTime > '2014-04-01 00:00:00'"
    sql = "SELECT l.localId,t.localName FROM landmark l left join townfile_local t on l.localId=t.localId where l.landmarkRank>0 and l.linkUrl='' and l.updateTime > '2014-04-16 17:59:00' and l.updateTime < '2014-04-17 15:31:00'"
    cursor.execute(sql)
    result = cursor.fetchall()
    proclist = []
    pool     = Pool(processes=100)
    for s in result:
        if s[1]:
            result = pool.apply_async(geturl,(s,))
        else:
            pass
    time.sleep(5)
    pool.close()
    pool.join()
    cnx.commit()
    cursor.close()
    cnx.close()
    
if __name__ == '__main__':
    print('start')
    main()
    os.system('pause')

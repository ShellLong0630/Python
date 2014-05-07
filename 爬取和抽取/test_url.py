import httplib2,urllib.request,re,os,time,mysql.connector,random
from multiprocessing import Pool
import multiprocessing

'''
s = '北京大学'   
string = urllib.request.quote(s)
url_w = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
url_b = 'http://www.baidu.com/baidu?word='+string+'%20%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91&ie=utf-8'
url_s = 'http://www.baidu.com/baidu?word='+string+'%20%E6%90%9C%E6%90%9C%E7%99%BE%E7%A7%91&ie=utf-8'

content_w =urllib.request.urlopen(url_w,timeout=10).read().decode('utf-8')
content_b =urllib.request.urlopen(url_b,timeout=10).read().decode('utf-8')
content_s =urllib.request.urlopen(url_s,timeout=10).read().decode('utf-8')

url_b = re.findall("title : '北京大学_百度百科', link : '([\S]+)'}",content_b)[0]
url_s = re.findall('{"title":"北京大学 - 搜搜百科","url":"([\S]+)"}',content_s)[0]
url_w = re.findall('{"title":"北京大学 - 维基百科,自由的百科全书","url":"([\S]+)"}',content_w)[0]
print(url_w)
print(url_b)
print(url_s)

'''
url_w = 'http://en.wikipedia.org/wiki/Dolphin%27s_Nose_Coonoor'
content_w =urllib.request.urlopen(url_w,timeout=10).read().decode('utf-8')
print(content_w)
jpg = re.findall('<img[^<]+src="(//upload.wikimedia.org/wikipedia/commons/thumb/[\d]+/[\S]+/[\S]+.jpg/[\S]+.jpg)',content_w)
print(jpg)
if re.findall('wikipedia',content_w) :
    print(jpg[0].replace('/commons/thumb','/commons').split('.jpg/')[0]+'.jpg')
##key = re.findall('{"title":"([\S ]+) - Wikipedia, the free encyclopedia","url":"',content_w)
##url = re.findall(' - Wikipedia, the free encyclopedia","url":"([\S]+)"}',content_w)                               
##if url :
##    print(content_w)
##    print(key,url)
##else:
##    key = re.findall('{"title":"([\S]+) - 维基百科,自由的百科全书","url":"',content_w)
##    url = re.findall(' - 维基百科,自由的百科全书","url":"([\S]+)"}',content_w)               
##    if url:
##        print(key,url)


##host = '192.168.1.15'
##user = 'data'
##pwd  = 'skst'
##db   = 'd01_backup'
##cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
##cursor = cnx.cursor()
##sql = 'SELECT m.localId,n.localName,m.landmark FROM local_stars m left join townfile_local n ON m.localId=n.localId WHERE landmark>0 limit 500'
##cursor.execute(sql)
##result = cursor.fetchall()
##for s in result:
##    if s[1]:
##        file2 = 'D:\\张玉龙\\Python\\url\\%s_%s.txt'% (s[0],s[1])
##        if os.path.isfile(file2)==True:
##            pass
##        else:
##            f2 = open(file2,'w',encoding='utf-8')
##            say = '%s_%s  ~ok~'% (s[0],s[1])
##            string = urllib.request.quote(s[1])
##            headers = {
##                "Accept":"text/html, */*; q=0.01",
##                "Accept-Language":"zh-CN,zh;q=0.8",
##                "Connection":"keep-alive",
##                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36"}
##            try:
##                url_w = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
##                req = urllib.request.Request(url_w,None,headers)
##                content_w =urllib.request.urlopen(req,timeout=2).read().decode('utf-8')
##                #print(content_w)
##                url_w = re.findall('{"title":"'+s[1]+' - 维基百科,自由的百科全书","url":"([\S]+)"}',content_w)
##                
##                if url_w:
##                    f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_w[0]))
##                else:
##                    url_b = 'http://www.baidu.com/baidu?word='+string+'%20%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91&ie=utf-8'
##                    req = urllib.request.Request(url_b,None,headers)
##                    content_b =urllib.request.urlopen(req,timeout=2).read().decode('utf-8')
##                    url_b = re.findall("title : '"+s[1]+"_百度百科', link : '([\S]+)'}",content_b)
##                    if url_b:
##                        f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_b[0]))
##                    else:
##                        url_s = 'http://www.baidu.com/baidu?word='+string+'%20%E6%90%9C%E6%90%9C%E7%99%BE%E7%A7%91&ie=utf-8'
##                        req = urllib.request.Request(url_s,None,headers)
##                        content_s =urllib.request.urlopen(req,timeout=2).read().decode('utf-8')    
##                        url_s = re.findall('{"title":"'+s[1]+' - 搜搜百科","url":"([\S]+)"}',content_s)
##                        if url_s:
##                            f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_s[0]))
##                        else:
##                            f2.close()
##                            os.remove(f2)
##                            say = '%s_%s  ~null~'% (s[0],s[1])
##                print(say)
##            except:
##                f2.close()
##                os.remove(file2)
##                print('%s_%s error!'% (s[0],s[1]))
##            f2.close()
##    else:
##        pass
##cnx.commit()
##cursor.close()
##cnx.close()

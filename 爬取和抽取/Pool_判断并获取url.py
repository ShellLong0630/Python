import httplib2,urllib.request,re,os,time,mysql.connector,random
from multiprocessing import Pool
import multiprocessing
  
def geturl(m):
    s = m    
    file2 = 'D:\\张玉龙\\Python\\url\\%s_%s.txt'% (s[0],s[1])
    if os.path.isfile(file2)==True:
        pass
    else:
        f2 = open(file2,'w',encoding='utf-8')
        say = '%s_%s  ~ok~'% (s[0],s[1])
        string = urllib.request.quote(s[1])
        try:
            url_w = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
            content_w =urllib.request.urlopen(url_w,timeout=2).read().decode('utf-8')
            #print(content_w)
            url_w = re.findall('{"title":"'+s[1]+' - 维基百科,自由的百科全书","url":"([\S]+)"}',content_w)
            
            if url_w:
                f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_w[0]))
            else:
                url_b = 'http://www.baidu.com/baidu?word='+string+'%20%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91&ie=utf-8'
                content_b =urllib.request.urlopen(url_b,timeout=2).read().decode('utf-8')
                url_b = re.findall("title : '"+s[1]+"_百度百科', link : '([\S]+)'}",content_b)
                if url_b:
                    f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_b[0]))
                else:
                    url_s = 'http://www.baidu.com/baidu?word='+string+'%20%E6%90%9C%E6%90%9C%E7%99%BE%E7%A7%91&ie=utf-8'
                    content_s =urllib.request.urlopen(url_s,timeout=2).read().decode('utf-8')    
                    url_s = re.findall('{"title":"'+s[1]+' - 搜搜百科","url":"([\S]+)"}',content_s)
                    if url_s:
                        f2.write('%s,"%s","%s"\n'% (s[0],s[1],url_s[0]))
                    else:
                        f2.close()
                        os.remove(f2)
                        say = '%s_%s  ~null~'% (s[0],s[1])
            print(say)
        except:
            f2.close()
            os.remove(file2)
            print('%s_%s error!'% (s[0],s[1]))
        f2.close()
def main():
    host = '192.168.1.15'
    user = 'data'
    pwd  = 'skst'
    db   = 'd01_backup'
    cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
    cursor = cnx.cursor()
    sql = "SELECT l.localId,t.localName,c.cityName FROM (landmark l left join townfile_local t on l.localId=t.localId) left join city c on t.cityId=c.cityId where l.landmarkRank>0 and t.localName regexp '^[a-z]' and l.linkUrl='' and l.updateTime > '2014-04-01 00:00:00'"
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

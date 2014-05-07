import httplib2,urllib.request,re,os,time,mysql.connector,random
from multiprocessing import Pool
import multiprocessing
  
def geturl(m):
    s = m
       
    string = urllib.request.quote(s[1])
    url = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
    try:
        content=urllib.request.urlopen(url,timeout=10).read().decode('utf-8')
    except:
        say = str(s[0])+"  filed!"
    find = '		><em>%s</em> - <em>维基百科</em>,自由的百科全书</a>'% s[1]
    i=0
    
    file2 = 'd:/张玉龙/Python/url_0408/%s_%s.txt'% (s[0],s[1])
    f2 = open(file2,'w',encoding='utf-8')
    f2.write(content)
    f2.close()
    
    f3 = open(file2,'r',encoding='utf-8')
    write = '%s,"%s",%s'% (s[0],s[1],'""\n')        
    say = str(s[1])+'  ~null~'
    for t in f3:
        if re.findall(find,t):
            i=1
        elif re.findall('          href="http://www.baidu.com/link',t):
            url = re.split('href=',t)[1]
            i+=1
            if i==2:
                write = '%s,"%s",%s'% (s[0],s[1],url)
                say = str(s[1])+'  ~ok~'
                break
            else:
                break               
    f3.close()
    #time.sleep(random.random())
    f1 = open('d:/张玉龙/Python/url.txt','a',encoding='utf-8')
    f1.write(write)
    f1.close()
    #time.sleep(random.random()+1)
    print(say)
    
def main():
    host = '192.168.1.15'
    user = 'data'
    pwd  = 'skst'
    db   = 'wwere_v3'
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
